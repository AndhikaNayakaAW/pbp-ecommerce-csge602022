from django.urls import path
from main.views import show_main, add_product, show_xml, show_json, show_xml_by_id, show_json_by_id, index
from .views import edit_product

urlpatterns = [
    path('', show_main, name='show_main'),  # Make show_main the root URL
    path('add-product/', add_product, name='add_product'),  # Route for adding a product
    path('xml/', show_xml, name='show_xml'),  # XML view for all products
    path('json/', show_json, name='show_json'),  # JSON view for all products
    path('xml/<uuid:id>/', show_xml_by_id, name='show_xml_by_id'),  # XML view for product by UUID
    path('json/<uuid:id>/', show_json_by_id, name='show_json_by_id'),  # JSON view for product by UUID
    path('index/', index, name='index'),  # Keep the index view at /index/
    path('edit-product/<uuid:product_id>/', edit_product, name='edit_product'),  # Change from int to uuid
]
