from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.defaultfilters import yesno


def main_page(request):
    return HttpResponse("<h1>Main page</h1>")

def catalog(request, year):
    if 1990 < year < 2025:
        return HttpResponse(f"<h1>Archive sorted by years</h1><p>Chosen year: {year}</p>")
    raise Http404()


def not_found(request, exception):
    return HttpResponseNotFound("<h1>PAGE NOT FOUND</h1>")