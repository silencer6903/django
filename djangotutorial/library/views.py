from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse


def main_page(request):
    data = {
        'title': "MAIN PAGE OF SITE!"
    }
    return render(request, 'library/main_page.html', context=data)

def about(request):
    data = {
        'title': "About",
        'about': """This library was build in 1946`s year. And we
                    have a lot of books about WW2, so you can stud more
                    about this period of lifetime."""
    }
    return render(request, 'library/about.html', context=data)

def catalog(request, year):
    if 1990 < year < 2025:
        return HttpResponse(f"<h1>Archive sorted by years</h1><p>Chosen year: {year}</p>")
    url = reverse('home')
    return redirect(url)

def archive(request, book, author='Unknown author'):
    return HttpResponse(f"<h1>Libraries books: </h1><p>Chosen Book: {book}, author: {author}")

def not_found(request, exception):
    return HttpResponseNotFound("<h1>PAGE NOT FOUND</h1>")


