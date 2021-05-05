from django.shortcuts import render,redirect
from Child.forms import UsForm,ComplaintForm,Newuserform,ChpwdForm
from Child import forms
from django.core.mail import send_mail
from Children_Welfare import settings
from django.contrib import messages
from django.contrib.auth.models import User
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

def deletedata(req,st):
	data=Newuser.objects.get(id=st)
	data.delete()
	return redirect('/show')

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
	data=Newuser.objects.all()
	return render(request,'html/showdata.html',{'info1':data})
	

def infodelete(req,et):
	data=Newuser.objects.get(id=et)
	#print(data)
	if req.method=="POST":
		data.delete()
		return redirect('/show')
	return render(req,'html/userdelete.html',{'sd':data})

# def edit(re,id):
# 	data=UsrRg.objects.get(id=id)
# 	if re.method=="POST":
# 		data.username=re.POST["username"]
# 		data.email=re.POST["email"]
# 		data.age=re.POST["age"]
# 		data.password=re.POST["password"]
# 		data.save()
# 		return HttpResponse("Data Saved Successfully")
# 	return render(re,'html/useredit.html',{'info':data})

def userupdate(up,si):
	t=Newuser.objects.get(id=si)
	y=NewData.objects.get(pid_id=si)
	if up.method=="POST":
		d=Userupdate(up.POST,instance=t)
		k=NewUsrForm(up.POST,instance=y)
		if(d.is_valid() and k.is_valid()):
			d.save()
			k.save()
			return redirect('/show')
	d=Userupdate(instance=t)
	k=NewUsrForm(instance=y)
	return render(up,'html/updateuser.html',{'us':d,'nt':k})

def userinfo(ty,uname):
	p=Newuser.objects.get(username=uname)
	#print(p.id) debugging
	h=NewData.objects.get(pid_id=p.id)
	return render(ty,'html/uinfo.html',{'y':p,'yu':h})




