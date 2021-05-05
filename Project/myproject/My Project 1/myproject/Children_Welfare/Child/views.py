from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def feedback(request):
	return render(request,'html/feedback.html')

def joinus(request):
	return render(request,'html/joinus.html')

def profile(req):
	return render(req,'html/profile.html')

def donate(req):
	return render(req,'html/donate.html')

def occasion(req):
	return render(req,'html/occasion.html')

def regi(request):
	if request.method=="POST":
		p=UsForm(request.POST)
		if p.is_valid():
			p.save()
			return redirect('/lg')
	p=UsForm()
	return render(request,'html/register.html',{'u':p})

@login_required
def cgf(request):
	if request.method=="POST":
		print("yes")
		c=ChpwdForm(user=request.user,data=request.POST)
		if c.is_valid():
			c.save()
			return redirect('/lg')
	c=ChpwdForm(user=request)
	return render(request,'html/changepassword.html',{'t':c})


