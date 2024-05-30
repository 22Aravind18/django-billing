from django.shortcuts import render, redirect
from .forms import BillingForm, ProductFormSet
from .models import Product, Purchase, PurchaseItem


def calculate_bill(products, paid_amount):
    total_price_without_tax = sum(p.price * q for p, q in products)
    total_tax = sum(p.price * q * p.tax_percentage / 100 for p, q in products)
    net_price = total_price_without_tax + total_tax
    balance = paid_amount - net_price

    return total_price_without_tax, total_tax, net_price, balance


def billing_view(request):
    if request.method == "POST":
        form = BillingForm(request.POST)
        formset = ProductFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            customer_email = form.cleaned_data['customer_email']
            paid_amount = form.cleaned_data['paid_amount']

            products = []
            for product_form in formset:
                product = product_form.cleaned_data.get('product')
                quantity = product_form.cleaned_data.get('quantity')
                if product and quantity:
                    products.append((product, quantity))

            total_price_without_tax, total_tax, net_price, balance = calculate_bill(products, paid_amount)

            # Create purchase record
            purchase = Purchase.objects.create(customer_email=customer_email, total_amount=net_price,
                                               paid_amount=paid_amount)

            # Collect calculated details for each product
            product_details = []
            for product, quantity in products:
                purchase_price = product.price * quantity
                tax_amount = purchase_price * product.tax_percentage / 100
                total_price = purchase_price + tax_amount

                product_details.append({
                    'product_id': product.product_id,
                    'unit_price': product.price,
                    'quantity': quantity,
                    'purchase_price': purchase_price,
                    'tax_percentage': product.tax_percentage,
                    'tax_amount': tax_amount,
                    'total_price': total_price,
                })

                # Create purchase items and adjust stock
                PurchaseItem.objects.create(purchase=purchase, product=product, quantity=quantity,
                                            total_price=purchase_price)
                product.available_stocks -= quantity
                product.save()

            # Create denominations for balance
            denominations = [500, 50, 20, 10, 5, 2, 1]
            balance_denominations = {}
            remaining_balance = int(balance)
            for denom in denominations:
                count = remaining_balance // denom
                balance_denominations[denom] = count
                remaining_balance = remaining_balance % denom

            context = {
                'customer_email': customer_email,
                'products': product_details,
                'total_price_without_tax': total_price_without_tax,
                'total_tax': total_tax,
                'net_price': net_price,
                'balance': balance,
                'balance_denominations': balance_denominations
            }
            return render(request, 'invoice.html', context)
        else:
            print(f"Form errors: {form.errors}")
            print(f"Formset errors: {formset.errors}")
    else:
        form = BillingForm()
        formset = ProductFormSet()

    denominations = [500, 50, 20, 10, 5, 2, 1]
    context = {'form': form, 'formset': formset, 'denominations': denominations}
    return render(request, 'billing.html', context)