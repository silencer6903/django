from tkinter.font import names

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.defaultfilters import capfirst, join



menu = [
    {'name': 'Main page', 'url_page': 'home'},
    {'name': 'About us', 'url_page': 'about'},
    {'name': 'Library', 'url_page': 'library'},
    {'name': 'Authentication', 'url_page': 'aunt'},
    {'name': 'Exit', 'url_page': 'exit'},
]

data = {
    'posts': [
        {'title': '1984',
         'content': """Plot Summary. George Orwell wrote 1984 in 1949. 
                        The dystopian novel is set in 1984 - Orwells near 
                        future and our recent past - but the novel is still 
                        relevant today, due to its depiction of a totalitarian 
                        government and its themes of using media manipulation and 
                        advanced technology to control people.""",
         'is_published': True,
         'id': 1},
        {'title': 'I will find you',
         'content': """David and Cheryl Burroughs are living the dream - married, 
                        a beautiful house in the suburbs, a three-year-old son named 
                        Matthew - when tragedy strikes one night in the worst possible 
                        way.""",
         'is_published': True,
         'id': 2},
        {'title': 'The Courage To Be Disliked',
         'content': """Millions have already benefited from the wisdom dispensed 
                        in The Courage to Be Disliked, its simple yet profound advice 
                        showing us how to harness our inner power to become the person we 
                        would like to be.""",
         'is_published': True,
         'id': 3}
    ]
}






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
        },
        'cat_id': 0,
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

def main_2(request):
    return render(request, 'library/index.html', {'data':data, post:'asd'})

def post(request):
    return HttpResponse("Post")


def not_found(request, exception):
    return HttpResponseNotFound("<h1>PAGE NOT FOUND</h1>")



cats = [
        {'title': 'Book', 'id': 1},
        {'title': 'Comics', 'id': 2},
        {'title': 'Magazine', 'id': 3},
    ]

def l_cat(request, id_cat):
    data = {
        'menu': menu,
        'title_c': "Catalog!",
        'book': {
            'best_seller': [
                {'name': 'Сяйво', 'author': 'Stephen King', 'year': '01.11.1974'},
                {'name': 'Керрі', 'author': 'Stephen King', 'year': '01.11.1974'},
                {'name': 'Зелена миля', 'author': 'Stephen King', 'year': '01.11.1974'}
            ]
        },
        'cat_id': id_cat,
    }
    return render(request, 'library/main_page.html', context=data)






































