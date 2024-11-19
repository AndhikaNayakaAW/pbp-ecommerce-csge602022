from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from main.models import Product


from main.forms import ProductForm  # Import the ProductForm
from main.models import Product  # Import the Product model
from django.utils.html import strip_tags


import datetime

# Existing index view
def index(request):
    context = {
        'app_name': 'E-Commerce Application',
        'student_name': 'Andhika Nayaka Arya Wibowo',
        'student_id': '2306174135',
        'class_name': 'KKI CSGE602022 Platform-Based Programming',
        'last_login': request.COOKIES.get('last_login', 'Unknown'),
        'name': request.user.username,
    }
    return render(request, 'main/index.html', context)

# Function to update product image URLs and descriptions
def update_product_images():
    product1 = Product.objects.filter(name="Sonny Angel - Series 1").first()
    if product1:
        product1.image_url = "https://raw.githubusercontent.com/AndhikaNayakaAW/Nayaka/main/Series%20dinasaur%20cummon.jpg"
        product1.description = "A cute Sonny Angel minifigure from Series Dinosaur, Rarity (Common)"
        product1.save()

    product2 = Product.objects.filter(name="Sonny Angel - Secret Edition").first()
    if product2:
        product2.image_url = "https://raw.githubusercontent.com/AndhikaNayakaAW/Nayaka/main/series%20dinosaur%20secret.jpg"
        product2.description = "A rare secret edition Sonny Angel minifigure from Series Dinosaur, Rarity (Secret)"
        product2.save()

@login_required  # Ensure the user is logged in
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # Assign the logged-in user to the product
            product.save()
            return redirect('main:show_main')
    else:
        form = ProductForm()
    return render(request, 'main/create_product_entry.html', {'form': form})

# View to display products on the main page
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)  # Only fetch products for the logged-in user
    last_login = request.COOKIES.get('last_login', 'Unknown')

    total_products = products.count()
    total_stock = sum(product.stock for product in products)

    context = {
        'name': request.user.username,
        'app_name': 'E-Commerce Application',
        'products': products,
        'student_name': 'Andhika Nayaka Arya Wibowo',
        'student_id': '2306174135',
        'class_name': 'KKI CSGE602022 Platform-Based Programming',
        'last_login': last_login,
        'total_products': total_products,
        'total_stock': total_stock,
    }
    return render(request, 'main/main.html', context)

# View to return products in XML format (only for logged-in user)
def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# View to return products in JSON format (only for logged-in user)
def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# View to return a product by ID in XML format
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id, user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# View to return a product by ID in JSON format
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id, user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Edit product view
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, user=request.user)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "main/edit_product.html", context)

# User registration view
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'main/register.html', context)

# User login view
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', now().strftime('%Y-%m-%d %H:%M:%S'))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'main/login.html', context)

# User logout view
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# Delete product view
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, user=request.user)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

# New function to add product with AJAX
@csrf_exempt
@require_POST
def add_product_ajax(request):
    if request.method == 'POST':
        try:
            # Parse JSON data
            data = json.loads(request.body)

            # Extract and sanitize fields
            name = strip_tags(data.get("name"))
            price = data.get("price")  # No need to strip_tags, this is an integer field
            description = strip_tags(data.get("description"))
            rarity = strip_tags(data.get("rarity"))
            stock = data.get("stock")  # No need to strip_tags, this is an integer field
            image_url = strip_tags(data.get("image_url"))
            user = request.user

            # Check if all required fields are present
            if not all([name, price, description, rarity, stock, image_url]):
                return HttpResponse('Missing required fields', status=400)

            # Create and save the new product
            new_product = Product(
                name=name,
                price=price,
                description=description,
                rarity=rarity,
                stock=stock,
                image_url=image_url,
                user=user
            )
            new_product.save()

            # Return success response
            return HttpResponse('Product created successfully', status=201)

        except json.JSONDecodeError:
            return HttpResponse('Invalid JSON data', status=400)
        except Exception as e:
            return HttpResponse(f'Error occurred: {str(e)}', status=400)

    return HttpResponse('Invalid request method', status=405)

# Product list view (Optional, in case needed)
@login_required(login_url='/login')
def product_list(request):
    products = Product.objects.filter(user=request.user)
    return render(request, 'main/main.html', {'products': products})

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from Flutter
            data = json.loads(request.body)
            
            # Extract data
            name = data.get('name', '').strip()
            price = data.get('price')
            description = data.get('description', '').strip()
            rarity = data.get('rarity', '').strip()
            stock = data.get('stock')
            image_url = data.get('image_url', '').strip()

            # Validate input data
            if not all([name, price, description, rarity, stock, image_url]):
                return JsonResponse({
                    "status": False,
                    "message": "All fields are required."
                }, status=400)

            # Check if the user is authenticated
            if not request.user.is_authenticated:
                return JsonResponse({
                    "status": False,
                    "message": "User not authenticated."
                }, status=401)

            # Create and save the product
            product = Product.objects.create(
                name=name,
                price=price,
                description=description,
                rarity=rarity,
                stock=stock,
                image_url=image_url,
                user=request.user  # Associate product with logged-in user
            )

            return JsonResponse({
                "status": True,
                "message": "Product created successfully!",
                "product_id": product.id
            }, status=201)

        except Exception as e:
            return JsonResponse({
                "status": False,
                "message": f"An error occurred: {str(e)}"
            }, status=500)

    return JsonResponse({
        "status": False,
        "message": "Invalid request method."
    }, status=405)
