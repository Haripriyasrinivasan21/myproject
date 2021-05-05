from django.shortcuts import render,redirect
from Child.forms import UsForm,ComplaintForm,Newuserform,ChpwdForm,Donor,Donorform
from django.core.mail import send_mail
from Children_Welfare import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Child.models import User
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

@login_required
def updpf(request):
	if request.method=="POST":
		u=UsForm(request.POST,instance=request.user)
		i=Newuserform(request.POST,request.FILES,instance=request.user)
		if u.is_valid() and i.is_valid():
			u.save()
			i.save()
			return redirect('/pro')
	u=UsForm(instance=request.user)
	i=Newuserform(instance=request.user)
	return render(request,'html/updateprofile.html',{'us':u,'imp':i})


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
	return render(req,'html/complaint.html',{'c':form})

def Newone(request):
	form=forms.Newuserform()
	if request.method=="POST":
		form=forms.Newuserform(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/th')
	return render(request,'html/newuser.html',{'form':form})


def donor(request):
	if request.method=="POST":
		details=Donorform(request.POST)
		if details.is_valid():
			k=details.save(commit=False)
			k.uid_id=request.user.id
			k.save()
			return redirect('/show')
	details=Donorform()
	return render(request,'html/donordetails.html',{'details':details})


def thankyou(req):
	return render(req,'html/thankyou.html')




def crud(request):
	if request.method=="POST":
		fn=request.POST['First_Name']
		ln=request.POST['Last_Name']
		email=request.POST['Email_ID']
		dob=request.POST['Dob']
		mn=request.POST['Mobile_Number']
		pan=request.POST['PAN']
		add=request.POST['Address']
		coun=request.POST['Country']
		pc=request.POST['Postal_code']	
		city=request.POST['City']
		data2=Newuser.objects.all()
		if len(un)!=0:
			data=Newuser.objects.create(First_Name=fn,Last_Name=ln,Email_ID=email,Dob=dob,Mobile_Number=mn,PAN=pan,Address=add,Country=coun,Postal_code=pc,City=city)
		return render(request,'html/actions.html',{'info':data2})
	data2=Newuser.objects.all()
	return render(request,'html/actions.html',{'info':data2})

# def deletedata(req,st):
# 	data=Newuser.objects.get(id=st)
# 	data.delete()
# 	return redirect('/show')

def dform(request):
	if request.method=="POST":
		e=UsregForm(request.POST)

		if e.is_valid():
			q=e.save()
			y=NewData.objects.create(pid_id=q.id)
			#return HttpResponse("User Created Successfully")
			return redirect('/show')
	e=UsregForm()
	return render(request,'html/dyform.html',{'tu':e})

def showinfo(request):
	data=Donor.objects.filter(uid_id=request.user.id)
	return render(request,'html/showdata.html',{'info1':data})


def deletedata(req,st):
	data=Donor.objects.get(id=st)
	#print(data)
	if req.method=="POST":
		data.delete()
		return redirect('/show')
	return render(req,'html/userdelete.html',{'sd':data})

def userupdate(up,si):
	t=Donor.objects.get(id=si)
	if up.method=="POST":
		d=Donorform(up.POST,instance=t)
		if(d.is_valid()):
			d.save()
			return redirect('/show')
	d=Donorform(instance=t)
	return render(up,'html/updateuser.html',{'us':d})

def userinfo(ty,uname):
	p=Donorform.objects.get(username=uname)
	h=Donorform.objects.get(pid_id=p.id)
	return render(ty,'html/uinfo.html',{'y':p,'yu':h})


def roles(request):
	return render(request,'html/role.html')


