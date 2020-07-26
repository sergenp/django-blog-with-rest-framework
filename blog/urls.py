import blog.settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path('', include('frontend.urls')),
    path('', include('blogapp.urls')),
    path('markdownx/', include('markdownx.urls')),
    path('admin/', admin.site.urls)
] + static(blog.settings.MEDIA_URL, document_root=blog.settings.MEDIA_ROOT)
