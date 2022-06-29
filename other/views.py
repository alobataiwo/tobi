from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import Modal
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

def thankyou(request):
    x={
        'tobi':1,
        'ope':2
    }
    return render(request,'other/thankyou.html',context=x)

def homeview(request):
   if request.method == 'POST':
      form = Modal(request.POST)
      if form.is_valid():
        form.save()
        return redirect(reverse('other:thankyou'))
    

      else:
        form = Modal()
      return render(request,'other/home.html',context={'form':form})

