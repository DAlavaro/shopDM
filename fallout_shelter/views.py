from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return render(request, 'fallout_shelter/index.html')

def categories(request, pk):
    return HttpResponse(f'Category: {pk}')

def page_not_found(request, exception=None):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')