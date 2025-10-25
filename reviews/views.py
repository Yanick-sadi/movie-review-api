from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.db.models import Q
from .models import User, Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import UserRegistrationSerializer, UserSerializer, ReviewSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'register': reverse('user-register', request=request, format=format),
        'user-profile': reverse('user-detail', request=request, format=format),
        'reviews': reverse('review-list-create', request=request, format=format),
        'movie-reviews': 'api/movies/{movie_title}/reviews/',
    })
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

# User Views
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user

# Review Views
class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['rating']
    search_fields = ['movie_title']
    ordering_fields = ['rating', 'created_date', 'updated_date']
    ordering = ['-created_date']
    
    def get_queryset(self):
        queryset = Review.objects.all()
        movie_title = self.request.query_params.get('movie_title', None)
        if movie_title:
            queryset = queryset.filter(movie_title__iexact=movie_title)
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# Custom endpoint for movie reviews
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def movie_reviews(request, movie_title):
    try:
        reviews = Review.objects.filter(movie_title__iexact=movie_title)
        paginator = PageNumberPagination()
        paginated_reviews = paginator.paginate_queryset(reviews, request)
        serializer = ReviewSerializer(paginated_reviews, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)