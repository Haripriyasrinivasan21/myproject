from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from Child.models import Complaintbox,User,Donor

class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))
	class Meta:
		model=User
		fields=["username","email"]
		widgets={"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"UserName",
			}),
			"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Email_ID",
			}),

		}

class ComplaintForm(forms.ModelForm):
	class Meta:
		model=Complaintbox
		fields="__all__"

class Newuserform(forms.ModelForm):
	class Meta:
		model=User
		fields=["Dob","Mobile_Number","PAN","Address","Country","Postal_code","City"]
		widgets={
		"Dob":forms.DateInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter your Date Of Birth",
			"required":True,
			}),
		"Mobile_Number":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Phone number",
			"required":True,
			}),
		"PAN":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter your Permanent Acc no",
			"required":True,
			}),
		"Address":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter your Address",
			"required":True,
			}),
		"Country":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter your Country",
			"required":True,
			}),
		"Postal_code":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter your Postal code",
			"required":True,
			}),
		"City":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter your City",
			"required":True,
			}),
		}



class ChpwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter Old password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter New password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Confirm your New password"}))
	class Meta:
		model=User
		fields=['oldpassword','newpassword','confirmpassword']


class Donorform(forms.ModelForm):
	class Meta:
		model=Donor
		fields=["username","email","donated_on","donated_thing","donated_way"]
		widgets={
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Username",
			"required":True,
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Email ID",
			"required":True,
			}),
		"donated_on":forms.DateInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter your Date of Donation",
			"required":True,
			}),
		"donated_thing":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Donated Thing",
			"required":True,
			}),
		"donated_way":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Donated Way",
			"required":True,
			}),
		}

