# Create your models here.
from django.db import models

class Books(models.Model):
  book_title = models.CharField(max_length=255)
  book_publisher = models.CharField(max_length=255)