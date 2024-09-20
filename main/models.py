from django.db import models
import uuid  # Add this for UUID
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Use UUID for primary key
    name = models.CharField(max_length=200)  # Name of the product (e.g., Sonny Angel)
    price = models.IntegerField()  # Price of the product
    description = models.TextField()  # Description of the product
    rarity = models.CharField(max_length=100, choices=[('Common', 'Common'), ('Rare', 'Rare'), ('Secret', 'Secret')], default='Common')  # Rarity of the toy
    stock = models.IntegerField(default=0)  # Stock available
    image_url = models.URLField(max_length=200, blank=True)  # URL of the product image (optional)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link product to a user

    def __str__(self):
        return self.name
