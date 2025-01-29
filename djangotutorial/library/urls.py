from . import views
from django.urls import path, register_converter
from .convertors import FourDigitsYear

register_converter(FourDigitsYear, "year")

urlpatterns = [
    path('', views.main_page, name='home'),
    path('catalog/<year:year>/', views.catalog, name='year'),
    path('library/', views.library, name='library'),
    path('about/', views.about, name='about'),
    path('authentication/', views.authentication, name='aunt'),
    path('exit/', views.exit, name='exit'),
]