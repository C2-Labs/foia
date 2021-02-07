from django.db import models

# Create your models here.
class Agency(models.Model):
    title = models.CharField(max_length=512)

class RequestType(models.Model):
    title = models.CharField(max_length=512)

