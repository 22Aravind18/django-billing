from django import forms
from .models import Product

class ProductModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f'{obj.name} - ${obj.price}'

class ProductForm(forms.Form):
    product = ProductModelChoiceField(queryset=Product.objects.all(), empty_label="Select a product")
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'placeholder': 'Quantity'}))

class BillingForm(forms.Form):
    customer_email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email ID'}))
    paid_amount = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Amount'}))

ProductFormSet = forms.formset_factory(ProductForm, extra=1)