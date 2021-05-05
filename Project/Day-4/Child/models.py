from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Complaintbox(models.Model):
	p_name=models.CharField(max_length=100)
	p_email=models.EmailField(max_length=50)
	p_complaint=models.CharField(max_length=1000)


class User(AbstractUser):
	t = (
		(1,'Donor'),
		(2,'Org'),
		(3,'Anonymous'),
		)
	i=[('I',"India")]
	role = models.IntegerField(default=3,choices=t)
	Dob=models.DateField(null=True)
	Mobile_Number=models.IntegerField(null=True)
	Address=models.TextField()
	Country=models.CharField(max_length=20,choices=i)
	Postal_code=models.IntegerField(null=True)
	City=models.CharField(max_length=20)
	impf=models.ImageField(upload_to='Profiles/',default="profile.jpg")


class Donate(models.Model):
	d=[('1',"Yearly Once"),('2',"Monthly Once"),('3',"Quarterly Once")]
	s=[('F',"Food"),('C',"Clothes"),('M',"Money")]
	p=[('G',"Google pay",'C',"Card",'P',"Paytm")]
	User_Name=models.CharField(max_length=50)
	Email_ID=models.EmailField(max_length=50)
	Mobile_Number=models.IntegerField(null=True)
	Ways_to_donate=models.CharField(max_length=50,choices=d)
	Sponsor_way=models.CharField(max_length=50,choices=s)
	Donating_Date=models.DateField(null=True)
	Pan=models.CharField(max_length=50)
	Amount=models.IntegerField(null=True)
	Payment_Mode=models.CharField(max_length=20,choices=p)
	uid=models.ForeignKey(User,on_delete=models.CASCADE)

class Occdonate(models.Model):
	s=[('F',"Food"),('C',"Clothes"),('M',"Money")]
	p=[('G',"Google pay",'C',"Card",'P',"Paytm")]
	User_Name=models.CharField(max_length=50)
	Email_ID=models.EmailField(max_length=50)
	Mobile_Number=models.IntegerField(null=True)
	Occassion_Name=models.CharField(max_length=50)
	Occassion_Date=models.DateField(null=True)
	Sponsor_way=models.CharField(max_length=50,choices=s)
	Pan=models.CharField(max_length=50)
	Amount=models.IntegerField(null=True)
	Payment_Mode=models.CharField(max_length=20,choices=p)
	uid=models.ForeignKey(User,on_delete=models.CASCADE)

class Onetimedon(models.Model):
	s=[('F',"Food"),('C',"Clothes"),('M',"Money")]
	p=[('G',"Google pay",'C',"Card",'P',"Paytm")]
	User_Name=models.CharField(max_length=50)
	Email_ID=models.EmailField(max_length=50)
	Mobile_Number=models.IntegerField(null=True)
	Sponsor_way=models.CharField(max_length=50,choices=s)
	Donating_Date=models.DateField(null=True)
	Pan=models.CharField(max_length=50)
	Amount=models.IntegerField(null=True)
	Payment_Mode=models.CharField(max_length=20,choices=p)
	uid=models.ForeignKey(User,on_delete=models.CASCADE)



# class service(models.Model):
# 	r=[('d',"Donor"),('v',"Volunteer")]
# 	Guest_Name=models.CharField(max_length=50)
# 	Email_ID=models.EmailField(max_length=50)
# 	My_Role=models.CharField(max_length=20,choices=r)


