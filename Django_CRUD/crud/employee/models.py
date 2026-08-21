from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = EmailField()
    econtact = models.CharField(max_length=15)

    def __str__(self) :
        return str(self.ename)

    class Meta:
        db_table = "employee"
