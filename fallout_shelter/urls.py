from django.conf.urls.static import static
from django.urls import path

from .views import *
from shop import settings

urlpatterns = [
    path('', index, name='home'),
    path('about/', about,  name='about'),
    path('contact/', contact, name='contact'),
    path('addtrash/', add_trash, name='add_trash'),
    path('post/<slug:slug>/', show_post, name='post'),
    path('category/<int:pk>/', show_category, name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)