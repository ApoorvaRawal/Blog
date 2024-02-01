from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView,RetrieveDestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from .permissions import IsOwnerOrReadOnly,IsOwnerOrReadOnlyy
from rest_framework.authtoken.models import Token
from .models import Category,Post, Comment,User
from django.contrib.auth import authenticate, login,logout
from .serializers import Categoryserializers, Postserializers, Commentserializers,UserSerializer,LoginSerializer


class SignupAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.create(user=user)
        return user
from rest_framework import status

class LoginAPIView(CreateAPIView):
    queryset = Token.objects.all()
    serializer_class=LoginSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({ 'user_id': user.pk, 'username': user.username})
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        user = request.user
        if user is not None:
            return Response({'username': user.username, 'email': user.email})
        
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        logout(request)
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)        
        
class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserializers

class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = Categoryserializers


class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializers
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        

class PostDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializers
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    
class CommentListAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = Commentserializers
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = Commentserializers
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnlyy]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
