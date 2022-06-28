from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def simple_view(request):
    return HttpResponse(' you are welcome!')

def design(request):
    x={
        'tobi':1,
        'ope':2
    }
    return render(request,'other/index.html',context=x)
def login_view(request):
    x={
        'tobi':1,
        'ope':2
    }
    return render(request,'other/login.html',context=x)
def signup(request):
    x={
        'tobi':1,
        'ope':2
    }
    return render(request,'other/signup.html',context=x)

def homeview(request):
    x={
        'tobi':1,
        'ope':2
    }
    return render(request,'other/home.html',context=x)

