from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.utils.timezone import now


from main.forms import ProductForm  # Import the ProductForm
from main.models import Product  # Import the Product model

import datetime

# Existing index view
def index(request):
    # Prepare the context with basic information
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
    # Update the image and description for Sonny Angel - Series Dinosaur (Common)
    product1 = Product.objects.filter(name="Sonny Angel - Series 1").first()
    if product1:
        product1.image_url = "https://raw.githubusercontent.com/AndhikaNayakaAW/Nayaka/main/Series%20dinasaur%20cummon.jpg"
        product1.description = "A cute Sonny Angel minifigure from Series Dinosaur, Rarity (Common)"
        product1.save()

    # Update the image and description for Sonny Angel - Secret Edition Dinosaur
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
            return redirect('main:show_main')  # Redirect to the main page instead of the product list
    else:
        form = ProductForm()
    return render(request, 'main/create_product_entry.html', {'form': form})

# View to display products on the main page
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)  # Only fetch products for the logged-in user
    last_login = request.COOKIES.get('last_login', 'Unknown')

    context = {
        'name': request.user.username,
        'app_name': 'E-Commerce Application',
        'products': products,  # Pass filtered products to the template
        'student_name': 'Andhika Nayaka Arya Wibowo',
        'student_id': '2306174135',
        'class_name': 'KKI CSGE602022 Platform-Based Programming',
        'last_login': last_login,  # Add last login to context
    }
    return render(request, 'main/main.html', context)

# View to return products in XML format
def show_xml(request):
    data = Product.objects.all()  # Query all products
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# View to return products in JSON format
def show_json(request):
    data = Product.objects.all()  # Query all products
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# New view to return a product by ID in XML format
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)  # Query product by UUID
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# New view to return a product by ID in JSON format
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)  # Query product by UUID
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Edit product view
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        # Redirect to the main page after editing
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
    context = {'form':form}
    return render(request, 'register.html', context)

# User login view
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Set a cookie with the current time as the last login
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', now().strftime('%Y-%m-%d %H:%M:%S'))  # Save login time in cookie
            return response
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

def delete_product(request, product_id):
    # Get product based on id
    product = get_object_or_404(Product, id=product_id)
    # Delete product
    product.delete()
    # Return to the main page
    return HttpResponseRedirect(reverse('main:show_main'))

def product_list(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'main/product_list.html', {'products': products})

