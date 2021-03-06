from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from .models import Post

class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render( 
            request,
            'ccblog/home.html',
            context={
                'page_obj': page_obj
            })

class PostDetailView(View):
    def get(self, request, *arg, **kwargs):
        post = get_object_or_404(Post, url=slug)
        return render(request, 'ccblog/post_detail', context={
            'post' : post
        })