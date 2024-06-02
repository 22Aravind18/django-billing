# Billing System

## Setup Instructions

1. **Clone the Repo**

   ```bash
   git clone repo-url
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv my_venv
   .\my_venv\Scripts\activate
   ```

3. **Change Directory**

   Change the directory to the Django project directory:
   
   ```bash
   cd django-billing/mallow/billing_system
   ```

4. **Install Dependencies**

   Run the `requirements.txt` file to install the dependency packages:
   
   ```bash
   pip install -r requirements.txt
   ```

5. **Create django secret key**
6. 
   To run and access the billing page, create a secret using the command:
   
   ```bash
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```
   
   Create a secret variable named "SECRET_KEY" and append the randomly generated secret string with the prefix "django-insecure-" in settings.py file
   

7. **Run the Server**

   Run the server by executing the following command:
   
   ```bash
   python manage.py runserver
   ```
