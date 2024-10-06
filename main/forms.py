from django import forms
from main.models import Product  # Import the Product model
from django.utils.html import strip_tags


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "rarity", "stock", "image_url"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_rarity(self):
        rarity = self.cleaned_data["rarity"]
        return strip_tags(rarity)

    def clean_image_url(self):
        image_url = self.cleaned_data["image_url"]
        return strip_tags(image_url)