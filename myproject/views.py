# from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello,World I am HOME.")
    return render(request,"home.html")
def about(request):
    # return HttpResponse("About Page")
    return render(request,"about.html")
def profile(request):
    return render(request,"profile.html")