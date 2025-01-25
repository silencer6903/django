from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse


def main_page(request):
    return HttpResponse("<h1>Main page</h1>")

def catalog(request, year):
    if 1990 < year < 2025:
        return HttpResponse(f"<h1>Archive sorted by years</h1><p>Chosen year: {year}</p>")
    url = reverse('home')
    return redirect(url)

def archive(request, book, author='Unknown author'):
    return HttpResponse(f"<h1>Libraries books: </h1><p>Chosen Book: {book}, author: {author}")

def not_found(request, exception):
    return HttpResponseNotFound("<h1>PAGE NOT FOUND</h1>")


