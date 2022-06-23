from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.views import View
from .forms import SignUpForm
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
    def get(self, request, slug, *arg, **kwargs):
        post = get_object_or_404(Post, url=slug)
        return render(request, 'ccblog/post_detail.html', context={
            'post' : post
        })


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'ccblog/signup.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'ccblog/signup.html', context={
            'form': form,
        })