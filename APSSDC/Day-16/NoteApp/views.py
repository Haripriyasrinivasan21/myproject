from django.shortcuts import render,redirect
from NoteApp.forms import UsForm,ComplaintForm,ImForm,UtupForm
from django.core.mail import send_mail
from NoteSharing import settings
from django.contrib import messages
from django.contrib.auth.models import User
from NoteApp.models import ImProfile
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

def profile(req):
	return render(req,'html files/profile.html')

def complaint(req):
	if req.method=="POST":
		data=ComplaintForm(req.POST)
		if data.is_valid():
			subject='Confirmation of your Complaint'
			body="Thank you, We'll look into it ASAP"+req.POST['p_name']
			receiver=req.POST['p_email']
			sender=settings.EMAIL_HOST_USER
			send_mail(subject,body,sender,[receiver])
			data.save()
			messages.success(req,"Successfully Sent to ur mail"+receiver)
			return redirect('/')
	form=ComplaintForm()
	return render(req,'html files/complaint.html',{'c':form})

def updpf(request):
	if request.method=="POST":
		u=UtupForm(request.POST,instance=request.user)
		i=ImForm(request.POST,request.FILES,instance=request.user.improfile)
		if u.is_valid() and i.is_valid():
			u.save()
			i.save()
			return redirect('/pro')
	u=UtupForm(instance=request.user)
	i=ImForm(instance=request.user.improfile)
	return render(request,'html files/updateprofile.html',{'us':u,'imp':i})
