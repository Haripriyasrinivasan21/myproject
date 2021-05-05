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
	role = models.IntegerField(default=3,choices=t)
	Dob=models.DateField(null=True)
	Mobile_Number=models.IntegerField(null=True)
	PAN=models.IntegerField(null=True)
	Address=models.TextField()
	Country=models.CharField(max_length=20)
	Postal_code=models.IntegerField(null=True)
	City=models.CharField(max_length=20)
	impf=models.ImageField(upload_to='Profiles/',default="profile.jpg")


class Donor(models.Model):
	username=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	donated_on=models.DateTimeField()
	donated_thing=models.CharField(max_length=50)
	donated_way=models.CharField(max_length=50)
	uid=models.ForeignKey(User,on_delete=models.CASCADE)
