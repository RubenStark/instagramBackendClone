from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile, Post, Comment
# Create your views here.

def home(request):

    if request.user.is_authenticated:
        profile = request.user.profile
        posts = profile.post_set.all()
        followers = profile.followers.all()
    else:
        profile = None
        posts = None
        followers = None
    
    context = {'profile': profile, 'posts': posts, 'followers': followers}
    return render(request, 'instagram/home.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, 'instagram/login.html')

def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'instagram/signup.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def follow(request, pk):

    profile = Profile.objects.get(id = pk)
    profile.followers.add(request.user)
    profile.save()
    request.user.profile.following.add(profile.user)
    request.user.profile.save()

    return redirect('home')

def unfollow(request, pk):

    profile = Profile.objects.get(id = pk)
    profile.followers.remove(request.user)
    profile.save()
    request.user.profile.following.remove(profile.user)
    request.user.profile.save()

    return redirect('home')

def like(request, pk):

    post = Post.objects.get(id = pk)
    post.likes.add(request.user)
    post.save()

    return redirect('home')

def comment(request, pk):
    post = Post.objects.get(id = pk)
    
    if request.method == 'POST':
        comment = request.POST.get('comment')
        Comment.objects.create(user=request.user, post=post, body=comment)

    return redirect('home')