from django.shortcuts import render,redirect
from service.forms import UsForm,ServiceForm,Userupdate,ChpwdForm,UpdPfle,CategoryForm,AddForm
from django.core.mail import send_mail
from carservice import settings
from django.contrib import messages
from service.models import UserService
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from service.models import User,CarCategory,Services,Cart
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
			return redirect('/carservices')
	cf=CategoryForm()
	return render(request,'services/addcategory.html',{'c':cf})

def addcarservices(request):
	if request.method=="POST":
		b=AddForm(request.POST)
		if b.is_valid():
			b.save()
			return redirect('/category')
	se=AddForm()
	return render(request,'services/addcarservices.html',{'e':se})

def showinfo(req):
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

def cart(request,id):
	a=Services.objects.get(id=id)
	if request.method=="POST":
		c=Cart(user_id=request.user.id,service_id=a.id)
		c.save()
		return redirect("/crtcnt")
	return render(request,'services/cart.html',{'crt':a})

def cartcount(request):
	c=Cart.objects.filter(user_id=request.user.id)
	d=CarCategory.objects.all()
	sum=0
	count=0
	for i in c:
		count=count+1
		sum=sum+i.service.price
	return render(request,'services/viewcart.html',{'data':d,'sum':sum,'count':count})

def cartdetails(request):
	c=Cart.objects.filter(user_id=request.user.id)
	d=CarCategory.objects.all()
	sum=0
	count=0
	for i in c:
		count=count+1
		sum=sum+i.service.price
	return render(request,'services/cartdetails.html',{'sum':sum,'count':count,'data':d,'cart':c})

def remove(request,id):
	c=Cart.objects.get(id=id)
	c.delete()
	return redirect('/cartdata')

def placeorder(request):
	c=Cart.objects.filter(user_id=request.user.id,service_id=id)
	d=CarCategory.objects.all()
	count=0
	for i in c:
		count=count+1
		sum=sum+i.product.price
	return render(request,'html/placeorder.html',{'count':count,'data':d,'cart':c})

def pdf(request,id):
	b=Services.objects.get(id=id)
	c=Cart(user_id=request.user.id,service_id=id)
	d=CarCategory.objects.all()
	sum=0
	count=0
	for i in c:
		count=count+1
		sum=sum+i.service.price
	template_path="services/pdfpage.html"
	dic={}
	for i in c:
		dic[i.id]=i.service.service_type,i.service.price
	var=dic.values()
	dic2={'var':var,'sum':sum}
	response=HttpResponse(content_type="application/pdf")
	response["Content-Disposition"]="attachment;filename='productsreport.pdf'"
	template=get_template(template_path)
	html=template.render(dic2)
	pisa_status=pisa.CreatePDF(html,dest=response)
	if pisa_status.err:
		return HttpResponse("wrong")
	return response

def addcart(request,id):
	b=Services.objects.get(id=id)
	c=Cart(user_id=request.user.id,service_id=id)
	c.save()
	count=0
	data1 = Cart.objects.filter(user_id=request.user.id)
	for i in data1:
		count+=1
	return render(request,'services/addcart.html',{'b':c,'count':count,'data1':data1})

def msg(request):
	c=Cart.objects.filter(user_id=request.user.id,service_id=id)
	d=CarCategory.objects.all()
	count=0
	for i in c:
		count+=1
	return render(request,'services/message.html',{'data':d,'count':count})

def msg1(request):
	c=Cart.objects.filter(user_id=request.user.id,service_id=id)
	d=CarCategory.objects.all()
	count=0
	for i in c:
		count+=1
	return render(request,'services/message1.html',{'data':d,'count':count})
