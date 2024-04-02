from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
# Create your views here.

def home(request):
    posts=Post.objects
    return render(request, 'home.html', {'posts':posts})

def detail(request, post_id):
    post_detail=get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html',{'post': post_detail})

def new(request):
    form=PostForm()
    return render(request, 'new.html',{'form':form})

def create(request):
    form=PostForm(request.POST,request.FILES)
    if form.is_valid():
        new_post=form.save(commit=False)
        new_post.date=timezone.now()
        new_post.save()
        return redirect('detail',new_post.id)
    return redirect('home')

def delete(request, post_id):
    post_delete=get_object_or_404(Post, pk=post_id)
    post_delete.delete()
    return redirect('home')

def update_page(request,post_id):
    post_update=get_object_or_404(Post, pk=post_id)
    return render(request,'update.html',{'post':post_update})

def update(request, post_id):
    post_update = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        title = request.POST.get('title', '')  
        body = request.POST.get('body', '')  
        post_update.title = title
        post_update.body = body
        post_update.save()
        return redirect('home')
    else:
        return render(request, 'update.html', {'post': post_update})