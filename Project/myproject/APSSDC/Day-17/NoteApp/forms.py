from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from NoteApp.models import Complaintbox,ImProfile

class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))
	class Meta:
		model=User
		fields=['username']
		widgets={"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"UserName",
			}),

		}

class ComplaintForm(forms.ModelForm):
	class Meta:
		model=Complaintbox
		fields="__all__"

class UtupForm(forms.ModelForm):
	class Meta:
		model=User
		fields=["username","email"]
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Update Email ID",
			}),
		}

class ImForm(forms.ModelForm):
	class Meta:
		model =ImProfile
		fields=['age',"gender","impf"]
		widgets={
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Update Your Age",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"Select your Gender",
			}),
		}

class ChpwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter Old password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter New password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Confirm your New password"}))
	class Meta:
		model=User
		fields=['oldpassword','newpassword','confirmpassword']

