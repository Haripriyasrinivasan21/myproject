from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from Child.models import Complaintbox,User,Donate,Occdonate,Onetimedon#,service

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
		fields=["User_Name","Email_ID","Mobile_Number","Ways_To_Donate","Sponsor_way","Donating_Date","Pan","Amount","Payment_Mode"]
		widgets={
		"User_Name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"User Name",
			"required":True,
			}),
		"Email_ID":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Email ID",
			"required":True,
			}),
		"Mobile_Number":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Phone number",
			"required":True,
			}),
		"Ways_To_Donate":forms.Select(attrs = {
			"class":"form-control",
			"required":True,
			}),
		"Sponsor_Way":forms.Select(attrs = {
			"class":"form-control",
			"required":True,
			}),
		"Donating_Date":forms.DateInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Donating Date",
			"required":True,
			}),
		"Pan":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter your Permanent Acc no",
			}),
		"Amount":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Amount",
			}),
		"Payment_Mode":forms.Select(attrs = {
			"class":"form-control",
			"placeholder":"Select Payment Mode",
			"required":True,
			}),
		}

class Occdonateform(forms.ModelForm):
	class Meta:
		model=Occdonate
		fields=["User_Name","Email_ID","Mobile_Number","Occassion_Name","Occassion_Date","Sponsor_way","Pan","Amount","Payment_Mode"]
		widgets={
		"User_Name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"User Name",
			"required":True,
			}),
		"Email_ID":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Email ID",
			"required":True,
			}),
		"Mobile_Number":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Phone number",
			"required":True,
			}),
		"Occassion_Name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Occassion Name",
			"required":True,
			}),
		"Occassion_Date":forms.DateInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Occassion Date",
			"required":True,
			}),
		"Sponsor_Way":forms.Select(attrs = {
			"class":"form-control",
			"required":True,
			}),
		"Pan":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter your Permanent Acc no",
			}),
		"Amount":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Amount",
			}),
		"Payment_Mode":forms.Select(attrs = {
			"class":"form-control",
			"placeholder":"Select Payment Mode",
			"required":True,
			}),
		}


class Onetimedonform(forms.ModelForm):
	class Meta:
		model=Onetimedon
		fields=["User_Name","Email_ID","Mobile_Number","Sponsor_way","Donating_Date","Pan","Amount","Payment_Mode"]
		widgets={
		"User_Name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"User Name",
			"required":True,
			}),
		"Email_ID":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Email ID",
			"required":True,
			}),
		"Mobile_Number":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Phone number",
			"required":True,
			}),
		"Sponsor_Way":forms.Select(attrs = {
			"class":"form-control",
			"required":True,
			}),
		"Donating_Date":forms.DateInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Donating Date",
			"required":True,
			}),
		"Pan":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter your Permanent Acc no",
			}),
		"Amount":forms.NumberInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Amount",
			}),
		"Payment_Mode":forms.Select(attrs = {
			"class":"form-control",
			"placeholder":"Select Payment Mode",
			"required":True,
			}),
		}





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