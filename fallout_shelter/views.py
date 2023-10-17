from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить хлам', 'url_name': 'add_trash'},
    {'title': 'Контакты', 'url_name': 'contact'},
]


class ProductHome(ListView):
    model = Product
    template_name = 'fallout_shelter/index.html'
    context_object_name = 'object_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Product.objects.filter(is_public=True)


def about(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'О сайте',
        'menu': menu,
    }
    return render(request, 'fallout_shelter/about.html', context=context)


class AddTrash(CreateView):
    form_class = AddPostForm
    template_name = 'fallout_shelter/add_trash.html'
    success_url = reverse_lazy('fallout_shelter')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление товара'
        return context


def contact(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Контактная информация',
        'menu': menu,
    }
    return render(request, 'fallout_shelter/contact.html', context=context)


class ShowPost(DetailView):
    model = Product
    template_name = 'fallout_shelter/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        context['cat_selected'] = 0
        return context



class ProductCategory(ListView):
    model = Product
    template_name = 'fallout_shelter/index.html'
    context_object_name = 'object_list'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория -' + str(context['object_list'][0].category)
        context['cat_selected'] = context['object_list'][0].category_id
        return context

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['cat_slug'], is_public=True)


def page_not_found(request, exception=None):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
