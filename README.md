# E-Commerce Application - README

## Created by: Andhika Nayaka Arya Wibowo  
**Student ID:** 2306174135  
**Course:** KKI CSGE602022 Platform-Based Programming

## Deployed Application Link
You can access the deployed application [here](http://andhika-nayaka-ecommerce.pbp.cs.ui.ac.id/).

---
## First README Assignment

### 1. Implementation Checklist: Step-by-step Explanation

### Step 1: **Create a New Django Project**

- First, I set up a virtual environment to isolate my Django project dependencies. This ensures that the Python packages installed for this project don’t conflict with others.
  
  **Command to create a virtual environment:**
  ```bash
  python -m venv env
  ```

- I activated the virtual environment using the following command:

  **For macOS/Linux:**
  ```bash
  source env/bin/activate
  ```

  **For Windows:**
  ```bash
  .\env\Scripts\activate
  ```

- After activating the virtual environment, I installed Django by running the following command:

  ```bash
  pip install django
  ```

- Then, I created the Django project named `ecommerce_project` using Django’s `startproject` command:
  
  ```bash
  django-admin startproject ecommerce_project
  ```

  This command generates the basic project structure, including:
  - `manage.py`: The command-line utility to interact with the Django project.
  - `ecommerce_project/`: A directory containing project settings and configuration files like `settings.py`, `urls.py`, and `wsgi.py`.

---

### Step 2: **Create a New App**

- Inside the `ecommerce_project` directory, I created a new Django app named `main`. Apps in Django are self-contained modules that handle specific functionality (in this case, product management).

  **Command to create the `main` app:**
  ```bash
  python manage.py startapp main
  ```

  This command created a new directory `main/` with important files like:
  - `models.py`: Where the data models (database tables) are defined.
  - `views.py`: Where the logic for processing requests and rendering responses is written.
  - `forms.py`: For handling forms in Django (created later).
  - `urls.py`: For routing URLs to specific views (added later).

- I added the `main` app to the `INSTALLED_APPS` list in `settings.py` to let Django know about the existence of this app:

  ```python
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'main',  # Add the main app here
  ]
  ```

---

### Step 3: **Routing Configuration**

- Next, I set up URL routing to connect the views (that handle requests) with specific URL patterns. In Django, the `urls.py` file is where you define the mapping between URLs and the views that handle them.

- In `ecommerce_project/urls.py`, I included the `main` app’s URLs:

  ```python
  from django.contrib import admin
  from django.urls import path, include

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('main.urls')),  # Include the URLs from the main app
  ]
  ```

- Then, I created a `urls.py` file inside the `main` app to define the specific routes for product-related views, like the main product listing page, adding a product, etc.

  Example `urls.py` in the `main` app:
  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path('', views.index, name='index'),  # Route for the homepage
      path('add-product/', views.add_product, name='add_product'),
      # Other routes for product-related views
  ]
  ```

---

### Step 4: **Create the Model**

- In Django, models define the structure of the database tables. I defined a `Product` model inside `models.py` to store information about each product.

- The `Product` model includes attributes like `name`, `price`, `description`, `rarity`, `stock`, and `image_url`.

  **Code for the `Product` model:**
  ```python
  from django.db import models

  class Product(models.Model):
      name = models.CharField(max_length=100)
      price = models.DecimalField(max_digits=10, decimal_places=2)
      description = models.TextField()
      rarity = models.CharField(max_length=50)
      stock = models.PositiveIntegerField()
      image_url = models.URLField(max_length=200, blank=True, null=True)
      
      def __str__(self):
          return self.name
  ```

- After defining the model, I created and applied the migrations to set up the database:

  **Command to create migrations:**
  ```bash
  python manage.py makemigrations
  ```

  **Command to apply migrations and create the database table:**
  ```bash
  python manage.py migrate
  ```

---

### Step 5: **Views and Templates**

- In `views.py`, I created the `index` view that retrieves all the products from the database and passes them to an HTML template for display. The view uses Django’s ORM (Object-Relational Mapper) to interact with the database and fetch product records.

  **Code for the `index` view:**
  ```python
  from django.shortcuts import render
  from .models import Product

  def index(request):
      products = Product.objects.all()  # Query all products from the database
      context = {
          'products': products,
          'app_name': 'E-Commerce Application',
          'student_name': 'Andhika Nayaka Arya Wibowo',
          'student_id': '2306174135',
          'class_name': 'KKI CSGE602022 Platform-Based Programming',
      }
      return render(request, 'main/index.html', context)  # Render the index.html template
  ```

- Next, I created the `index.html` template inside the `templates/main/` directory. This template is responsible for displaying the name of the app, my details (name, student ID, and class), and the list of products.

  **Example of `index.html`:**
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
          <p>No products are available at the moment.</p>
      {% else %}
          <ul>
              {% for product in products %}
                  <li>{{ product.name }} - ${{ product.price }}</li>
              {% endfor %}
          </ul>
      {% endif %}
  </body>
  </html>
  ```

