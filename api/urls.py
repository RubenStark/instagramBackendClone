from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.getRoutes),
    path('posts/', views.getPosts),
    path('like/<str:pk>', views.like),
    path('comments/<str:pk>', views.getComments),
    path('get-user-profile/', views.getUserProfile),
    path('get-stories/', views.getStories),
    path('get-storie/<str:pk>', views.getStorie),
    path('create-post/', views.createPost),
    path('get-posts/', views.getUserPosts),
    path('get-notifications/', views.getNotifications),
    path('comment/', views.createComment),
]
