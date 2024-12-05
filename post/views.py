from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Ticket
from .forms import PostForm, CommentForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

# Listar todos os museus
class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'  

# Detalhes de um único museus
@method_decorator(login_required(login_url='login'), name='dispatch')
class PostDetailView(PermissionRequiredMixin, DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'
    permission_required = 'post.view_post' 

# Criar um novo museus
class PostCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('post_list')
    permission_required = 'post.add_post' 

# Editar um museu existente
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post/post_edit.html'
    success_url = reverse_lazy('post_list')

# Excluir um museu
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')  

@login_required(login_url='login')
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

# Listagem de todos eventos
class CategoryListView(ListView):
    model = Category
    template_name = 'post/category_list.html'
    context_object_name = 'categories'

# Detalhes de um evento
class CategoryDetailView(DetailView):
    model = Category
    template_name = 'post/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object.posts.all()  
        return context

    def post_list(request):
        museums = Post.objects.all()  
        return render(request, 'post_list.html', {'posts': museums})

def home(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado com sucesso! Faça login para continuar.")
            return redirect('login')
    posts = Post.objects.all()
    context = {
        'form': form,
        'posts': posts,
    }
    return render(request, 'staticpages/home.html', context)

@login_required(login_url='login')
def ticket_list(request):
    tickets = Ticket.objects.filter(available_quantity__gt=0)
    return render(request, 'ticket/ticket_list.html', {'tickets': tickets})

@login_required(login_url='login')
def add_to_cart(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    cart = request.session.get('cart', {})
    if str(ticket_id) in cart:
        cart[str(ticket_id)] += 1
    else:
        cart[str(ticket_id)] = 1
    request.session['cart'] = cart
    return redirect('ticket_list')

@login_required(login_url='login')
def remove_to_cart(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    cart = request.session.get('cart', {})
    if str(ticket_id) in cart:
        cart[str(ticket_id)] -= 1
    else:
        cart[str(ticket_id)] = 1
    request.session['cart'] = cart
    return redirect('ticket_list')

@login_required(login_url='login')
def cart_view(request):
    cart = request.session.get('cart', {})
    tickets = Ticket.objects.filter(id__in=cart.keys())
    cart_items = [
        {
            'ticket': ticket,
            'quantity': cart[str(ticket.id)],
            'total': ticket.price * cart[str(ticket.id)],
        }
        for ticket in tickets
    ]
    total_price = sum(item['total'] for item in cart_items)
    return render(request, 'ticket/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def register(request):
    if request.method == 'POST':
        print("Dados recebidos no POST:", request.POST)  
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso! Faça login para continuar.")
            return redirect('login')
        else:
            print("Erros no formulário:", form.errors) 
            messages.error(request, "Erro ao criar a conta. Verifique os dados.")
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
