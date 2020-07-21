from rest_framework import permissions, generics
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

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

# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    # same logic as Register, but instead of using save() method, we use the validated_data 
    # (which gets created when we call the validate method from the LoginSerializer, 
    # which, gets called whenever we post stuff to this endpoint)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user" : UserSerializer(user, context=self.get_serializer_context()).data,
            "token" : AuthToken.objects.create(user)[1]
        })

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = UserSerializer
    # looks at the token sent, and returns the user using that token, notice this is a GET request
    def get_object(self):
        return self.request.user
