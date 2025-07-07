from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Booking, MenuItem


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Handles user creation with password validation and confirmation.
    """
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})
    password_confirm = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm', 'first_name', 'last_name']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'first_name': {'required': False},
            'last_name': {'required': False},
        }
    
    def validate(self, attrs):
        """Validate that passwords match and email is unique."""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords don't match.")
        
        # Check if email is already in use
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        
        # Check if username is already in use
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError("A user with this username already exists.")
        
        return attrs
    
    def create(self, validated_data):
        """Create a new user with hashed password."""
        validated_data.pop('password_confirm') 
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the Django User model.
    It exposes the user's URL, username, email, and groups.
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MenuItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the MenuItem model.
    It exposes the item's ID, title, price, and inventory.
    """
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']

class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    It converts Booking model instances into JSON format and vice-versa.
    """
    class Meta:
        model = Booking
        fields = ['id', 'name', 'no_of_guests', 'booking_date']
        read_only_fields = ['id'] 
