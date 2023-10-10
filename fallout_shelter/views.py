from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from fallout_shelter.models import Product

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Контакты', 'url_name': 'contact'},
]

def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'SkystoreDM',
        'menu': menu,
    }
    return render(request, 'fallout_shelter/index.html', context=context)


def about(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'О сайте',
        'menu': menu,
    }
    return render(request, 'fallout_shelter/about.html', context=context)


def contact(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Контактная информация',
        'menu': menu,
    }
    return render(request, 'fallout_shelter/contact.html', context=context)


def page_not_found(request, exception=None):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

