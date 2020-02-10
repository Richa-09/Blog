from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import post
from django.contrib import messages
import datetime

def home(request):
    return render(request,'posts/home.html')

def add(request):
    return render(request,'posts/add.html')

def create(request):
    if request.method=='POST':
        posst = post()
        posst.name = request.POST['name']
        posst.email = request.POST['email']
        posst.subject = request.POST['subject']
        posst.content = request.POST['content']
        posst.save()
        messages.success(request,"Your post has been created.")
        return render(request,'posts/add.html')
    else:
        return HttpResponse("Method not allowed")

def show(request):
    blog = post.objects.all().order_by('-id')
    return render(request,'posts/show.html',{'blog':blog})

def blog(request,k):
    posst=get_object_or_404(post,id=k)
    return render(request,'posts/blog.html',{'post':posst})

def delete(request,p):
    posst=get_object_or_404(post,id=p)
    return render(request,'posts/delete.html',{'post':posst})

def done(request,k):
    if request.method=='POST':
        posst = get_object_or_404(post,id=k)
        posst.delete()
        blog = post.objects.all().order_by('-id')
        return render(request,'posts/show.html',{'blog':blog})
    else:
        return HttpResponse("Method not allowed")



