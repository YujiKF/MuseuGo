from django.urls import path
from .views import ticket_list, add_to_cart, cart_view
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    add_comment,
    CategoryListView, 
    CategoryDetailView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/add_comment/', add_comment, name='add_comment'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('tickets/', ticket_list, name='ticket_list'),
    path('tickets/add_to_cart/<int:ticket_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_view, name='cart_view'),
]
