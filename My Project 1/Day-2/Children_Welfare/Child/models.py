from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Complaintbox(models.Model):
	p_name=models.CharField(max_length=100)
	p_email=models.EmailField(max_length=50)
	p_complaint=models.CharField(max_length=1000)

class Newuser(models.Model):
	First_Name=models.CharField(max_length=50)
	Last_Name=models.CharField(max_length=50)
	Email_ID=models.EmailField(max_length=30)
	Dob=models.DateField()
	Mobile_Number=models.IntegerField()
	PAN=models.IntegerField()
	Address=models.TextField()
	Country=models.CharField(max_length=20)
	Postal_code=models.IntegerField()
	City=models.CharField(max_length=20)

	# def __str__(self):
	# 	return self.username



