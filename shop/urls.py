from django.contrib import admin
from django.urls import path, include


from fallout_shelter.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fallout_shelter.urls')),
]

handler404 = page_not_found