from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


class User(AbstractUser):
	t = (
		(1,'owner'),
		(2,'customer'),
		(3,'Anonymous'),
		)
	role = models.IntegerField(default=3,choices=t)
	g=[('M',"Male"),('F','Female')]
	age=models.IntegerField(default=10)
	impf=models.ImageField(upload_to='Profiles/',default="Note.jpg")
	gender=models.CharField(max_length=10,choices=g)
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	phone_no=models.IntegerField(null=True)
	car_regno=models.CharField(max_length=20)
	address=models.CharField(max_length=200)
# class ImProfile(models.Model):
# 	g = [('M',"Male"),('F','Female')]
# 	first_name=models.CharField(max_length=100)
# 	last_name=models.CharField(max_length=100)
# 	email=models.EmailField(max_length=100)
# 	phone_no=models.IntegerField(max_length=10)
# 	car_regno=models.TextField(max_length=8)
# 	age = models.IntegerField(default=10)
# 	impf = models.ImageField(upload_to='Profiles/',default="profile.png")
# 	gender = models.CharField(max_length=10,choices=g)

class UserService(models.Model):
	car_make=models.CharField(max_length=100)
	car_model=models.CharField(max_length=100)
	service_type=models.CharField(max_length=100)
	price=models.DecimalField(max_digits=6,decimal_places=2)
	uid=models.ForeignKey(User,on_delete=models.CASCADE)
class CarCategory(models.Model):
	cname=models.CharField(max_length=20)
	def __str__(self):
		return self.cname
class Services(models.Model):
	service_type=models.CharField(max_length=30)
	price=models.IntegerField()
	sid=models.ForeignKey(CarCategory,on_delete=models.CASCADE)
	is_status=models.IntegerField(default=1)
	def __str__(self):
		return self.sname

class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	service=models.ForeignKey(Services,on_delete=models.CASCADE)


class Myorders(models.Model):
	service_type=models.CharField(max_length=30)
	price=models.IntegerField()
	is_status=models.IntegerField(default=1)
	date=models.DateTimeField(auto_now_add='True',null='True')
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)



