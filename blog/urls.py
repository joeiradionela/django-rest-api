from django.urls import path
from .views import PostListCreate, PostDetail, SecureHelloView

urlpatterns = [
    path('posts/', PostListCreate.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('secure-hello/', SecureHelloView.as_view()),
]
