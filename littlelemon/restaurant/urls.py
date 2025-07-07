from django.contrib import admin 
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from . import views

# Create a router and register our viewsets with it
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'bookings', views.BookingViewSet)
  
urlpatterns = [ 
    path('', views.index, name='index'),

    # API endpoints using router
    path('api/', include(router.urls)),
    
    # Registration endpoint
    path('api/registration/', views.UserRegistrationView.as_view(), name='user-register'),
    
    # menu endpoints
    path('menu/', views.MenuItemsView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),

    # message
    path('message/', views.msg, name='message'),

    # token
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
