from django.shortcuts import render,redirect
from NoteApp.forms import UsForm

# Create your views here.

def home(request):
	return render(request,'html files/home.html')

def about(request):
	return render(request,'html files/about.html')

def contact(request):
	return render(request,'html files/contact.html')

def regi(request):
	if request.method=="POST":
		p=UsForm(request.POST)
		if p.is_valid():
			p.save()
			return redirect('/lg')
	p=UsForm()
	return render(request,'html files/register.html',{'u':p})

def dashboard(request):
	return render(request,'html files/dashboard.html')

