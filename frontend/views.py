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

def tag(request, id):
    tag_obj = Tag.objects.filter(pk=id).first()
    if tag_obj:
        posts = tag_obj.posts.all().extra(select=
  {'comment_count': 'SELECT count(*) FROM blogapp_comment WHERE blogapp_comment.post_id=blogapp_blogpost.id'},)
        return render(request, 'tags.html', {"posts" : posts, "tag" : tag_obj})
    else:
        return render(request, '404.html')

def post(request, id):
    post = BlogPost.objects.filter(pk=id).first()
    if post:
        comments = Comment.objects.filter(post=id)
        tags = Tag.objects.filter(posts=id)
        tag_cloud = Tag.objects.all()
        category = Category.objects.filter(pk=post.category.pk)
        return render(request, 'single.html',  {"post" : BlogPost.objects.get(pk=id), "tags" : tags, "tag_cloud":tag_cloud, 
        "category" : category, "comments" : comments})
   
    return render(request, '404.html')
