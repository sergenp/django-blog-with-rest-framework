from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=50)

    @classmethod
    def get_default_pk(cls):
        category, created = cls.objects.get_or_create(id=1,
            title='No Category', defaults=dict(id=1, title='No category'))
        return category.pk

class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, null=False, default=Category.get_default_pk)
    post_image = models.ImageField(blank=False, null=False, default="default_post.jpg", upload_to="post_images")

class Comment(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(default=timezone.now)

class Tag(models.Model):
    title = models.CharField(max_length=50)
    blog_posts = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True)
