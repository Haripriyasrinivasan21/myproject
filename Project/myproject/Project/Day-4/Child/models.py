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
	d=[('1',"Yearly Once"),('2',"Monthly Once"),('3',"Quarterly Once"),('4',"One time donation")]
	s=[('F',"Food"),('C',"Clothes"),('M',"Money")]
	p=[('G',"Google pay",'C',"Card",'P',"Paytm")]
	user_name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	ways_to_donate=models.CharField(max_length=50,choices=d)
	sponsor_way=models.CharField(max_length=50,choices=s)
	donating_date=models.DateField(null=True)
	uid=models.ForeignKey(User,on_delete=models.CASCADE)

# class Occdonate(models.Model):
# 	a=[('F',"Food"),('C',"Clothes"),('M',"Money")]
# 	b=[('G',"Google pay",'C',"Card",'P',"Paytm")]
# 	user_name=models.CharField(max_length=50)
# 	email=models.EmailField(max_length=50)
# 	occassion_name=models.CharField(max_length=50)
# 	donating_date=models.DateField(null=True)
# 	sponsor_way=models.CharField(max_length=50,choices=a)
# 	amount=models.IntegerField(null=True)
# 	uid=models.ForeignKey(User,on_delete=models.CASCADE)



