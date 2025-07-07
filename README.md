# Little Lemon Restaurant API

A Django REST Framework-based API for the Little Lemon restaurant, providing endpoints for menu management, booking reservations, and user management.

## About

Little Lemon is a family-owned Mediterranean restaurant based in Chicago, Illinois, focused on traditional recipes served with a modern twist. This API provides a complete backend solution for managing the restaurant's digital operations.

## Features

- **Menu Management**: CRUD operations for menu items
- **Booking System**: Restaurant table reservations
- **User Management**: User authentication and authorization
- **RESTful API**: Well-structured REST endpoints
- **Token Authentication**: Secure API access
- **Admin Interface**: Django admin for data management
- **Frontend Integration**: Interactive booking form and menu display
- **User Registration**: Public registration endpoint

## Architecture

### Models
- **MenuItem**: Restaurant menu items with title, price, and inventory
- **Booking**: Customer reservations with guest count and booking date
- **User**: Django's built-in user model for authentication

### API Endpoints
- **Menu Items**: `/menu/` and `/menu/{id}/`
- **Bookings**: `/api/bookings/` and `/api/bookings/{id}/`
- **Users**: `/api/users/` and `/api/users/{id}/`
- **Authentication**: `/api-token-auth/`

## Quick Start

### Prerequisites
- Python 3.9+
- pip
- virtual environment

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd littlelemon
   ```

2. **Activate virtual environment**
   ```bash
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://localhost:8000/`

## API Documentation

### Authentication
All API endpoints require authentication using token-based authentication, except for registration.

**Get Token:**
```bash
POST /api-token-auth/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

### User Registration

#### Register New User
```bash
POST /api/registration/
Content-Type: application/json

{
    "username": "newuser",
    "email": "user@example.com",
    "password": "securepassword123",
    "password_confirm": "securepassword123",
    "first_name": "John",
    "last_name": "Doe"
}
```

**Response:**
```json
{
    "message": "User registered successfully",
    "user_id": 1,
    "username": "newuser",
    "email": "user@example.com"
}
```

**Validation Rules:**
- Username must be unique
- Email must be unique
- Password must be at least 8 characters
- Password and password_confirm must match
- First name and last name are optional

### Menu Items

#### List Menu Items
```bash
GET /menu/
Authorization: Token your_token_here
```

#### Create Menu Item
```bash
POST /menu/
Authorization: Token your_token_here
Content-Type: application/json

{
    "title": "Italian Pizza",
    "price": "12.99",
    "inventory": 50
}
```

#### Get Single Menu Item
```bash
GET /menu/{id}/
Authorization: Token your_token_here
```

#### Update Menu Item
```bash
PUT /menu/{id}/
Authorization: Token your_token_here
Content-Type: application/json

{
    "title": "Updated Italian Pizza",
    "price": "13.99",
    "inventory": 45
}
```

#### Delete Menu Item
```bash
DELETE /menu/{id}/
Authorization: Token your_token_here
```

### Bookings

#### List Bookings
```bash
GET /api/bookings/
Authorization: Token your_token_here
```

#### Create Booking
```bash
POST /api/bookings/
Authorization: Token your_token_here
Content-Type: application/json

{
    "name": "John Doe",
    "no_of_guests": 4,
    "booking_date": "2024-01-15T19:00:00Z"
}
```

#### Get Single Booking
```bash
GET /api/bookings/{id}/
Authorization: Token your_token_here
```

#### Update Booking
```bash
PUT /api/bookings/{id}/
Authorization: Token your_token_here
Content-Type: application/json

{
    "name": "John Doe",
    "no_of_guests": 6,
    "booking_date": "2024-01-15T20:00:00Z"
}
```

#### Delete Booking
```bash
DELETE /api/bookings/{id}/
Authorization: Token your_token_here
```

### Users

#### List Users
```bash
GET /api/users/
Authorization: Token your_token_here
```

#### Create User
```bash
POST /api/users/
Authorization: Token your_token_here
Content-Type: application/json

{
    "username": "newuser",
    "email": "user@example.com",
    "password": "securepassword"
}
```

#### Get Single User
```bash
GET /api/users/{id}/
Authorization: Token your_token_here
```

#### Update User
```bash
PUT /api/users/{id}/
Authorization: Token your_token_here
Content-Type: application/json

{
    "username": "updateduser",
    "email": "updated@example.com"
}
```

#### Delete User
```bash
DELETE /api/users/{id}/
Authorization: Token your_token_here
```

## Testing

Run the test suite:
```bash
python manage.py test tests/ -v 2
```

Current test coverage includes:
- Menu item model tests
- Menu item view tests

## Development

### Project Structure
```
littlelemon/
├── littlelemon/          # Main project settings
├── restaurant/           # Main application
│   ├── models.py        # Data models
│   ├── views.py         # API views
│   ├── serializers.py   # Data serialization
│   ├── urls.py          # URL routing
│   ├── admin.py         # Admin interface
│   └── templates/       # HTML templates
├── tests/               # Test files
├── manage.py            # Django management script
└── README.md           # This file
```


### Database
The project uses MySQL by default.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
