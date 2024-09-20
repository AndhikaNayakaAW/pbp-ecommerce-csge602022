# E-Commerce Application - README

## Created by: Andhika Nayaka Arya Wibowo  
**Student ID:** 2306174135  
**Course:** KKI CSGE602022 Platform-Based Programming

## Deployed Application Link
You can access the deployed application [here](http://andhika-nayaka-ecommerce.pbp.cs.ui.ac.id/).

---
## First README Assignment

### 1. Implementation Checklist: Step-by-step Explanation

#### Step 1: Create a New Django Project
- I created a new Django project named `ecommerce_project` using the command `django-admin startproject ecommerce_project`.

#### Step 2: Create a New App
- Inside the project, I created an app called `main` using the command `python manage.py startapp main`.
  
#### Step 3: Routing Configuration
- I configured the URLs by editing `urls.py` in the project directory and including the URL routing for the `main` app.
  
#### Step 4: Create the Model
- I defined the `Product` model inside the `models.py` file of the `main` app. This model includes the mandatory attributes `name`, `price`, and `description`, as well as additional attributes like `rarity`, `stock`, and `image_url`.

#### Step 5: Views and Templates
- I created a function `index()` in `views.py` that retrieves all products and passes them to an HTML template (`index.html`) to display the name of the application, my name, and class.

#### Step 6: Add Products
- Using the Django shell, I added several products (Sonny Angels) with their respective details (name, price, description, etc.).

#### Step 7: Deployment to PWS
- I initialized the repository for PWS using the provided credentials and commands. Then, I pushed the code to PWS using Git and deployed the app successfully.

---

## 2. Client Request and Server Response Diagram

Below is a diagram that shows the flow of a request from a client to a Django-based web application and the response it gives:

![Django Request-Response Diagram](<https://github.com/AndhikaNayakaAW/Nayaka/blob/main/Request-Response%20Cycle%20In%20A%20Django%20Web%20Application.jpg?raw=true>)

**Explanation:**
- **Client Request**: The client (typically a web browser) sends an HTTP request to the Django server. This request is usually for a specific URL.
- **urls.py (URL Routing)**: The Django server receives the request and looks up the corresponding route in the `urls.py` file. This file defines which view function or class should handle a particular URL pattern.
- **views.py (Logic Processing)**: Once a matching route is found, the request is passed to a view function or class in `views.py`. Here, the logic for handling the request is processed, including any business rules.
- **models.py (Database Interaction)**: If the view needs to retrieve or update data, it interacts with the database using Django models. These models are defined in `models.py`, representing the structure of the data stored in the database.
- **views.py (Prepare Data)**: After interacting with the database and processing the request, the view prepares the data (if any) to be passed to the template for rendering.
- **HTML Template (Render Data)**: The view renders the data using an HTML template. The template receives the data and outputs an HTML page dynamically generated with the relevant content.
- **Response to Client**: The server sends the rendered HTML page as a response back to the client. The client displays this page in the browser.


---

## 3. Explanation of Git in Software Development

Git is a version control system that helps developers track changes in their codebase over time. It allows multiple people to collaborate on a project by managing different versions of code efficiently. Some key benefits of using Git include:
- **Collaboration**: Enables developers to work together without overwriting each other’s changes.
- **Branching**: Developers can work on different features simultaneously and merge them when ready.
- **History**: Every change made to the project is recorded, making it easy to revert back to a previous state if necessary.

---

## 4. Why Django is an Excellent Starting Point for Learning Software Development

Django is a popular web framework due to several reasons that make it an ideal starting point:
- **Batteries-included framework**: It comes with a lot of built-in tools (authentication, ORM, admin panel, etc.) that help developers get started quickly.
- **Well-documented**: Django has extensive and detailed documentation, making it easier for beginners to understand and learn.
- **Scalable**: It is suitable for both small-scale projects and large, complex applications.
- **Encourages clean, pragmatic design**: Django enforces the separation of concerns by using the Model-View-Template (MVT) architecture, which helps new developers understand good practices from the beginning.

---

## 5. Why Django Model is Called an ORM

Django’s model is called an ORM (Object-Relational Mapping) because it allows developers to interact with the database using Python objects, without needing to write SQL queries directly. With Django’s ORM, models represent tables in the database, and the attributes of the models represent the columns in the table. This abstraction simplifies database interactions by allowing developers to use Python code to query and manipulate the database instead of SQL.

---

## Second README Assignment

### URL Routing for Views

### URL Routing for Views

I added the following URL routing for each view:

```python
from django.urls import path
from main.views import show_main, add_product, show_xml, show_json, show_xml_by_id, show_json_by_id, index
from .views import edit_product

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product/', add_product, name='add_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    path('index/', index, name='index'),
    path('edit-product/<uuid:product_id>/', edit_product, name='edit_product'),
]
```

### Explanation Questions

1. **Why do we need data delivery in implementing a platform?**
   - Data delivery is essential in platform development to ensure communication between the client and server. It allows the server to send relevant information (e.g., products, user data) to the client and receive input (e.g., form submissions) from the client, which is critical for an interactive web application.

2. **Which is better, XML or JSON? Why is JSON more popular than XML?**
   - In my opinion, JSON is better than XML for most use cases. JSON is more lightweight, easier to read and write, and is natively supported in JavaScript, which is commonly used in web applications. JSON's popularity stems from its simplicity and better performance compared to XML.

3. **What is the functional usage of `is_valid()` in Django forms?**
   - The `is_valid()` method checks if the form has been filled out correctly according to the form's validation rules. It ensures that all fields have the expected data types and formats. Without `is_valid()`, the form might save incorrect or incomplete data.

4. **Why do we need `csrf_token` in Django forms? What could happen if we did not use it?**
   - `csrf_token` is required to protect the form from Cross-Site Request Forgery (CSRF) attacks. Without `csrf_token`, attackers could trick users into submitting malicious requests. If not used, an attacker could submit unauthorized requests on behalf of a user, potentially causing damage or gaining unauthorized access.

5. **Detailed Step-by-Step Implementation**
#### Step 1: Create a Form Input to Add a Product Object
First, I created a `forms.py` file in the `main` directory to handle the form for adding new products. The form is built using Django’s `ModelForm`, which automatically generates form fields based on the model's attributes.

In `forms.py`:

```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "rarity", "stock", "image_url"]
```

This form includes fields to capture the product's name, price, description, rarity, stock quantity, and image URL.

#### Step 2: Update `views.py` to Handle Product Creation

Next, I updated the `views.py` file to add a view that handles the form submission for creating a new product. This view checks if the form is valid and, if so, saves the new product to the database and redirects the user back to the main page.

In `views.py`:

```python
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()  # Save the product to the database
        return redirect('show_main')  # Redirect to the main page

    context = {'form': form}
    return render(request, "main/add_product.html", context)  # Render the form template
```

#### Step 3: Create `add_product.html` Template

I created a new HTML template to display the form where users can input the details of the new product. The form uses Django’s built-in CSRF protection and renders all fields using `form.as_table()` for simplicity.

In `main/templates/main/add_product.html`:

```html
{% extends 'base.html' %}

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```

#### Step 4: Display the Products on the Main Page

In `views.py`, I modified the `show_main` view to retrieve all the products from the database and pass them to the main template for rendering.

In `views.py`:

```python
def show_main(request):
    products = Product.objects.all()  # Fetch all products

    context = {
        'app_name': 'E-Commerce Application',
        'products': products,
        'student_name': 'Andhika Nayaka Arya Wibowo',
        'student_id': '2306174135',
        'class_name': 'KKI CSGE602022 Platform-Based Programming',
    }
    return render(request, 'main/main.html', context)  # Render the main page
```

#### Step 5: Create the `main.html` Template

The `main.html` template displays a table of products with their details such as name, price, description, and image. Additionally, an “Edit” button is added to each product that allows users to modify existing products.

In `main/templates/main/main.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ app_name }}</title>
</head>
<body>
    <h1>{{ app_name }}</h1>
    <p><strong>NPM:</strong> {{ student_id }}</p>
    <p><strong>Name:</strong> {{ student_name }}</p>
    <p><strong>Class:</strong> {{ class_name }}</p>

    <h2>Available Products</h2>

    {% if not products %}
        <p>There are no products available at the moment.</p>
    {% else %}
        <table border="1" cellpadding="10" cellspacing="0" style="border-collapse: collapse; width: 100%;">
            <thead>
                <tr>
                    <th>Product Name</th>
                    <th>Price</th>
                    <th>Description and Rarity</th>
                    <th>Stock</th>
                    <th>Image</th>
                    <th>Actions</th> <!-- Added a new column for actions like edit -->
                </tr>
            </thead>
            <tbody>
            {% for product in products %}
                <tr>
                    <td>{{ product.name }}</td>
                    <td>${{ product.price }}</td>
                    <td>{{ product.description }} <br> <strong>Rarity:</strong> {{ product.rarity }}</td>
                    <td>{{ product.stock }}</td>
                    <td><img src="{{ product.image_url }}" alt="{{ product.name }}" width="100"></td>
                    <td>
                        <a href="{% url 'edit_product' product.id %}">
                            <button>Edit</button>
                        </a>
                    </td>
                </tr>
            {% endfor %}
            </tbody>
        </table>
    {% endif %}

    <br>
    <a href="{% url 'add_product' %}">
        <button>Add New Product</button>
    </a>
</body>
</html>
```

#### Step 6: Add Views to Display Data in XML and JSON Formats

I added views in `views.py` to display the list of products in both XML and JSON formats. This allows other services to consume the product data via API.

In `views.py`:

```python
# XML format for all products
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# JSON format for all products
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# XML format for product by ID
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# JSON format for product by ID
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

#### Step 7: Create URL Routing for Each View

I updated the `urls.py` to add routes for each of the views, including the form for adding products, and the views to display data in XML and JSON formats.

In `urls.py`:

```python
from django.urls import path
from main.views import show_main, add_product, show_xml, show_json, show_xml_by_id, show_json_by_id, index
from .views import edit_product

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product/', add_product, name='add_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    path('index/', index, name='index'),
    path('edit-product/<uuid:product_id>/', edit_product, name='edit_product'),
]
```
Final Addition: Edit Button
To make editing products easier, I created an "Edit" button on the main.html template. This button links to an edit form, which allows users to modify the details of an existing product. The button was added in the "Actions" column of the product table for each product. The edit_product view was created to handle the form submission for editing the product, using a similar approach as the add_product view.

By completing these steps, the project is now able to handle the addition, display, and editing of products as well as expose the product data via XML and JSON endpoints.
8. **Screenshoot**
   **XML**
   ![](https://github.com/AndhikaNayakaAW/Nayaka/blob/ffab9afb27e160b70ec00840b5b1e3e3265cf4e7/XML.png)
   **XML ID**
   ![](https://github.com/AndhikaNayakaAW/Nayaka/blob/00598ea36a81437180a76fa9242c86bf6954fcd9/XML%20ID.png)
   **JSON**
   ![](https://github.com/AndhikaNayakaAW/Nayaka/blob/a88700c55122b50ac51f8f303638ba77808c0269/JSON.png)
   **JSON ID**
   ![](https://github.com/AndhikaNayakaAW/Nayaka/blob/f056e676dfa2effc7beb75aaa16c0d10559c95f7/JSON%20ID.png)

---
## Third README Assignment

### 1. What is the difference between `HttpResponseRedirect()` and `redirect()`?

- **`HttpResponseRedirect()`**: This function is a low-level response object that takes a URL and creates an HTTP response redirecting the user to that URL. It is part of the Django `http` module and requires you to manually specify the target URL as a string.
  
  Example:
  ```python
  return HttpResponseRedirect('/some-url/')
  ```

- **`redirect()`**: This is a high-level utility function in Django that handles redirection more efficiently. It can take not just a URL, but also a view name and any required arguments for that view. The `redirect()` function abstracts some of the work by figuring out the URL for you if you pass it a view name or model instance.
  
  Example:
  ```python
  return redirect('some-view-name')
  ```

  In short, `redirect()` is a more convenient and flexible function that internally uses `HttpResponseRedirect()`.

### 2. Explain how the `MoodEntry` model is linked with `User`!

- In Django, models can be linked to the `User` model using a **ForeignKey** relationship. The `MoodEntry` model is likely linked to the `User` model by using `models.ForeignKey(User, on_delete=models.CASCADE)` in its definition. This sets up a one-to-many relationship, meaning each user can have multiple mood entries, but each `MoodEntry` is associated with exactly one user.

  Example:
  ```python
  from django.contrib.auth.models import User
  from django.db import models

  class MoodEntry(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      mood = models.CharField(max_length=100)
      date = models.DateField(auto_now_add=True)
  ```

  Here, the `user` field in `MoodEntry` links each mood entry to a specific user.

### 3. What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.

- **Authentication**: This is the process of verifying a user's identity. In Django, authentication typically happens when the user submits a login form. If the credentials are correct, the user is considered authenticated.

- **Authorization**: This determines what an authenticated user is allowed to do. For instance, whether the user can access a particular page or perform certain actions is part of authorization.

  **When a user logs in**:
  - Django authenticates the user by checking their username and password.
  - Upon successful authentication, Django creates a session for the user and stores their ID in the session. This allows Django to identify the user in future requests.

  **How Django implements this**:
  - Django uses the `authenticate()` function to check credentials.
  - If successful, `login()` is called to set up the session.
  - For authorization, Django uses decorators like `@login_required` and permission classes like `PermissionRequiredMixin`.

### 4. How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.

- **Django remembers logged-in users** by using **sessions** and **cookies**. After a user logs in, Django creates a session and stores the session ID in a cookie on the user's browser. This session ID is then used on subsequent requests to identify the user. The cookie usually contains a session key like `sessionid`.

- **Other uses of cookies**:
  - Storing user preferences (like dark mode settings).
  - Keeping track of items in a shopping cart.
  - Analytics and tracking purposes.

- **Are all cookies safe?**:
  Not all cookies are inherently safe. It depends on how they are used and their contents:
  - **Session cookies** used by Django are safe if used correctly.
  - **Persistent cookies** (those that last beyond a session) can pose risks if they store sensitive information.
  - **Secure** and **HttpOnly** flags should be used to ensure cookies are only transmitted over HTTPS and are not accessible via JavaScript.

### 5. Explain how did you implement the checklist step-by-step (apart from following the tutorial).

1. **Set up the Django project**: Created a new Django project and app. Defined the necessary models (like `Product` or `MoodEntry`).
2. **Created templates**: Designed HTML templates for displaying data such as products, login, and registration forms.
3. **Defined views**: Implemented views to handle user authentication, product management, and data rendering in the templates.
4. **Added cookies for last login**: After successful login, I added a cookie to store the last login time and displayed it on the main page.
5. **Set up routes**: Defined the URL patterns in `urls.py` to connect views with routes.
6. **Tested functionality**: Thoroughly tested each feature, including login, product display, and cookie-based last login tracking.

### 6. Perform add-commit-push to GitHub.

1. **Add files to staging**:
   ```bash
   git add .
   ```

2. **Commit changes**:
   ```bash
   git commit -m "Implemented user login and product functionality"
   ```

3. **Push to GitHub**:
   ```bash
   git push origin main
   ```
```
