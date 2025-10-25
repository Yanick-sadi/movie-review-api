from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Review

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'user', 'rating', 'created_date')
    list_filter = ('rating', 'created_date')
    search_fields = ('movie_title', 'user__username', 'review_content')
    readonly_fields = ('created_date', 'updated_date')
    date_hierarchy = 'created_date'