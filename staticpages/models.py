from django.db import models
from django.utils.timezone import now
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

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField()
    museus = models.ManyToManyField(Post, related_name='eventos')

    def __str__(self):
        return self.nome