---

### Step 6: **Add Products**

- I manually added products using Django’s interactive shell. The shell allows direct interaction with the Django models and database.

  **Command to open the Django shell:**
  ```bash
  python manage.py shell
  ```

- Inside the shell, I created new products by instantiating the `Product` model and saving them to the database:

  **Code to add products in the shell:**
  ```python
  from main.models import Product

  product1 = Product(name='Sonny Angel - Series Dinosaur', price=100, description='A cute Sonny Angel minifigure from Series Dinosaur', rarity='Common', stock=20)
  product1.save()

  product2 = Product(name='Sonny Angel - Secret Dinosaur Edition', price=300, description='A rare secret edition Sonny Angel minifigure from Series Dinosaur', rarity='Secret', stock=2)
  product2.save()
  ```

- After adding several products, I confirmed they were displayed correctly on the product list page (`index.html`).

---

### Step 7: **Deployment to PWS**

- I prepared the project for deployment on PWS (Platform Web Service) by pushing the code to the repository.
  
- First, I initialized the project repository using Git, added the project files, and committed the changes:

  **Commands to initialize the Git repository and push code:**
  ```bash
  git init
  git add .
  git commit -m "Initial commit with product management functionality"
  ```

- I then configured the remote repository with the credentials provided by PWS, pushed the code, and deployed the app successfully.

  **Commands to push code to PWS and deploy:**
  ```bash
  git remote add origin https://pws-url.git
  git push -u origin main
  ```

- After deployment, I accessed the live application at the provided URL and verified that the product management features were working correctly.

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

---

### Step 1: **Set up the Django Project**

- First, I created a virtual environment for the project to isolate dependencies, ensuring a clean working environment for my Django app.
  
  **Command to create a virtual environment:**
  ```bash
  python -m venv env
  ```

  I activated the virtual environment using:

  **For macOS/Linux:**
  ```bash
  source env/bin/activate
  ```

  **For Windows:**
  ```bash
  .\env\Scripts\activate
  ```

- With the environment active, I installed Django using pip:

  ```bash
  pip install django
  ```

- I then created a new Django project using the following command:

  ```bash
  django-admin startproject ecommerce_project
  ```

  This generated the initial project files, including `manage.py` for project management, and the main project directory `ecommerce_project` containing configuration files like `settings.py`, `urls.py`, etc.

- To manage the specific product-related logic, I created a new app called `main`:

  ```bash
  python manage.py startapp main
  ```

  This created a new directory `main/` for the app’s models, views, templates, and other functionality.

- Next, I added the `main` app to the `INSTALLED_APPS` list in `settings.py` to let Django know that this app is part of the project:

  ```python
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'main',  # Register the main app
  ]
  ```

---

### Step 2: **Created Templates**

- I set up the directory structure for templates in the `main` app by creating a `templates` folder inside the `main` directory. Within this, I created another `main` folder to house all the HTML files.

  **Directory structure:**
  ```
  main/
    templates/
      main/
        base.html
        index.html
        add_product.html
        login.html
        register.html
  ```

- For each view (e.g., product list, login, registration), I designed corresponding templates. For example:

  **Example of `index.html`:**

  ```html
  {% extends 'base.html' %}

  {% block content %}
  <h1>Product List</h1>

  {% if not products %}
      <p>No products available at the moment.</p>
  {% else %}
      <ul>
      {% for product in products %}
          <li>{{ product.name }} - ${{ product.price }}</li>
      {% endfor %}
      </ul>
  {% endif %}
  {% endblock %}
  ```

- Each page was designed to be simple but functional, focusing on displaying relevant data like products, form inputs, and user information.

---

### Step 3: **Defined Views**

- I implemented views in `views.py` to handle user interactions and data rendering. These views retrieve data from the database and pass it to the templates.

- **Example: `index` view for product listing:**

  ```python
  from django.shortcuts import render
  from .models import Product

  def index(request):
      products = Product.objects.all()
      context = {
          'products': products,
          'app_name': 'E-Commerce Application',
          'student_name': 'Andhika Nayaka Arya Wibowo',
          'student_id': '2306174135',
          'class_name': 'KKI CSGE602022 Platform-Based Programming',
      }
      return render(request, 'main/index.html', context)
  ```

- I also created views to handle form submissions for user login, registration, and product management (add, edit, delete). Each view used Django’s form handling and validation mechanisms, ensuring data was correctly processed before being saved to the database.

- **Example: `add_product` view:**

  ```python
  from django.shortcuts import redirect
  from .forms import ProductForm

  def add_product(request):
      form = ProductForm(request.POST or None)
      
      if request.method == 'POST' and form.is_valid():
          form.save()
          return redirect('index')
      
      return render(request, 'main/add_product.html', {'form': form})
  ```

---

### Step 4: **Added Cookies for Last Login**

- To enhance the user experience, I implemented cookies to track and display the user’s last login time.

