from django.urls import path

from fallout_shelter.views import index, categories

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:pk>/', categories, name='category'),
]
