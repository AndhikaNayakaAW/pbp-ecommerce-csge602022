# E-Commerce Application - README

## Created by: Andhika Nayaka Arya Wibowo  
**Student ID:** 2306174135  
**Course:** CSGE602022 Platform-Based Programming

## Deployed Application Link
You can access the deployed application [here](http://andhika-nayaka-ecommerce.pbp.cs.ui.ac.id/).

---

## 1. Implementation Checklist: Step-by-step Explanation

### Step 1: Create a New Django Project
- I created a new Django project named `ecommerce_project` using the command `django-admin startproject ecommerce_project`.

### Step 2: Create a New App
- Inside the project, I created an app called `main` using the command `python manage.py startapp main`.
  
### Step 3: Routing Configuration
- I configured the URLs by editing `urls.py` in the project directory and including the URL routing for the `main` app.
  
### Step 4: Create the Model
- I defined the `Product` model inside the `models.py` file of the `main` app. This model includes the mandatory attributes `name`, `price`, and `description`, as well as additional attributes like `rarity`, `stock`, and `image_url`.

### Step 5: Views and Templates
- I created a function `index()` in `views.py` that retrieves all products and passes them to an HTML template (`index.html`) to display the name of the application, my name, and class.

### Step 6: Add Products
- Using the Django shell, I added several products (Sonny Angels) with their respective details (name, price, description, etc.).

### Step 7: Deployment to PWS
- I initialized the repository for PWS using the provided credentials and commands. Then, I pushed the code to PWS using Git and deployed the app successfully.

---

## 2. Client Request and Server Response Diagram

Below is a diagram that shows the flow of a request from a client to a Django-based web application and the response it gives:

![<Django Request-Response Diagram>](<https://www.canva.com/design/DAGQQIdblyM/AX9JJn6pbqeSwdlVB9JEAA/edit?utm_content=DAGQQIdblyM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton>)

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
