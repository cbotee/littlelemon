from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User 
from rest_framework import viewsets, generics, status
from rest_framework import permissions
from .serializers import UserSerializer, MenuItemSerializer, BookingSerializer, UserRegistrationSerializer
from .models import Booking, MenuItem
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response 
from datetime import datetime

@permission_classes([AllowAny])
def index(request):
    """
    Homepage view for the Little Lemon restaurant.
    
    This view renders the main homepage template with the current year.
    It's publicly accessible and doesn't require authentication.
    """
    context = {
        'current_year': datetime.now().year,
    }
    return render(request, 'index.html', context)

class UserRegistrationView(generics.CreateAPIView):
    """
    User registration endpoint.
    
    This view allows new users to create accounts with proper validation.
    No authentication is required to register.
    """
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        """Create a new user and return success response."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response({
            'message': 'User registered successfully',
            'user_id': user.id,
            'username': user.username,
            'email': user.email
        }, status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for managing user accounts.
    
    This ViewSet provides full CRUD operations for the Django User model,
    allowing administrators to create, read, update, and delete user accounts.
    All operations require authentication and are typically restricted to admin users.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for managing restaurant bookings.
    
    This ViewSet provides full CRUD operations for the Booking model,
    allowing users to create, read, update, and delete booking reservations.
    All operations require authentication.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

class MenuItemsView(generics.ListCreateAPIView):
    """
    A view for listing and creating menu items.
    
    This view provides GET and POST operations for menu items.
    GET returns a list of all menu items, POST creates a new menu item.
    All operations require authentication.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    """
    A view for retrieving, updating, and deleting individual menu items.
    
    This view provides GET, PUT, PATCH, and DELETE operations for a specific menu item.
    GET retrieves the item, PUT/PATCH updates it, DELETE removes it.
    All operations require authentication.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    """
    Protected message endpoint for testing authentication.
    
    This view returns a simple JSON message to verify that
    the user is properly authenticated. Used for testing
    authentication functionality.
    """
    return Response({"message":"This view is protected"})
