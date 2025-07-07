from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Booking(models.Model):
    """
    Represents a booking made by a customer at the restaurant.
    """
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(
        validators=[
            MinValueValidator(0),       # Ensures the number of guests is not negative
            MaxValueValidator(999999)   # Allows up to 6 digits for the number of guests
        ]
    )
    booking_date = models.DateTimeField()

    def __str__(self):
        """
        Returns a string representation of the booking, typically the guest's name.
        """
        return self.name

class MenuItem(models.Model):
    """
    Represents a specific item on the menu.
    """
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField() # SmallIntegerField is suitable for smaller integer values

    def __str__(self):
        """
        Returns a string representation of the menu item's title and price.
        """
        return f'{self.title} : {str(self.price)}'
