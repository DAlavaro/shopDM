from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from fallout_shelter.models import Product, Category

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Контакты', 'url_name': 'contact'},
]

def index(request):
    object_list = Product.objects.all()
    cats = Category.objects.all()

    context = {
        'object_list': object_list,
        'cats': cats,
        'title': 'Главная страница',
        'menu': menu,
        'cat_selected': 0,
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

def show_post(request, pk):
    return HttpResponse(f'Отображение товара с id = {pk}')

def show_category(request, pk):
    object_list = Product.objects.filter(category=pk)
    cats = Category.objects.all()

    if len(object_list) == 0:
        raise Http404

    context = {
        'object_list': object_list,
        'cats': cats,
        'title': 'Отображение по уровню хлама',
        'menu': menu,
        'cat_selected': pk,
    }
    return render(request, 'fallout_shelter/index.html', context=context)


def page_not_found(request, exception=None):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

