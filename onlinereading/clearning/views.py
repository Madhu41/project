from onlinereading import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse
from clearning.forms import Usregis,Upd,Pad
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from clearning.models import Exfd,Exam



# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def start(request):
	return render(request,'html/start.html')

def cflow(request):
	return render(request,'html/datatypes.html')

def fcn(request):
	return render(request,'html/function.html')

def arr(request):
	return render(request,'html/arrays.html')
 
def poter(request):
 	return render(request,'html/pointer.html')

def strg(request):
	return render(request,'html/strings.html')

def struc(request):
	return render(request,'html/structures.html')

def uni(request):
	return render(request,'html/unions.html')

	


def register(request):
	if request.method == "POST":
		y = Usregis(request.POST)
		if y.is_valid():
			p = y.save(commit=False)
			rc = p.email
			# print(rc)
			sb = "Testing Email to register for Worklog Project"
			mg = "Hi Welcome {} you have successfully registered in our portal with password: {}".format(p.username,p.password)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[rc])
			if snt == 1:
				p.save()
				messages.success(request,"Please check your {} for login creadentials".format(rc))
				return redirect('/lg')
			messages.danger(request,"please enter correct emailid or username or password")
			# print(p.username,p.email)
	y = Usregis()
	return render(request,'html/register.html',{'t':y})

@login_required
def dashboard(request):
	return render(request,'html/dashboard.html')
	
@login_required
def onlineexam(request):
	results = Exam.objects.all()
	return render(request,'html/quiz.html',{"Exam":results})

@login_required
def prfle(request):
	return render(request,'html/profile.html')

@login_required
def updf(request):
	if request.method == "POST":
		p=Upd(request.POST,instance=request.user)
		t=Pad(request.POST,request.FILES,instance=request.user.exfd) 
		if p.is_valid() and t.is_valid():
			p.save()
			t.save()
			messages.success(request,"{} your profile updated successfully".format(request.user.username))
			return redirect('/pf')
	p = Upd(instance=request.user)
	t = Pad(instance=request.user.exfd)
	return render(request,'html/updateprofile.html',{'r':p,'q':t})