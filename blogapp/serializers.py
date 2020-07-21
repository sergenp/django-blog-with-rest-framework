from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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
        user = User.objects.create_user(validated_data['username'], 
        validated_data['email'], validated_data['password'])
        return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        # authenticate method explained here https://docs.djangoproject.com/en/3.0/topics/auth/default/#authenticating-users
        user = authenticate(**data)
        # if the given username and password matches a user, return that user
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


