from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('blogapp.urls')),
    path('admin/', admin.site.urls),
]
