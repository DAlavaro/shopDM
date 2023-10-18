from django.conf.urls.static import static
from django.urls import path

from .views import *
from shop import settings

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('about/', about,  name='about'),
    path('contact/', contact, name='contact'),
    path('addtrash/', AddTrash.as_view(), name='add_trash'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ProductCategory.as_view(), name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)