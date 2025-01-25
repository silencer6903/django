from . import views
from django.urls import path, register_converter
from .convertors import FourDigitsYear

register_converter(FourDigitsYear, "year")

urlpatterns = [
    path('', views.main_page),
    path('catalog/<year:year>/', views.catalog),
]