from django.conf.urls.static import static
from django.urls import path

from fallout_shelter.views import index, categories, about
from shop import settings

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:pk>/', categories, name='category'),
    path('about', about,  name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)