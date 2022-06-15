from django.shortcuts import render
from django.views import View
from .models import Post

class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objrcts.all()
        return render(
            request,
            'ccblog/home.html',
            context={
                'posts': posts
            }
        )