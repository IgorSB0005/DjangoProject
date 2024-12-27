from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from . import forms
from django.http import HttpResponse

def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/post_list.html', {'posts' : posts})


def post_page(requests, slug):
    posts = Post.objects.get(slug=slug)
    return render(requests, 'posts/post_page.html', {'posts': posts})

@login_required(login_url="/users/login/")
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.author = request.user
            newPost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', {'form' : form})

@login_required(login_url="/users/login/")
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'posts:list'))

