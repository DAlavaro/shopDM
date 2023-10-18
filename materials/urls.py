from django.conf.urls.static import static
from django.urls import path

from .views import *
from shop import settings

urlpatterns = [
    path('create/', ..., name='create'),
    path('', ..., name='list'),
    path('view/<int:pk>', ..., name='view'),
    path('edit/<int:pk>', ..., name='edit'),
    path('delete/<int:pk>', ..., name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)