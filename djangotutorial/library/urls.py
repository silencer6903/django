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
    path('index/', views.main_2, name='main_2'),
    path('post/', views.post, name='post'),
    path('l_catalog/<int:id_cat>/', views.l_cat, name='l_cat'),
]