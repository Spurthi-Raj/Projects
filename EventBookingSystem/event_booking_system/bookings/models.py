from django.db import models
from django.contrib.auth.models import User

from events.models import Event


# Create your models here.


class Booking(models.Model):


    BOOKING_STATUS = (
        ('BOOKED','booked' ),
        ('CANCELLED','cancelled')
    )

    PAYMENT_STATUS =(
        ('PENDING','pending'),
        ('PAID','paid')
    )

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='bookings')
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name='bookings')
    booking_date = models.DateField()
    status = models.CharField(max_length=20,choices=BOOKING_STATUS,default='BOOKED')
    payment_status = models.CharField(max_length=20,choices=PAYMENT_STATUS,default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"


