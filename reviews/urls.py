from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    # API root
    path('', views.api_root, name='api-root'),
    
    # User endpoints
    path('register/', views.UserRegistrationView.as_view(), name='user-register'),
    path('user/', views.UserDetailView.as_view(), name='user-detail'),
    
    # Review endpoints
    path('reviews/', views.ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('movies/<str:movie_title>/reviews/', views.movie_reviews, name='movie-reviews'),
    
    # API authentication (for browsable API)
    path('auth/', include('rest_framework.urls')),
]