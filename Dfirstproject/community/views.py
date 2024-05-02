from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from community.models import Post
from django.contrib.auth.forms import AutenticationForm. UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def List(request):
    posts = Post.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'list.html', {'posts':posts})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detail.html', {'post':post})

