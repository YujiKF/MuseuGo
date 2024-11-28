from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, CommentForm
from .models import Museum

# Listar todos os posts
class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'  

# Detalhes de um único post
class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'  

# Criar um novo post
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('post_list')  

# Editar um post existente
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_edit.html'
    success_url = reverse_lazy('post_list')

# Excluir um post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')  

@login_required
def add_comment(request, pk): 
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.id)
    else:
        form = CommentForm()
    return render(request, 'post/add_comment.html', {'form': form, 'post': post})

# Listagem de todas as categorias
class CategoryListView(ListView):
    model = Category
    template_name = 'post/category_list.html'
    context_object_name = 'categories'

# Detalhes de uma categoria com posts
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'post/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.all()  # Recupera todos os posts da categoria
        return context

    def museum_list(request):
        museums = Museum.objects.all()  # Recupera todos os museus
        return render(request, 'museum_list.html', {'museums': museums})

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
