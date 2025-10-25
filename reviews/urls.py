from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    # API root - this might be interfering
    path('', views.api_root, name='api-root'),
    
    # JWT Authentication - THESE SHOULD COME FIRST
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # User endpoints
    path('register/', views.UserRegistrationView.as_view(), name='user-register'),
    path('user/', views.UserDetailView.as_view(), name='user-detail'),
    
    # Review endpoints
    path('reviews/', views.ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', views.ReviewDetailView.as_view(), name='review-detail'),
    path('movies/<str:movie_title>/reviews/', views.movie_reviews, name='movie-reviews'),
]