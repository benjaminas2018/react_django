from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .my_serializers import UserSerializer, RegisterSerializer, LoginSerializer

# Register API
class RegsiterAPI(generics.GenericAPIView):
    
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
      
    # The Token.objects.create returns a tuple (instance, token). So in order to get token use the index 1
    # "token": AuthToken.objects.create(user)[1]
    # The bestway is using 
    # `_, token = AuthToken.objects.create(user)``
        _, token = AuthToken.objects.create(user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token
        })

# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
      
    # The Token.objects.create returns a tuple (instance, token). So in order to get token use the index 1
    # "token": AuthToken.objects.create(user)[1]
    # The bestway is using 
    # `_, token = AuthToken.objects.create(user)``
        _, token = AuthToken.objects.create(user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token
        })    
# get user API
class UserAPI(generics.RetrieveAPIView):
    permissions_class = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user