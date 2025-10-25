# Movie Review API

A Django REST Framework API for managing movie reviews. This is an ALX Backend Capstone Project.

## Features

- User registration and authentication
- CRUD operations for movie reviews
- Review filtering by movie title and rating
- Pagination and sorting
- User permissions (users can only modify their own reviews)
- Admin interface for management

## API Endpoints

### Authentication
- `POST /api/register/` - User registration
- `GET/POST /api/auth/login/` - Login (for browsable API)
- `GET/POST /api/auth/logout/` - Logout (for browsable API)

### Users
- `GET/PUT/DELETE /api/user/` - Get, update, or delete user profile

### Reviews
- `GET/POST /api/reviews/` - List all reviews or create new review
- `GET/PUT/DELETE /api/reviews/{id}/` - Get, update, or delete specific review
- `GET /api/movies/{movie_title}/reviews/` - Get reviews for specific movie

### Query Parameters for Reviews

- `?movie_title=Inception` - Filter by exact movie title
- `?rating=5` - Filter by rating
- `?search=Inception` - Search in movie titles
- `?ordering=-created_date` - Sort by creation date (newest first)
- `?ordering=rating` - Sort by rating
- `?page=2` - Pagination

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd movie-review-api

## JWT Authentication

### Get Access Token
```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'