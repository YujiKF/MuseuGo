from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Ticket(models.Model):
    event_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.PositiveIntegerField(default=0)
    museums = models.ManyToManyField('Post', related_name='tickets') 

    def __str__(self):
        return self.event_name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(default=now)
    categories = models.ManyToManyField(Category, related_name='posts')
    location = models.TextField()
    image_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()  
    created_date = models.DateTimeField(default=now)