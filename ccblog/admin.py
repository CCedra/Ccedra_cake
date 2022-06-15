from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    paginator: type

admin.site.register(Post, PostAdmin)