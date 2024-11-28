from django.shortcuts import render

from django.shortcuts import render
from .models import Museum, Category

def home(request):
    # Recuperar dados necessários para a página inicial
    museums = Museum.objects.all()[:3]  # Limita a exibição de 3 museus (ou ajuste conforme necessário)
    event_categories = Category.objects.all()  # Categorias associadas aos eventos
    context = {
        'museums': museums,
        'event_categories': event_categories,
    }
    return render(request, 'staticpages/home.html', context)


def about(request):
    return render(request, 'staticpages/about.html')