from django.db import models

# Create your models here.
class EmailEntry(models.Model):
  bio = models.TextField(blank=True)
  consent = models.BooleanField(default=False)
  email = models.EmailField()
  name = models.CharField(max_length=120, 
  blank=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

