from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from fallout_shelter.models import Product

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    context = {
        'object_list': Product.objects.all()[0:3],
        'title': 'SkystoreDM',
        'menu': menu,
    }
    return render(request, 'fallout_shelter/index.html', context)

def categories(request, pk):
    return HttpResponse(f'Category: {pk}')

def about(request):
    return render(request, 'fallout_shelter/about.html', {'title': 'О сайте'})

def page_not_found(request, exception=None):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')