from django.contrib import admin
from .models import BlogPost, Comment, Category, Tag

# Register your models here.
admin.site.register([BlogPost, Comment, Category, Tag])