from django.urls import path
from .views import (
    CategoryListAPIView, CategoryDetailAPIView,
    PostListAPIView, PostDestroyAPIView, CommentDetailAPIView,CommentListAPIView,
    SignupAPIView,LoginAPIView,LogoutView,
    CurrentUserView,PostDestroyAPIView
)

urlpatterns = [
    path('signup/', SignupAPIView.as_view(), name='signup'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('who/', CurrentUserView.as_view(), name='who'),
    # Category URLs
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/<int:id>/', CategoryDetailAPIView.as_view(), name='category-detail'),


    # Post URLs
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    
    path('post/<int:pk>/', PostDestroyAPIView.as_view(), name='post-delete'),
   

    # Comment URLs
    
    path('comment/',CommentListAPIView.as_view(),name='comments'),
    path('comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
]
