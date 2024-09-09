from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Routing for the home page
]
