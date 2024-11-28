from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
def home(request):
    # Posts classificados como museus
    museums = Post.objects.filter(category__name__icontains="Museu")
    # Categorias relacionadas a eventos
    event_categories = Category.objects.filter(name__icontains="Evento")
    
    return render(request, 'staticpages/home.html', {
        'museums': museums,
        'event_categories': event_categories,
    })


class Museum(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    local = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField()
    museus = models.ManyToManyField(Museum, related_name='eventos')

    def __str__(self):
        return self.nome

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name