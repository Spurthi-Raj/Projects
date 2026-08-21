from django.db import models
from django.contrib.auth.models import User
from django.db.models import fields
from django.db.models.base import Model
# Create your models here.

class ToDo(models.Model):
    srno = models.AutoField(primary_key=True,auto_created=True)
    title = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)