from django.db import models

# Create your models here.
class Messages(models.Model):
    name=models.CharField(max_length=15)
    text=models.TextField()
    def __str__(self):
        return self.name

"""
class MessagesLite(models.Model):
    age=models.IntegerField()
"""