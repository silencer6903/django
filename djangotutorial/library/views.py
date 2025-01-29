from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.defaultfilters import capfirst, join



menu = [
    {'name': 'Main page', 'url_page': 'home'},
    {'name': 'Authentication', 'url_page': 'aunt'},
    {'name': 'About us', 'url_page': 'about'},
    {'name': 'Exit', 'url_page': 'exit'},
    {'name': 'Library', 'url_page': 'library'},
]



def main_page(request):
    data = {
        'menu': menu,
        'title': "MAIN PAGE OF SITE!",
        'book': {
            'best_seller': [
                {'name': 'Сяйво', 'author': 'Stephen King', 'year': '01.11.1974'},
                {'name': 'Керрі', 'author': 'Stephen King', 'year': '01.11.1974'},
                {'name': 'Зелена миля', 'author': 'Stephen King', 'year': '01.11.1974'}
            ]
        }
    }
    return render(request, 'library/main_page.html', context=data)

def about(request):
    data = {
        'title': capfirst("short information about us:"),
        'menu': menu,
        'about': """This library was build in 1946`s year. And we
                    have a lot of books about WW2, so you can stud more
                    about this period of lifetime.""",
        'info': {
                 'name': "JOHN",
                 'last_name': "KIRBI",
                 'mail': 'john_kir@gmail.com',
                 'number': '+8412342133',
                 'country': {
                     'coun': "Union States of America",
                     'town': "New York",
                     'postal_code': "12343",
                     'capital': "Washington"
                 }

        }
    }
    return render(request, 'library/about.html', context=data)

def catalog(request, year):
    if 1990 < year < 2025:
        return HttpResponse(f"<h1>Archive sorted by years</h1><p>Chosen year: {year}</p>")
    url = reverse('home')
    return redirect(url)

def library(request):
    return HttpResponse(f"<h1>Libraries books: </h1><p>Chosen Book: Kerri, author: Stephen King")

def authentication(request):
    return HttpResponse(f"<h1>Enter your user data</h1>")

def exit(request):
    return HttpResponse(f"<h1>EXIT!</h1>")



def not_found(request, exception):
    return HttpResponseNotFound("<h1>PAGE NOT FOUND</h1>")


