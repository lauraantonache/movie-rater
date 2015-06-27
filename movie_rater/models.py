from django.db import models
from django.utils import timezone

class Movie(models.Model):
    owner = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    extern_link = models.CharField(max_length=500)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    

class Person(models.Model):
    user = models.ForeignKey('auth.User')
    age = models.IntegerField()
	
class MovieRating(models.Model):
    movie = models.ForeignKey('Movie')
    person = models.ForeignKey('Person')
    rate = models.IntegerField()

def publish(self):
     self.published_date = timezone.now()
     self.save()

def __str__(self):
     return self.title
     
