from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def index(request):
    a=[]
    for i in range(65,91):
        a.append(chr(i))
    return render(request,"index.html",{"alpha":a})

def movies(request):
    m=request.GET.get("mname")
    a=[]
    for fname in os.listdir("D:/django/myweb/myweb/static/mysongs"):
        if fname.startswith(m):
            a.append(fname)
    return render(request,"movies.html",{"movies":a})
def songs(request):
    m=request.GET.get("mname")
    a=[]
    for i in os.listdir("D:/django/myweb/myweb/static/mysongs/"+m):
        a.append(i)
    
    return render(request,"songs.html",{"songs":a,"mname":m})


def play(request):
    mname=request.GET.get("mname")
    sname=request.GET.get("sname")
    return render(request,"play.html",{"mname":mname,"sname":sname})

