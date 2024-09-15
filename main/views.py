from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect
from main.forms import ProductForm  # Import the ProductForm
from main.models import Product  # Import the Product model

# Existing index view
def index(request):
    # Prepare the context with basic information
    context = {
        'app_name': 'E-Commerce Application',
        'student_name': 'Andhika Nayaka Arya Wibowo',
        'student_id': '2306174135',
        'class_name': 'CSGE602022 Platform-Based Programming',
    }
    return render(request, 'main/index.html', context)

# View to add a new product
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()  # Save the product to the database
        return redirect('index')  # Redirect back to the index page

    context = {'form': form}
    return render(request, "main/add_product.html", context)  # Render the form template

# View to display products on the main page
def show_main(request):
    products = Product.objects.all()  # Fetch all products

    context = {
        'app_name': 'E-Commerce Application',
        'products': products,  # Pass products to the template
        'student_name': 'Andhika Nayaka Arya Wibowo',
        'student_id': '2306174135',
        'class_name': 'CSGE602022 Platform-Based Programming',
    }
    return render(request, 'main/main.html', context)  # Render the main page

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
    data = Product.objects.filter(pk=id)  # Query product by ID
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# New view to return a product by ID in JSON format
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)  # Query product by ID
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
