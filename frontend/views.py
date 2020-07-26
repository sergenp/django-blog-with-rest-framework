from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from blogapp.models import BlogPost, Comment, Tag, Category


def index(request):
    posts = BlogPost.objects.all().extra(select=
  {'comment_count': 'SELECT count(*) FROM blogapp_comment WHERE blogapp_comment.post_id=blogapp_blogpost.id'},)
    return render(request, 'index.html', {"posts" : posts})

def about(request):
     return render(request, 'about.html', {'title': 'About'})
    
def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def post(request, id):
    post = BlogPost.objects.filter(pk=id).first()
    tags = Tag.objects.all()
    category = Category.objects.filter(pk=post.category.pk)
    if post:
        return render(request, 'single.html',  {"post" : BlogPost.objects.get(pk=id), "tags" : tags, "category" : category})
    return render(request, '404.html')
