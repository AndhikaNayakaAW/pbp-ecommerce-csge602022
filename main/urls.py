from django.urls import path
from main.views import index, show_main, add_product, show_xml, show_json, show_xml_by_id, show_json_by_id  # Import your views

urlpatterns = [
    path('', index, name='index'),  # Existing index view
    path('add-product/', add_product, name='add_product'),  # Route for adding a product
    path('show-main/', show_main, name='show_main'),  # Route for displaying all products
    path('xml/', show_xml, name='show_xml'),  # XML view for all products
    path('json/', show_json, name='show_json'),  # JSON view for all products
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),  # XML view for product by ID
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),  # JSON view for product by ID
]
