from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(
        validators=[
            MinValueValidator(0),       # Minimum value (optional, but common for "positive" int(6))
            MaxValueValidator(999999)   # Maximum value for 6 digits
        ]
    )
    booking_date = models.DateTimeField()

    def __str__(self): 
        return self.name


# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=10, decimal_places=2)
   inventory = models.IntegerField(
        validators=[
            MinValueValidator(0),       # Minimum value (optional, but common for "positive" int(5))
            MaxValueValidator(99999)   # Maximum value for 5 digits
        ]
    ) 

   def __str__(self):
      return self.title
