from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
from .forms import PostForm, CommentForm
# Create your views here.

def home(request):
    posts=Post.objects
    return render(request, 'home.html', {'posts':posts})

def detail(request, post_id):
    post_detail=get_object_or_404(Post, pk=post_id)
    post_hashtag=post_detail.hashtag.all()
    return render(request, 'detail.html',{'post': post_detail, 'hashtags':post_hashtag})

def new(request):
    form=PostForm()
    return render(request, 'new.html',{'form':form})

def create(request):
    form=PostForm(request.POST,request.FILES)
    if form.is_valid():
        new_post=form.save(commit=False)
        new_post.date=timezone.now()
        new_post.save()
        hashtags=request.POST['hashtags']
        hashtag=hashtags.split(", ")
        for tag in hashtag:
            new_hashtag=HashTag.objects.get_or_create(hashtag=tag)
            new_post.hashtag.add(new_hashtag[0])
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

def add_comment(request, post_id):
    blog= get_object_or_404(Post, pk=post_id)

    if request.method =='POST':
        form = CommentForm(request.POST)
    
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=blog
            comment.save()
            return redirect('detail', post_id)
    
    else:
        form = CommentForm()

    return render(request, 'add_comment.html', {'form':form})

