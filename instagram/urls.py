from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutUser, name='logout'),
    path('follow/<str:pk>/', views.follow, name='follow'),
    path('unfollow/<str:pk>/', views.unfollow, name='unfollow'),
    path('like/<str:pk>/', views.like, name='like'),
    path('comment/<str:pk>/', views.comment, name='comment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)