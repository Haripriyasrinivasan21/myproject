from Emp.models import UsrRg,NewData
from django import forms #from django.forms import ModelForm



class UsregForm(forms.ModelForm): #class UsregForm(ModelForm):
	class Meta:
		model=UsrRg
		fields= ['username','email','password']
		widgets={
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Username",
			"required":True,
			}),
		"password":forms.PasswordInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Password",
			"required":True,
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Email ID",
			"required":True,
			}),
		}

class Userupdate(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','age']
		widgets={
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Username",
			"required":True,
			}),
		"password":forms.PasswordInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Password",
			"required":True,
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Email ID",
			"required":True,
			}),
		"age":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"Update your Age",
			"required":True,
			}),
		}

class NewUsrForm(forms.ModelForm):
	class Meta:
		model=NewData
		fields=['mobile','gender']
		widgets={"mobile":forms.TextInput(attrs={"class":"form-control",
			"placeholder":"Update your phone number",}),
		"gender":forms.Select(attrs={"class":"form-control",}),
		}		