- After a user successfully logs in, I saved the current time as a cookie using `HttpResponse.set_cookie()`.

  **Code to set the last login cookie in `login_user` view:**
  
  ```python
  from django.utils.timezone import now
  from django.http import HttpResponseRedirect
  from django.contrib.auth import login

  def login_user(request):
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
          user = form.get_user()
          login(request, user)
          
          # Save last login time in a cookie
          response = HttpResponseRedirect(reverse('index'))
          response.set_cookie('last_login', now().strftime('%Y-%m-%d %H:%M:%S'))
          return response
  ```

- On the homepage (`index.html`), I retrieved the `last_login` cookie and displayed it for the user:

  **Code to display last login:**
  ```html
  <p>Last login session: {{ last_login }}</p>
  ```

  **View to retrieve and pass the last login cookie to the template:**

  ```python
  def index(request):
      last_login = request.COOKIES.get('last_login', 'Unknown')
      context = {
          'last_login': last_login,
          'app_name': 'E-Commerce Application',
          # Other context data
      }
      return render(request, 'main/index.html', context)
  ```

---

### Step 5: **Set Up Routes**

- I defined URL patterns in the `urls.py` file to route requests to the appropriate views. Each route corresponds to a specific view, such as showing the product list or processing a product form.

- **Example `urls.py`:**

  ```python
  from django.urls import path
  from .views import index, add_product, login_user

  urlpatterns = [
      path('', index, name='index'),
      path('add-product/', add_product, name='add_product'),
      path('login/', login_user, name='login'),
  ]
  ```

  This routing file ensures that when users visit specific URLs (e.g., `/add-product/`), the correct view is executed, and the appropriate template is rendered.

---

### Step 6: **Tested Functionality**

- Before final deployment, I thoroughly tested each feature to ensure they worked as expected:

  1. **Login Functionality**: I ensured that the user could log in and that the `last_login` cookie was correctly set and displayed on the homepage.
  
  2. **Product Management**: I tested the add, edit, and delete product functionalities. This involved filling out forms, validating data, and checking if products were saved to or removed from the database.

  3. **Cookies**: I verified that cookies were handled properly. After logging in, I ensured the last login time was stored in the browser’s cookies and displayed when the user revisited the site.

  4. **UI Responsiveness**: I tested the frontend design to ensure that the product list, forms, and other components displayed properly on both desktop and mobile devices. I used a combination of CSS frameworks and custom styling to make sure the site was visually appealing and functional.

---
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

## Fourth Assignment: Advanced Web Design Concepts

### 1. CSS Selector Priority

If there are multiple CSS selectors for an HTML element, the browser uses the **CSS specificity** to decide which style to apply. The order of priority for CSS selectors is as follows:

1. **Inline styles** (added directly to an element’s "style" attribute) have the highest priority.
   - Example: `<p style="color: red;">Hello</p>`
2. **ID selectors** (`#id`) have the next level of priority.
   - Example: `#header { color: blue; }`
3. **Class selectors** (`.class`), **attribute selectors** (`[type="text"]`), and **pseudo-classes** (`:hover`, `:focus`) are applied next.
   - Example: `.button { color: green; }`
4. **Element selectors** (like `div`, `p`, `a`) and **pseudo-elements** (`::before`, `::after`) have the lowest priority.
   - Example: `p { color: black; }`

In cases where selectors have equal specificity, the **order of appearance** in the stylesheet matters, with the latest rule overriding the earlier one. Additionally, the `!important` declaration can override all other rules, but it should be used sparingly to avoid complications.

---

### 2. Importance of Responsive Design

Responsive design ensures that a web application adjusts smoothly to different screen sizes and devices, improving the user experience on both desktop and mobile devices. It has become crucial due to the diversity of devices used to access websites, ranging from smartphones to large desktop monitors.

- **Why it’s important**:
   - Enhances accessibility across devices with varying screen sizes.
   - Improves user experience, leading to better engagement and conversion rates.
   - Reduces the need to maintain separate websites for mobile and desktop.

**Example of an application with responsive design**:  
Facebook’s web version dynamically adjusts its layout based on screen size, ensuring a good experience on both mobile phones and desktops.

**Example of an application without responsive design**:  
An older version of Reddit didn’t have responsive design, forcing users on mobile devices to zoom in and scroll horizontally to read content. This has since been updated.

---

### 3. Differences Between Margin, Border, and Padding

- **Margin**: The space **outside** the border of an element. It creates distance between the element and other elements around it.
   - Example: `margin: 20px;`
   - This creates a 20-pixel gap around the element.

- **Border**: The **outline** around the padding and content of an element. It is a visible line that surrounds the element.
   - Example: `border: 2px solid black;`
   - This adds a 2-pixel black solid line around the element.

- **Padding**: The space **inside** the border, between the border and the element’s content. Padding controls the space between the content and the edge of the element.
   - Example: `padding: 10px;`
   - This adds a 10-pixel gap between the content and the border.

