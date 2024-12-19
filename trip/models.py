from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

User = get_user_model()
# 2 tables->  trips table and notes table

# trips table
class Trip(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2)
    start_date = models.DateField(blank = True, null = True)
    end_date = models.DateField(blank = True, null = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'trips')

    def __str__(self):
        return f'{self.city}, {self.country}'

# Notes table
class Note(models.Model):
    EXCURSIONS = (
        ("event", "Event"),
        ("diving", "Dinig"),
        ("experience", "Experience"),
        ("general", "General"),
    )
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name = 'notes')
    name = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=50, choices = EXCURSIONS)
    img = models.ImageField(upload_to='notes', blank = True, null = True)
    #pillow library is used to handle images (pip install pillow)
    rating = models.PositiveSmallIntegerField(default = 3, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.name} in {self.trip.city}...'
