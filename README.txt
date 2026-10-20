# Little Lemon — Capstone Project

## Project overview
Django REST Framework API for menu items and table bookings. Includes user registration, token authentication, MySQL configuration, and an HTML welcome page.

## Welcome page
- GET /restaurant/

## Menu API
- GET /restaurant/menu/items
- POST /restaurant/menu/items
- GET /restaurant/menu/items/<id>
- PUT /restaurant/menu/items/<id>
- PATCH /restaurant/menu/items/<id>
- DELETE /restaurant/menu/items/<id>

## Table booking API
- GET /restaurant/booking/tables/
- POST /restaurant/booking/tables/
- GET /restaurant/booking/tables/<id>/
- PUT /restaurant/booking/tables/<id>/
- PATCH /restaurant/booking/tables/<id>/
- DELETE /restaurant/booking/tables/<id>/

Booking endpoints require authentication.

## User registration and authentication
- POST /auth/users/ — Register a user.
- GET /auth/users/me/ — Get the authenticated user's profile.
- POST /auth/token/login/ — Obtain an authentication token.
- POST /auth/token/logout/ — Delete the current token.

For authenticated requests, use this HTTP header:
Authorization: Token <your_token>

## Alternative token endpoint
- POST /restaurant/api-token-auth/

## Automated tests
Run from the directory containing manage.py:
python manage.py test

## API testing
Use Insomnia to test the endpoints.