Together, margin, border, and padding define the spacing and appearance of elements on the page, and understanding their use is critical for layout design.

---

### 4. Flexbox and Grid Layout

- **Flexbox**:
   - Flexbox is a layout model that allows elements to align and distribute space within a container dynamically, either in rows or columns. It’s ideal for building layouts where items need to be equally spaced or dynamically resized.
   - **Example**: A row of buttons that expands or contracts to fit the container width.
   - Key properties: `display: flex;`, `justify-content`, `align-items`, `flex-direction`.

- **Grid Layout**:
   - Grid layout provides a more structured and two-dimensional way to lay out elements, dividing the page into rows and columns. It is particularly useful for more complex layouts where both horizontal and vertical alignment is important.
   - **Example**: A photo gallery where images are displayed in a grid of rows and columns.
   - Key properties: `display: grid;`, `grid-template-columns`, `grid-gap`.

---

### 5. Step-by-Step Implementation of the Checklist

---

### 1. **Implement Functions to Delete and Edit Products**

#### a. **Edit Product Functionality**:
- I started by creating a view function in `views.py` to handle product editing. The function retrieves the specific product using its unique `id`, then displays its details in a form for editing.
- I used Django's `ModelForm` to populate the form with the product's existing data. This allows users to make changes to the fields like `name`, `price`, `description`, and `stock`.
  
   **Code for the edit function:**
   ```python
   def edit_product(request, product_id):
       product = get_object_or_404(Product, id=product_id)
       form = ProductForm(request.POST or None, instance=product)
   
       if form.is_valid() and request.method == "POST":
           form.save()
           # Redirect to the main page after editing
           return redirect('main:show_main')
   
       context = {'form': form}
       return render(request, "main/edit_product.html", context)
   ```

- I added an "Edit" button for each product in the product list. This button is placed within each product card, making it easy for users to directly navigate to the edit form of the corresponding product.
  
   **Code for the edit button:**
   ```html
   <td>
       <a href="{% url 'main:edit_product' product.id %}">
           <button>Edit</button>
       </a>           
   </td>
   ```

#### b. **Delete Product Functionality**:
- For the delete functionality, I created a separate view that uses the product's `id` to find and delete the product from the database. Before deletion, I added a confirmation prompt to ensure the user intends to delete the product.
  
   **Code for the delete function:**
   ```python
   def delete_product(request, product_id):
       product = get_object_or_404(Product, id=product_id)
       product.delete()  # Delete the product from the database
       return HttpResponseRedirect(reverse('main:show_main'))
   ```

- I added a "Delete" button within each product card. This button triggers the delete view, and when clicked, it asks for confirmation using JavaScript (`onclick="return confirm('Are you sure you want to delete this product?');"`).
  
   **Code for the delete button:**
   ```html
   <td>
       <a href="{% url 'main:delete_product' product.id %}" onclick="return confirm('Are you sure you want to delete this product?');">
           <button>Delete</button>
       </a>
   </td>
   ```

---

### 2. **Customize the Design of HTML Templates Using Tailwind CSS**

#### a. **Login, Register, and Add Product Pages Customization**:
- I applied **Tailwind CSS** to the login, registration, and add product pages to enhance the visual appeal and make the forms user-friendly.
  
   **Login Page Customization:**
   - Added a centered layout using Tailwind’s flexbox utilities (`flex`, `justify-center`, `items-center`) to align the form in the center of the page.
   - Tailwind form input classes (`input`, `bg-gray-200`, `focus:border-blue-500`, etc.) were applied to style the input fields and buttons, ensuring they look clean and modern.

   **Example of form styling in login.html**:
   ```html
   <form method="POST" class="bg-white p-6 rounded-lg shadow-md max-w-sm mx-auto">
       {% csrf_token %}
       <div>
           {{ form.as_p }}
       </div>
       <button type="submit" class="w-full bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600">
           Login
       </button>
   </form>
   ```

   **Add Product Page Customization:**
   - I used the same Tailwind classes to make the form responsive and visually appealing. The form has clear input fields, spacing, and buttons with hover effects.
   - This page also includes a section for the product image URL, which allows users to visually associate an image with the product.

#### b. **Product List Page Customization**:
- I implemented a card-based layout using **Tailwind CSS** to display each product’s details (name, price, description, stock, and image).
  
   **Code for product card styling:**
   ```html
   <div class="bg-white shadow-md rounded-lg p-6 mb-4">
       <h3 class="text-xl font-bold">{{ product.name }}</h3>
       <p class="text-gray-600">Price: ${{ product.price }}</p>
       <p class="text-gray-600">Stock: {{ product.stock }}</p>
       <p class="text-gray-600">Description: {{ product.description }}</p>
       <p class="text-gray-600">Rarity: {{ product.rarity }}</p>
       <img src="{{ product.image_url }}" alt="{{ product.name }}" class="w-32 h-32 object-cover">
   </div>
   ```

