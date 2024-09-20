from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import ProductForm  # Import the ProductForm
from main.models import Product  # Import the Product model
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.timezone import now

# Existing index view
def index(request):
    # Prepare the context with basic information
    context = {
        'app_name': 'E-Commerce Application',
        'student_name': 'Andhika Nayaka Arya Wibowo',
        'student_id': '2306174135',
        'class_name': 'KKI CSGE602022 Platform-Based Programming',
        'last_login': request.COOKIES['last_login'],
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

# View to add a new product
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()  # Save the product to the database
        return redirect('show_main')  # Redirect to the main page

    context = {'form': form}
    return render(request, "main/add_product.html", context)  # Render the form template

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
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user  # Associate the product with the logged-in user
        product.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "main/add_product.html", context)