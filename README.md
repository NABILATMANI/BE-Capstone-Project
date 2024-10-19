# Movie Review API

This project is a Movie Review API built using Django and Django REST Framework. The API allows users to **create, read, update, delete, and view movie reviews**. User authentication is implemented to ensure that only authorized users can modify their reviews. The API is designed to be deployed on **PythonAnywhere** for live testing.

## Table of Contents
- [Project Overview](#project-overview)
- [API Endpoints](#api-endpoints)
- [Setup and Installation](#setup-and-installation)
- [Authentication Steps](#authentication-steps)
- [How to Use the API](#how-to-use-the-api)
- [API Documentation](#api-documentation)
- [Deployment on PythonAnywhere](#deployment-on-pythonanywhere)
- [Conclusion](#conclusion)
- [Contact](#contact)

## Project Overview
This API provides functionality to manage movie reviews:
- **CRUD operations** for reviews (Create, Read, Update, Delete).
- **JWT-based authentication** ensures only logged-in users can modify their own reviews.
- **Search, filtering, and pagination** to manage large datasets.
- **Deployed on PythonAnywhere** for live access and testing.

## API Endpoints
### Authentication
- **POST** `/api/token/` - Get access and refresh tokens.
- **POST** `/api/token/refresh/` - Refresh the access token.

### Movie Reviews
- **GET** `/api/reviews/` - List all movie reviews.
- **POST** `/api/reviews/` - Create a new review (requires authentication).
- **GET** `/api/reviews/{id}/` - Get a specific review by ID.
- **PUT** `/api/reviews/{id}/` - Update a review (only by the review owner).
- **DELETE** `/api/reviews/{id}/` - Delete a review (only by the review owner).

### API Documentation
- **Swagger UI**: `/swagger/`
- **ReDoc UI**: `/redoc/`

## Setup and Installation
### Prerequisites
- Python 3.x
- Virtual environment (recommended)
- Git (optional for version control)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd movie-review-api