- I applied flexbox utilities (`flex`, `flex-wrap`) to ensure the cards are responsive and adjust automatically based on the screen size. On smaller screens, the cards stack vertically, while on larger screens, they are displayed in a grid.

#### c. **Responsive Design Implementation**:
- The layout automatically adjusts for different screen sizes (mobile, tablet, desktop) using **Tailwind’s responsive utilities**. I used the following key classes for responsiveness:
   - `w-full sm:w-1/2 lg:w-1/4`: This makes each product card take full width on small screens, half the width on medium screens, and one-fourth of the width on larger screens.
   - `hidden md:flex`: I used this class to hide elements on smaller screens and only show them on medium or larger screens (for example, showing the full navbar).

- **Handling No Products Scenario**:
   - If no products are available, I implemented logic in the `product_list.html` to show a custom message and a placeholder image instead of an empty product table.
  
   **Code for no products check**:
   ```html
   {% if not products %}
       <div class="flex justify-center items-center h-screen">
           <img src="{% static 'image/no-products.png' %}" alt="No products available" class="w-1/2 h-auto">
           <p class="text-xl">There are no products registered.</p>
       </div>
   {% endif %}
   ```

---

### 3. **Navigation Bar (Navbar) Implementation**

#### a. **Responsive Navbar Design**:
- I designed a **responsive navbar** using Tailwind CSS that works both on desktop and mobile devices.
- On **desktop**, the navbar displays the links horizontally, while on **mobile**, the navbar collapses into a hamburger menu for better usability.

   **Code for navbar implementation (in `navbar.html`)**:
   ```html
   <nav class="bg-indigo-600 shadow-lg fixed top-0 left-0 z-40 w-screen">
       <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
           <div class="flex items-center justify-between h-16">
               <h1 class="text-2xl font-bold text-white">Sonny Angels E-Commerce</h1>
               <div class="hidden md:flex items-center">
                   {% if user.is_authenticated %}
                       <span class="text-gray-300 mr-4">Welcome, {{ user.username }}</span>
                       <a href="{% url 'main:logout' %}" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded">
                           Logout
                       </a>
                   {% else %}
                       <a href="{% url 'main:login' %}" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">
                           Login
                       </a>
                   {% endif %}
               </div>
               <div class="md:hidden">
                   <button class="mobile-menu-button">
                       <svg class="w-6 h-6 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                           <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
                       </svg>
                   </button>
               </div>
           </div>
       </div>
       <div class="mobile-menu hidden md:hidden px-4 w-full">
           {% if user.is_authenticated %}
               <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
               <a href="{% url 'main:logout' %}" class="bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded">
                   Logout
               </a>
           {% endif %}
       </div>
   </nav>
   ```

#### b. **Mobile Hamburger Menu**:
- I added JavaScript to toggle the visibility of the navbar links on mobile when the hamburger button is clicked.

   **JavaScript for mobile menu toggle**:
   ```javascript
   const btn = document.querySelector("button.mobile-menu-button");
   const menu = document.querySelector(".mobile-menu");

   btn.addEventListener("click", () => {
       menu.classList.toggle("hidden");
   });
   ```

###

1. **Add files to staging**:
   ```bash
   git add .
   ```

2. **Commit changes**:
   ```bash
   git commit -m "Implemented CSS styling and completed product functionality"
   ```

3. **Push to GitHub**:
   ```bash
   git push origin main
   ```

---

## Fifth Assignment - AJAX and Security

### 1. Explain the benefits of using JavaScript in developing web applications!

JavaScript offers numerous benefits when developing web applications. Some of these include:

- **Client-Side Interactivity**: JavaScript allows developers to create interactive and dynamic web pages. It runs directly in the user's browser, which means that users can interact with elements on the page without needing to reload it. Features like form validation, modals, sliders, and dropdowns can all be implemented using JavaScript.
  
- **AJAX for Asynchronous Data Loading**: JavaScript enables web pages to communicate with the server asynchronously through AJAX (Asynchronous JavaScript and XML). This means that parts of a page can be updated dynamically (such as fetching new data or submitting forms) without reloading the entire page, providing a faster and more fluid user experience.

- **Improved User Experience**: By utilizing JavaScript, you can provide instant feedback to users. For instance, form validation can be done in real-time, and users can see errors or success messages without reloading the page.

- **Cross-Browser Support**: JavaScript runs on all modern browsers. With minimal setup, a developer can ensure that their website will function similarly across a wide range of devices and browsers.

- **Event Handling**: JavaScript allows developers to easily manage events (like clicks, scrolls, form submissions, etc.), making it possible to execute code in response to user actions.

- **Rich Ecosystem and Libraries**: JavaScript has a large ecosystem of libraries and frameworks (like React, Angular, and Vue.js) that streamline the process of building large-scale applications. These libraries enable rapid development and maintenance of complex web applications.

---

### 2. Explain why we need to use await when we call fetch()! What would happen if we don't use await?

