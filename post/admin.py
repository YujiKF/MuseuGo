from django.contrib import admin
from .models import Post, Comment, Category, Ticket

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_date', 'content')
    list_filter = ('created_date', 'author')

admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Ticket)
