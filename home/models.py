from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    number = models.CharField(max_length=12)
    pcode = models.CharField(max_length=4)
    address = models.TextField(max_length=100)