In JavaScript, `fetch()` is used to make HTTP requests and returns a **promise** that resolves with the `Response` object. When calling `fetch()`, you need to use `await` to ensure the JavaScript engine waits for the promise to resolve (i.e., for the server to send the requested data) before continuing to execute the rest of the code.

#### Why we use `await`:
- **Handling asynchronous code**: When you use `await`, it pauses the execution of the function until the promise is resolved. This is important when you're expecting data from the server because you typically want to wait until the data is available before processing it.
  
- **Readable and clean code**: `await` makes your asynchronous code appear synchronous, improving readability and avoiding the need for messy `then()` and `catch()` chains.
  
#### What happens if you don't use `await`:
- **Code would execute before the response is available**: Without `await`, the code will continue to execute without waiting for the `fetch()` to resolve. This means any operation that depends on the response from `fetch()` will likely fail because the data hasn't been retrieved yet.
  
  For example:
  ```javascript
  let data = fetch("https://api.example.com/data");
  console.log(data); // Logs a Promise, not the actual data
  ```
  The above code would print a pending promise instead of the fetched data because the promise has not yet been resolved. If `await` was used, the data would be available before the console logs it.

  Correct version:
  ```javascript
  let response = await fetch("https://api.example.com/data");
  let data = await response.json();
  console.log(data); // Logs the actual data from the response
  ```

---

### 3. Why do we need to use the csrf_exempt decorator on the view used for AJAX POST?

In Django, CSRF (Cross-Site Request Forgery) protection is enabled by default for all POST requests to protect the application from unauthorized requests. However, when making AJAX POST requests, there are cases where the CSRF token might not be included correctly, which can cause Django to reject the request.

#### Why we use `csrf_exempt`:
- **Prevent CSRF validation**: The `csrf_exempt` decorator disables the CSRF validation for a specific view. This can be helpful when working with AJAX requests that might not include a CSRF token, especially when you're building an API or handling external clients that aren't designed to send CSRF tokens.
  
- **Testing and debugging purposes**: During development, using `csrf_exempt` makes it easier to test AJAX functionality without needing to worry about CSRF token configuration. However, it is not recommended for production applications unless proper measures are taken (like token-based authentication or other security mechanisms).

#### Caution:
- **Security concerns**: By using `csrf_exempt`, you are making the view vulnerable to CSRF attacks. Therefore, this decorator should be used with caution and only in trusted environments. It is better to include CSRF tokens in your AJAX requests using JavaScript and ensure that the server validates them correctly.

---

### 4. On this week's tutorial, the user input sanitization is done in the back-end as well. Why can't the sanitization be done just in the front-end?

While front-end input sanitization is important for providing a better user experience and catching basic mistakes (like empty fields or invalid formats), it **cannot be solely relied on for security**. The following reasons explain why back-end sanitization is crucial:

#### Reasons for back-end sanitization:
- **Bypass potential in the front-end**: Front-end validation and sanitization can be easily bypassed by a malicious user. Since JavaScript runs on the client-side, attackers can disable it, manipulate the data, or send raw HTTP requests directly to your server without using your front-end code at all.

- **Security against attacks like XSS and SQL injection**: If you rely solely on front-end sanitization, your application is vulnerable to attacks such as Cross-Site Scripting (XSS) and SQL injection. The server must sanitize and validate any incoming data to ensure it doesn't contain malicious code that could compromise the application.

- **Consistency and integrity of the data**: The back-end is the ultimate source of truth for data handling. By sanitizing inputs on the server, you ensure that any data stored in your database is clean, safe, and formatted correctly, regardless of how it was submitted (whether through your front-end or other external sources like APIs).

#### Example:
If a malicious user submits a form with `<script>alert('XSS')</script>` in an input field, front-end sanitization could remove or escape the `<script>` tags before sending it to the server. However, if they bypass your front-end and submit the request directly, the server would store the malicious script unless it also performs sanitization (e.g., using `strip_tags()` in Django).

Therefore, **both front-end and back-end sanitization** should be used together for optimal security.

---

### 5. **Explain how you implemented the checklist above step-by-step (not just following the tutorial)!**

#### Step 1: **Modify the previous assignment to use AJAX**

1. **Refactor Views and Templates**:
   - In my previous assignment, the product data was directly rendered in the template using Django’s context. I modified this approach by shifting product data rendering to be handled asynchronously through **AJAX**.
   - I first created a new view (`show_json`) that returns the product data in JSON format. This view is essential for making the product data available for JavaScript to fetch asynchronously.
     ```python
     def show_json(request):
         data = Product.objects.filter(user=request.user)
         return HttpResponse(serializers.serialize("json", data), content_type="application/json")
     ```

