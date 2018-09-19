from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Post
from .models import Greeting
from .forms import PostForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request,'index.html')#, {'posts': posts})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
#    post.publish() - usuniete, bo domysle ze strony nie działało
    post.published_date = timezone.now()
    post.save();
    return redirect('post_detail', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
