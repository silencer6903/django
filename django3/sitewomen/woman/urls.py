
from . import views
from django.urls import path, register_converter
from . import convertors

register_converter(convertors.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.main_respon),
    path('catalog/<int:cat_id>/', views.catalog),
    path('archive/<year4:year>/', views.archive)
]



