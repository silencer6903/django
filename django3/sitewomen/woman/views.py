from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import render


def main_respon(request):
    return HttpResponse("<h1>Main Site Web Page</h1>")

def catalog(request, cat_id):
    return  HttpResponse(f"<h1>Catalog with products</h1><p>cat id: {cat_id}</p>")

def archive(request, year):
    if 1990 <= year <= 2023:
        return HttpResponse(f"<h1>Archive by the years</h1>")
    raise Http404()


def not_found(request, exception):
    return HttpResponseNotFound(f"<h1>PAGE NOT FOUND</h1>")

