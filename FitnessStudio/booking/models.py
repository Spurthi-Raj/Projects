from django.db import models
from django.utils import timezone

# Create your models here.

class Fitness(models.Model):
    name = models.CharField(max_length=50)
    instructor = models.CharField(max_length = 50)
    start_date = models.DateTimeField()
    available_slot = models.PositiveIntegerField()

class Booking(models.Model):
    fitness_class = models.ForeignKey(Fitness,on_delete=models.CASCADE)
    client_name = models.CharField(max_length=50)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(default = timezone.now)