from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
 	return HttpResponse("<h1 style='color:white;background-color:green'>This is home page</h1>")

def chk(request):
	return HttpResponse("<script>alert('Hi Good Afternoon')</script><h2>Welcome</h2>")

def homepage(request):
	return render(request,'html/homepage.html')

def lgn(re):
	return render(re,'html/login.html')

def reg(rt):
	return render(rt,'html/register.html')