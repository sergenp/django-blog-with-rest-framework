from django.contrib.auth import login, logout

from rest_framework import permissions, generics, viewsets, status, parsers, views
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, CommentSerializer, BlogPostSerializer, CategorySerializer, TagsSerializer
from .models import BlogPost, Comment, Category, Tag
from rest_framework.authtoken.serializers import AuthTokenSerializer
import knox.views

# User API
class UserAPI(views.APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer
    # looks at the token sent, and returns the user using that token, notice this is a GET request

    def get(self, request):
        return self.request.user
    

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    # logic what happens when we "POST" to this endpoint
    def post(self, request, *args, **kwargs):
        # get the json body from the request.data
        serializer = self.get_serializer(data=request.data)
        # if the given json is invalid, i.e. it doesnt include the fields we want, raise exception
        serializer.is_valid(raise_exception=True)
        # if not save the given user
        user = serializer.save()
        return Response({
            # return a json containing the fields of UserSerializer
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            # return an authentication token from knox
            "token" : AuthToken.objects.create(user)[1]
        })

class LogoutAPI(knox.views.LogoutView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)
        return super(LogoutAPI, self).post(request, format=None)

class LoginAPI(knox.views.LoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

# Comment API
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            request.data["username"] = request.user.username
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        return Response({
            "comment" : CommentSerializer(comment, context=self.get_serializer_context()).data,
        }, status=status.HTTP_201_CREATED)

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = BlogPostSerializer
    parser_class = (parsers.FileUploadParser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            blogpost = serializer.save()
            return Response({
                "post" : BlogPostSerializer(blogpost, context=self.get_serializer_context()).data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = CategorySerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            return Response({
                "category" : CategorySerializer(category, context=self.get_serializer_context()).data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagsViewSet(viewsets.ModelViewSet):
    query_set = Tag.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = TagsSerializer 
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            tag = serializer.save()
            return Response({
                "tag" : TagsSerializer(tag, context=self.get_serializer_context()).data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
