from django.db import models
# Create your models here.


class User_query(models.Model):
    name = models.CharField(max_length=200)
    query = models.CharField(max_length=500)
    dateTime = models.DateTimeField(auto_now_add=True)