from django.db import models
from datetime import datetime

class post(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
