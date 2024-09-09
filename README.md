# E-Commerce Application - README

## Created by: Andhika Nayaka Arya Wibowo  
**Student ID:** 2306174135  
**Course:** CSGE602022 Platform-Based Programming

## Deployed Application Link
You can access the deployed application [here](http://pbp.cs.ui.ac.id/andhika.nayaka/ElectronicCommerce).

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

```plaintext
Client Request --> urls.py --> views.py --> models.py --> template (HTML) --> Response to Client
