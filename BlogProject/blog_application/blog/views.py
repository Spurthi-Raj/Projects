from django.http.response import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.

def Home(request):
    return HttpResponse('Welcome')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'registration/sigup.html',{'form':form})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request,'blog/create_post.html',{'form':form})


@login_required        
def edit_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.user != post.author:
        return redirect('post_list')
    if request.method == 'POST':
        form = PostForm(request.POST,instance = post)
        if form.is_valid():
            form.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'blog/edit_post.html',{'form':form})


@login_required
def delete_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.user != post.author:
        return redirect('post_list')
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return redirect('post_list')


@login_required
def post_list(request):
    query = request.GET.get('search','').strip()
    posts = Post.objects.filter(author = request.user).order_by('-created_at')
    if query:
        posts = posts.filter(
            Q(title__icontains = query) | Q(content__icontains = query)
            )
    paginator = Paginator(posts,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'blog/post_list.html',{'page_obj':page_obj})


@login_required
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})



