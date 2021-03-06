from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import Comment, BlogPost, Category, Tag

# User serializer, django provides a User model already, so we are going to use that model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')
        extra_kwargs = {
            'password' : {
                'write_only' : True
            }
        }
    # When we successfully created a serializer via post request, we crate a user object in the database
    # and return that user back for to use in the api.py (look at api.py line 16, when we call the save() method, 
    # it calls this create method inside of it)
    def create(self, validated_data):
        return User.objects.create_user(validated_data['username'], 
        validated_data['email'], validated_data['password'])

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__')
    
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

# BlogPost Serializer
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('__all__')
        post_image = serializers.ImageField()

    def create(self, validated_data):
        return BlogPost.objects.create(**validated_data)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('__all__')
        
    def create(self, validated_data):
        return Tag.objects.create(**validated_data)