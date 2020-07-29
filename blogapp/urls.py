from rest_framework import routers
from django.urls import path, include
from .api import RegisterAPI, LoginAPI, LogoutAPI, UserAPI, CommentViewSet, BlogPostViewSet, CategoriesViewSet, TagsViewSet
from knox import views as knox_views

routers = routers.DefaultRouter()
routers.register("api/comments", CommentViewSet, "comments")
routers.register("api/posts", BlogPostViewSet, "posts")
routers.register("api/categories", CategoriesViewSet, "categories")
routers.register("api/tags", TagsViewSet, "tags")

# add urls
urlpatterns = [
    path("api/auth", include("knox.urls")),
    path("api/auth/register", RegisterAPI.as_view()),
    path("api/auth/login",  LoginAPI.as_view()),
    path("api/auth/user", UserAPI.as_view()),
    path("api/auth/logout", LogoutAPI.as_view(), name = 'knox_logout')
]

urlpatterns += routers.urls