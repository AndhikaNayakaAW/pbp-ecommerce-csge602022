from django.shortcuts import render
from .models import Product  # Import the Product model

# Create your views here.
def index(request):
    # Check if there are no products and create them only if they don't exist
    if Product.objects.count() == 0:
        # Create Sonny Angel products
        Product.objects.create(
            name='Sonny Angel - Series 1',
            price=100,
            description='A cute Sonny Angel minifigure from Series 1.',
            rarity='Common',
            stock=20,
            image_url='http://example.com/image1.jpg'
        )
        Product.objects.create(
            name='Sonny Angel - Secret Edition',
            price=300,
            description='A rare secret edition Sonny Angel.',
            rarity='Secret',
            stock=2,
            image_url='http://example.com/image2.jpg'
        )

    products = Product.objects.all()  # Retrieve all products from the database
    context = {
        'app_name': 'E-Commerce Application',
        'student_name': 'Andhika Nayaka Arya Wibowo',  
        'student_id': '2306174135',
        'class_name': 'CSGE602022 Platform-Based Programming',
        'products': products,  # Pass the products to the template
    }
    return render(request, 'main/index.html', context)
