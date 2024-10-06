from django.urls import path
from main.views import (
    show_main, 
    add_product, 
    show_xml, 
    show_json, 
    show_xml_by_id, 
    show_json_by_id, 
    index, 
    register, 
    login_user, 
    logout_user, 
    edit_product,
    delete_product,
    product_list,  # Add this to import the view
    add_product_ajax  # Import the add_product_ajax view
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add-product/', add_product, name='add_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),
    path('index/', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:product_id>', edit_product, name='edit_product'),
    path('delete-product/<uuid:product_id>', delete_product, name='delete_product'),
    path('product-list/', product_list, name='product_list'),  # Added route
    path('create-product-entry-ajax/', add_product_ajax, name='add_product_ajax'),  # Added AJAX route for product creation
]
