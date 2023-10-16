from django import forms
from .models import *


class AddPostForm(forms.Form):
    name = forms.CharField(max_length=255, label='Название')
    slug = forms.CharField(max_length=255, label='URL')
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': '60', 'rows': '10'}), label='Описание')
    price = forms.IntegerField(label='Цена')
    created_at = forms.BooleanField(label='Публикация', required=False, initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категории',
                                      empty_label="Категория не выбрана")
