from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from service.models import UserService,User,CarCategory,Services

from django.contrib.auth import get_user_model

User = get_user_model()
class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border-success","placeholder":"enter password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border-success","placeholder":"confirm password"}))


	class Meta:
		model=User
		fields = ['username','email','last_name']
		widgets = {
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Username",
			"required":True,
			}),
		"last_name":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Lastname",
			"required":True,
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter emailid",
			"required":True,
			}),
		}
		
class ServiceForm(forms.ModelForm):
	class Meta:
		model= UserService
		fields=["car_make","car_model","service_type","price"]
		widgets = {
		"car_make":forms.TextInput(attrs= {
			"class":"form-control","placeholder":"enter car_make",
			}),
		"car_model":forms.TextInput(attrs= {
			"class":"form-control","placeholder":"enter car_model",
			}),
		"service_type":forms.TextInput(attrs= {
			"class":"form-control","placeholder":"enter service",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Price",
			}),
		}
class UpdPfle(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"readonly":True,
			}),
		}
		# "email":forms.EmailInput(attrs={
		# 	"class":"form-control",
		# 	"placeholder":"Update EmailId",
		# 	}),
		# "first_name":forms.TextInput(attrs={
		# 	"class":"form-control",
		# 	"placeholder":"Update First Name",
		# 	}),
		# "last_name":forms.TextInput(attrs={
		# 	"class":"form-control",
		# 	"placeholder":"Update Last Name",
		# 		}),

		
		
class Userupdate(forms.ModelForm):
	class Meta:
		model=UserService
		fields=["car_make","car_model","service_type","price"]
		widgets = {
		"car_make":forms.TextInput(attrs= {
			"class":"form-control","placeholder":"select car_make",
			}),
		"car_model":forms.TextInput(attrs= {
			"class":"form-control","placeholder":"select car_model",
			}),
		"service_type":forms.TextInput(attrs= {
			"class":"form-control","placeholder":"select service",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Price",
			}),
		}

class ChpwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Old Password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"New Password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))
		
	class Meta:
		model=['oldpassword','newpassword','confirmpassword']
class ImForm(forms.ModelForm):
	class Meta:
		model=User
		fields=["first_name","last_name","age","gender","impf","phone_no","car_regno","address",]
		widgets={
		"first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter First name"}),
		"last_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Last name"}),
		"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"Update your age"}),
 		"gender":forms.Select(attrs={"class":"form-control","placeholder":"select your gender"}),
		"phone_no":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter phone number"}),
		"car_regno":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter carreg number"}),
		"address":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter address"}),
		}

class CategoryForm(forms.ModelForm):
	class Meta:
		model=CarCategory
		fields=["cname"]
		widgets={
		"cname":forms.TextInput(attrs={"class":"form-control","placeholder":"enter cname"}),
		}
class AddForm(forms.ModelForm):
	class Meta:
		model=Services
		fields=["service_type","price","sid","is_status"]
		widgets = {
		"service_type":forms.TextInput(attrs= {
			"class":"form-control","placeholder":"Enter service_type",
			}),
		"price":forms.NumberInput(attrs= {
			"class":"form-control","placeholder":"enter price",
			}),
		}
