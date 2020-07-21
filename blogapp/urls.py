from rest_framework import routers
from django.urls import path, include
from .api import RegisterAPI, LoginAPI, UserAPI, CommentViewSet, BlogPostViewSet
from knox import views as knox_views

routers = routers.DefaultRouter()
routers.register("api/comments", CommentViewSet, "comments")
routers.register("api/posts", BlogPostViewSet, "posts")


# add urls
urlpatterns = [
    path("api/auth", include("knox.urls")),
    path("api/auth/register", RegisterAPI.as_view()),
    path("api/auth/login", LoginAPI.as_view()),
    path("api/auth/user", UserAPI.as_view()),
    path("api/auth/logout", knox_views.LogoutView.as_view(), name = 'knox_logout')
]

urlpatterns += routers.urls