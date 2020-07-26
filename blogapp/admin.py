from django.contrib import admin
from .models import BlogPost, Comment, Category, Tag
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
admin.site.register([Comment, Category, Tag])
admin.site.register(BlogPost, MarkdownxModelAdmin)