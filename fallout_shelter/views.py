from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить хлам', 'url_name': 'add_trash'},
    {'title': 'Контакты', 'url_name': 'contact'},
]


def index(request):
    object_list = Product.objects.all()

    context = {
        'object_list': object_list,
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


def add_trash(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            try:
                Product.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()
    context = {
        'form': form,
        'title': 'Добавить хлам',
        'menu': menu,
    }
    return render(request, 'fallout_shelter/add_trash.html', context=context)


def contact(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Контактная информация',
        'menu': menu,
    }
    return render(request, 'fallout_shelter/contact.html', context=context)


def show_post(request, slug):
    post = get_object_or_404(Product, slug=slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.name,
        'cat_selected': post.category,
    }

    return render(request, 'fallout_shelter/post.html', context=context)


def show_category(request, pk):
    object_list = Product.objects.filter(category=pk)

    if len(object_list) == 0:
        raise Http404

    context = {
        'object_list': object_list,
        'title': 'Отображение по уровню хлама',
        'menu': menu,
        'cat_selected': pk,
    }
    return render(request, 'fallout_shelter/index.html', context=context)


def page_not_found(request, exception=None):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