2. **Update the Template**:
   - In the `main.html` template, I removed the server-side product listing logic and replaced it with an empty table (`<tbody id="product_table_body"></tbody>`), which would be populated dynamically using AJAX.
   - I also added JavaScript functions (`getProducts()` and `refreshProductList()`) to retrieve and render the product data. The `getProducts()` function makes an AJAX GET request to the `show_json` view to retrieve product data.
     ```html
     <script>
       async function getProducts() {
           const response = await fetch("{% url 'main:show_json' %}");
           return response.json();
       }

       async function refreshProductList() {
           const productTableBody = document.getElementById("product_table_body");
           productTableBody.innerHTML = "";  // Clear existing table rows

           const products = await getProducts();
           products.forEach((item) => {
               const sanitizedName = DOMPurify.sanitize(item.fields.name);
               const sanitizedDescription = DOMPurify.sanitize(item.fields.description);
               const sanitizedRarity = DOMPurify.sanitize(item.fields.rarity);
               const sanitizedImageURL = DOMPurify.sanitize(item.fields.image_url);

               const productRow = `
                   <tr>
                       <td>${sanitizedName}</td>
                       <td>$${item.fields.price}</td>
                       <td>${sanitizedDescription} <br> <strong>Rarity:</strong> ${sanitizedRarity}</td>
                       <td>${item.fields.stock}</td>
                       <td><img src="${sanitizedImageURL}" alt="${sanitizedName}" class="w-24 h-auto object-cover rounded"></td>
                       <td>
                           <a href="/edit-product/${item.pk}" class="bg-yellow-500 text-white px-4 py-2 rounded hover:bg-yellow-600">Edit</a>
                           <a href="/delete-product/${item.pk}" onclick="return confirm('Are you sure?');" class="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600">Delete</a>
                       </td>
                   </tr>
               `;
               productTableBody.insertAdjacentHTML('beforeend', productRow);
           });
       }

       document.addEventListener('DOMContentLoaded', refreshProductList);  // Load the product list when the page is ready
     </script>
     ```

#### Step 2: **AJAX GET Implementation**

1. **AJAX GET Request for Retrieving Product Data**:
   - I wrote the `getProducts()` JavaScript function that fetches product data from the `show_json` endpoint using **fetch()**.
   - The `refreshProductList()` function then uses this data to dynamically populate the product table with the sanitized product information (such as name, description, rarity, stock, and image).

2. **Sanitizing Data with DOMPurify**:
   - To avoid potential XSS attacks, I used **DOMPurify** to sanitize the product data before displaying it on the page. This ensures that any malicious scripts injected into the product data are removed before being rendered.
   - I added the following in the `<head>` section of `main.html` to include DOMPurify:
     ```html
     <script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>
     ```

#### Step 3: **AJAX POST Implementation**

1. **Create the Modal Form for Adding Products**:
   - I added a modal that contains a form for adding new products. This modal is hidden by default and is displayed when the user clicks the "Add New Sonny Angel by AJAX" button.
   - The form inside the modal allows users to input product details such as name, price, description, rarity, stock, and image URL.

   Example modal code in `main.html`:
   ```html
   <button onclick="showModal()" class="bg-blue-500 text-white px-4 py-2 rounded">Add New Sonny Angel by AJAX</button>

   <div id="crudModal" class="hidden fixed inset-0 z-50 bg-gray-800 bg-opacity-50">
       <div id="crudModalContent" class="bg-white rounded-lg shadow-lg w-1/2 mx-auto">
           <form id="productEntryForm">
               <label for="name">Product Name</label>
               <input type="text" id="name" name="name" required>
               <!-- Other form fields here -->
               <button type="submit" id="submitProductEntry">Save</button>
           </form>
       </div>
   </div>
   ```

2. **AJAX POST for Adding New Product**:
   - I wrote an **AJAX POST** function to submit the form data to the server asynchronously. This function is triggered when the user submits the form inside the modal.
   - I created a new view (`add_product_ajax()`) in `views.py` to handle the POST request and save the product to the database.

   Example JavaScript code for handling the form submission:
   ```html
   <script>
       async function addProductAjax() {
           const csrfToken = '{{ csrf_token }}';

           const form = document.getElementById("productEntryForm");
           const formData = new FormData(form);

           const productData = {
               name: formData.get("name"),
               price: formData.get("price"),
               description: formData.get("description"),
               rarity: formData.get("rarity"),
               stock: formData.get("stock"),
               image_url: formData.get("image_url")
           };

           const response = await fetch("{% url 'main:add_product_ajax' %}", {
               method: 'POST',
               headers: {
                   'Content-Type': 'application/json',
                   'X-CSRFToken': csrfToken
               },
               body: JSON.stringify(productData)
           });

           if (response.status === 201) {
               alert("Product added successfully!");
               hideModal();
               refreshProductList();  // Refresh the product list to show the new product
           } else {
               alert("Failed to add product. Please try again.");
           }
       }

       document.getElementById("submitProductEntry").addEventListener("click", function(event) {
           event.preventDefault();
           addProductAjax();
       });
   </script>
   ```

