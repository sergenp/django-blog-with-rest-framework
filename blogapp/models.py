from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)

    @classmethod
    def get_default_pk(cls):
        obj = None
        try:
            obj = Category.objects.get(title="No Category")
        except cls.DoesNotExist:
            obj = Category(title="No Category")
            obj.save()
        return obj.pk

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    content = MarkdownxField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=False, default=Category.get_default_pk)
    post_image = models.ImageField(blank=False, null=False, default="default_post.jpg", upload_to="post_images")

    def __str__(self):
        return self.title
    
    def formatted_markdown(self):
        return markdownify(self.content)

class Comment(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(default=timezone.now)

class Tag(models.Model):
    title = models.CharField(max_length=50)
    blog_posts = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True)
