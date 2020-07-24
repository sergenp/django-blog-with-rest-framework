from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('contact/', views.contact, name="contact"),
    path('post/<int:id>', views.post, name="post")
]