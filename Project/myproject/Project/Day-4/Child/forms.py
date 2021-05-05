from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from Child.models import Complaintbox,User,Donate

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
		fields=["Dob","Mobile_Number","Address","Country","Postal_code","City"]
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


class Donateform(forms.ModelForm):
	class Meta:
		model=Donate
		fields=["user_name","email","ways_to_donate","sponsor_way","donating_date"]
		widgets={
		"user_name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"User Name",
			"required":True,
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Email ID",
			"required":True,
			}),
		"ways_to_donate":forms.Select(attrs = {
			"class":"form-control",
			"required":True,
			}),
		"sponsor_way":forms.Select(attrs = {
			"class":"form-control",
			"required":True,
			}),
		"donating_date":forms.DateInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Donating Date",
			"required":True,
			}),
		}

# class Occdonateform(forms.ModelForm):
# 	class Meta:
# 		model=Occdonate
# 		fields=["user_name","email","occassion_name","sponsor_way","donating_date"]
# 		widgets={
# 		"user_name":forms.TextInput(attrs = {
# 			"class":"form-control",
# 			"placeholder":"User Name",
# 			"required":True,
# 			}),
# 		"email":forms.EmailInput(attrs = {
# 			"class":"form-control",
# 			"placeholder":"Enter Email ID",
# 			"required":True,
# 			}),
# 		"occassion_name":forms.TextInput(attrs = {
# 			"class":"form-control",
# 			"placeholder":"Enter Occassion Name",
# 			"required":True,
# 			}),
# 		"sponsor_way":forms.Select(attrs = {
# 			"class":"form-control",
# 			"required":True,
# 			}),
# 		"donating_date":forms.DateInput(attrs = {
# 			"class":"form-control",
# 			"placeholder":"Enter Occassion Date",
# 			"required":True,
# 			}),
# 		}









# class Serviceform(forms.ModelForm):
# 	class Meta:
# 		model=service
# 		fields=["Guest_Name","Email_ID","My_Role"]
# 		widgets={
# 		"username":forms.TextInput(attrs = {
# 			"class":"form-control",
# 			"placeholder":"Username",
# 			"required":True,
# 			}),
# 		"Email_ID":forms.EmailInput(attrs = {
# 			"class":"form-control",
# 			"placeholder":"Enter Email ID",
# 			"required":True,
# 			}),
# 		"My_Role":forms.Select(attrs = {
# 			"class":"form-control",
# 			"required":True,
# 			}),