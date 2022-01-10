from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Value

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    course = models.ForeignKey(Course,related_name='reviews',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True,default='')
    rating = models.IntegerField()