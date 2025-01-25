from . import views
from django.urls import path, register_converter
from .convertors import FourDigitsYear

register_converter(FourDigitsYear, "year")

urlpatterns = [
    path('', views.main_page, name='home'),
    path('catalog/<year:year>/', views.catalog, name='year'),
    path('catalog/archive/<slug:book>/', views.archive, name='book'),
    path('catalog/archive/<slug:book>/<slug:author>/', views.archive, name='author'),
]