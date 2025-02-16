from django.shortcuts import render
from .models import Posts
# Create your views here.
def posts_list(request):
    posts=Posts.objects.all().order_by('-date')
    return render(request,'posts/posts_list.html',{'posts':posts})
def posts_page(request,slug):
    posts=Posts.objects.get(slug=slug)
    return render(request,'posts/post_page.html',{'posts':posts})