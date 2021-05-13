from django.shortcuts import render,redirect
from service.forms import UsForm,ServiceForm,Userupdate,ChpwdForm,UpdPfle,CategoryForm,AddForm
from django.core.mail import send_mail
from carservice import settings
from django.contrib import messages
from service.models import UserService
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from service.models import User,CarCategory,Services,Cart,Myorders
from django.core.mail import send_mail,EmailMessage
# Create your views here
def home(request):
	cf=CarCategory.objects.all()
	return render(request,'services/home.html',{'u':cf})

def about(request):
	return render(request,'services/about.html')

def contact(request):
	return render(request,'services/contact.html')

def booking(request):
	return render(request,'services/booking.html')

def cart(request):
	return render(request,'/services/cart.html')

def viewuser(request):
	p=User.objects.all()
	return render(request,'services/viewuser.html',{'u':p})

def customer(request,id):
	a=User.objects.get(id=id)
	a.role="2"
	a.save()
	return redirect('/viewuser')

def owner(request,id):
	a=User.objects.get(id=id)
	a.role="1"
	a.save()
	return redirect('/viewuser')

def registration(request):
	if request.method=="POST":
		p=UsForm(request.POST)
		if p.is_valid():
			p.save()
			return redirect('/log')
			
	p=UsForm()
	return render(request,'services/register.html',{'u':p})

def Service(request):
	if request.method=="POST":
		j=ServiceForm(request.POST,request.FILES)
		if j.is_valid():
			i=j.save(commit=False)
			i.uid_id=request.user.id
			i.save()
			return redirect('/showdata')
	j=ServiceForm()
	return render(request,'services/Services.html',{'u':j})

def role(request):
	return render(request,'services/role.html')

def deletedata(req,st):
	data=UserService.objects.get(id=st)
	data.delete()
	return redirect('/cr')

def addcategory(request):
	if request.method=="POST":
		a=CategoryForm(request.POST)
		if a.is_valid():
			a.save()
			return redirect('/home')
	cf=CategoryForm()
	return render(request,'services/addcategory.html',{'c':cf})

def addcarservices(request):
	if request.method=="POST":
		b=AddForm(request.POST)
		if b.is_valid():
			b.save()
			return redirect('/home')
	se=AddForm()
	return render(request,'services/addcarservices.html',{'e':se})

def showinfo(req,bt):
	data=CarCategory.objects.all()
	return render(req,'services/showdata.html',{'info':data})

def infodelete(req,et):
	data=UserService.objects.get(id=et)
	if req.method == "POST":
		data.delete()
		return redirect('/showdata')
	return render(req,'services/userdelete.html',{'sd':data})

def userupdate(up,si):
	t=UserService.objects.get(id=si)
	if up.method=="POST":
		d=Userupdate(up.POST,instance=t)
		if d.is_valid():
			d.save()
			return redirect('/showdata')
	d=Userupdate(instance=t)
	return render(up,'services/updateuser.html',{'us':d})

def profile(req):
	return render(req,'services/profile.html')

def dashboard(req):
	return render(req,'services/dashboard.html')

def cgf(re):
	if re.method=="POST":
		c=ChpwdForm(user=re.user,data=re.POST)
		if c.is_valid():
			c.save()
			return redirect('/log')
	c=ChpwdForm(user=request)
	return render(re,'services/changepassword.html',{'t':c})	

def updprofile(request):
	if request.method == "POST":
		t = UpdPfle(request.POST,instance=request.user)
		if t.is_valid():
			t.save()
			return redirect('/pro')
	t = UpdPfle(instance=request.user)
	return render(request,'services/updateprofile.html',{'z':t})

def categories(request,id):
	d=CarCategory.objects.all()
	p=Services.objects.filter(sid_id=id)
	return render(request,'services/carservices.html',{'da':p,'data':d})

def addcart(request,id):
	b=Services.objects.get(id=id)
	c=Cart(user_id=request.user.id,service_id=id)
	c.save()
	count=0
	data1 = Cart.objects.filter(user_id=request.user.id)
	for i in data1:
		count+=1
	return render(request,'services/addcart.html',{'b':c,'count':count,'data1':data1})

def cartdetails(request):
	c=Cart.objects.filter(user_id=request.user.id)
	d=CarCategory.objects.all()
	sum=0
	count=0
	for i in c:
		count=count+1
		sum=sum+i.service.price
	return render(request,'services/cartdetails.html',{'sum':sum,'count':count,'data':d,'cart':c})

def placeorder(request):
	data=Cart.objects.filter(user_id=request.user.id)
	b=request.user.email
	l1=[]
	l2=[]
	sum=0
	count=0
	for i in data:
		sum=sum+i.service.price
		l1.append(i.service.service_type)
	message='service type ::\n'+' ,'.join(l1)+'\n'+ ' will be contact you.\n'+'Total amount paid: Rs.'+str(sum)+'\n'+'THANK YOU for request!!'
	subject='service booked'
	sender=settings.EMAIL_HOST_USER
	if data:
		t=EmailMessage(subject,message,sender,[b])
		t.send()
		s=Myorders(service_type=i.service.service_type,price=i.service.price,user_id=request.user.id)
		data.delete()
	return render(request,'services/placeorder.html')

def myorders(request):
	my=Myorders.objects.filter(user_id=request.user.id)
	d=CarCategory.objects.all()
	sum=0
	count=0
	for i in my:
		count=count+1
		sum=sum+i.service.price
	return render(request,'services/myorders.html',{'sum':sum,'count':count,'my':my})