3. **Close Modal and Clear Form Upon Success**:
   - After the product is successfully added, the modal is closed using `hideModal()`, and the form is reset to its default state using `form.reset()`.
   - The product list is refreshed using `refreshProductList()` to include the newly added product.

#### Step 4: **Create a New View to Add Product with AJAX**

1. **Create the View for Handling AJAX POST**:
   - In `views.py`, I added a view (`add_product_ajax()`) that processes the incoming product data from the POST request. I used `csrf_exempt` to disable CSRF protection for this view since it is handled by JavaScript.
   - I sanitized the incoming data using Django’s `strip_tags()` function to prevent XSS attacks from malicious input.

   Example `views.py` code:
   ```python
   @csrf_exempt
   @require_POST
   def add_product_ajax(request):
       data = json.loads(request.body)

       name = strip_tags(data.get("name"))
       price = data.get("price")
       description = strip_tags(data.get("description"))
       rarity = strip_tags(data.get("rarity"))
       stock = data.get("stock")
       image_url = strip_tags(data.get("image_url"))

       product = Product(name=name, price=price, description=description, rarity=rarity, stock=stock, image_url=image_url, user=request.user)
       product.save()

       return HttpResponse('CREATED', status=201)
   ```

#### Step 5: **Create a /create-ajax/ Path for Adding Products**

1. **URL Mapping for the AJAX POST Endpoint**:
   - I added a new path (`/create-ajax/`) in `urls.py` to map to the `add_product_ajax()` view. This path is used by the AJAX POST function to submit the product data.
   ```python
   from . import views

   urlpatterns = [
       path('create-ajax/', views.add_product_ajax, name='add_product_ajax'),
       # Other paths...
   ]
   ```

#### Step 6: **Perform Asynchronous Page Refresh (continued)**

2. **Dynamically Update the Product List**:
   - Instead of reloading the entire page, I updated the product list in real-time by calling the `refreshProductList()` function after the AJAX POST request completes successfully. This function uses the AJAX GET request to retrieve the latest product data, ensuring that the new product is included in the list without needing a full page refresh.
   - This greatly improves user experience by making the application feel more responsive and reducing server load from unnecessary page reloads.

   Example of refreshing the product list after the modal is closed:
   ```javascript
   if (response.status === 201) {
       alert("Product added successfully!");
       hideModal();  // Close the modal
       refreshProductList();  // Refresh the product list to show the new product
   }
   ```

#### Step 7: **Additional Security and UX Enhancements**

1. **CSRF Token Inclusion**:
   - Even though we used `csrf_exempt` for the AJAX POST request, this method is not recommended for production environments due to security concerns. Therefore, in a real-world scenario, you should ensure that CSRF tokens are included in your AJAX requests to protect against cross-site request forgery (CSRF) attacks.
   - In my implementation, I included the CSRF token in the AJAX POST request by adding it to the request headers:
   ```javascript
   const csrfToken = '{{ csrf_token }}';  // Fetch the CSRF token from the template context
   ```

2. **User Feedback and Error Handling**:
   - I implemented user feedback mechanisms such as displaying success or error alerts when the product is added or if the request fails. For instance, when the AJAX POST request fails (e.g., due to a server error or validation issue), I display an error message to notify the user and prompt them to try again.
   - I also made sure to handle form validation errors and notify the user if any required fields are missing.

   Example:
   ```javascript
   if (response.status !== 201) {
       alert("Failed to add product. Please try again.");
   }
   ```

3. **Form Reset and Modal Closing**:
   - Once a product is successfully added, the modal is closed, and the form inside the modal is reset to its default state. This ensures that when the user opens the modal again to add another product, the form fields are empty and ready for new input.
   - The modal closing functionality is triggered using `hideModal()` and the form reset is done using `form.reset()`:
   ```javascript
   hideModal();  // Close the modal
   form.reset();  // Clear form input fields
   ```

#### Step 8: **Deployment and Final Testing**

1. **Local Testing**:
   - Before deploying the application, I tested all the functionalities locally. This involved:
     - Testing the AJAX GET and POST requests to ensure the product data is loaded and submitted correctly.
     - Verifying that the form input is sanitized both on the front-end (using DOMPurify) and back-end (using `strip_tags()`).
     - Ensuring that the product list refreshes automatically after a new product is added.

2. **Pushing the Code to GitHub**:
   - After confirming that all functionalities work as expected, I committed the changes and pushed the code to the remote GitHub repository.

   Commands used for version control:
   ```bash
   git add .
   git commit -m "Implemented AJAX GET and POST for product management, added security features"
   git push origin main
   ```

3. **Deploying to the Server**:
   - Finally, I deployed the updated application to the production server (PWS) to make it live. This involved pushing the code to the server's Git repository and verifying that the deployed application works correctly.

---

### 6. Perform add-commit-push to GitHub

Finally, after implementing the above features, I performed the following Git commands to save the changes and push them to the remote repository:

```bash
git add .
git commit -m "assignment 6"
git push
```