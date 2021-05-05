from django.shortcuts import render,redirect
from Emp.models import UsrRg,NewData
from Emp.forms import UsregForm,Userupdate,NewUsrForm
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def login(request):
	return render(request,'html/login.html')

def register(request):
	if request.method=="POST":
		u=request.POST['uname']
		p=request.POST['pd']
		m=request.POST['eml']
		a=request.POST['ag']
		d={'un':u,'pas':p,'em':m,'age':a}
		return render(request,'html/details.html',{'d':d})
	return render(request,'html/register.html')


def crud(request):
	if request.method=="POST":
		un=request.POST['username']
		email=request.POST['email']
		pas=request.POST['password']
		age=request.POST['age']
		data2=UsrRg.objects.all()
		if len(un)!=0:
			data=UsrRg.objects.create(username=un,password=pas,email=email,age=age)
		return render(request,'html/actions.html',{'info':data2})
	data2=UsrRg.objects.all()
	return render(request,'html/actions.html',{'info':data2})

def deletedata(req,st):
	data=UsrRg.objects.get(id=st)
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
	data=UsrRg.objects.all()
	return render(request,'html/showdata.html',{'info1':data})
	

def infodelete(req,et):
	data=UsrRg.objects.get(id=et)
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
	t=UsrRg.objects.get(id=si)
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
	p=UsrRg.objects.get(username=uname)
	#print(p.id) debugging
	h=NewData.objects.get(pid_id=p.id)
	return render(ty,'html/uinfo.html',{'y':p,'yu':h})
