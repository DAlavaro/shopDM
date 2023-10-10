from django.conf.urls.static import static
from django.urls import path

from fallout_shelter.views import index, contact, about
from shop import settings

urlpatterns = [
    path('', index, name='home'),
    path('about/', about,  name='about'),
    path('contact/', contact, name='contact')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)