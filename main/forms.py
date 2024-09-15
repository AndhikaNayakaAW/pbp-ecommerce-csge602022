from django import forms
from main.models import Product  # Import the Product model

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product  # Connect the form to the Product model
        fields = ["name", "price", "description", "rarity", "stock", "image_url"]  # List the fields to be included in the form
