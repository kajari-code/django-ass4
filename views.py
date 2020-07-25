from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from . import models
# Create your views here.
from . import forms
def registrationpage(request):
    f1=forms.MyForm()
    return render(request,"registration.html",{'form':f1})

def getdata(request):
    if request.method=='GET':
        un=request.GET['Username']
        p=request.GET['Password']
        Em=request.GET['Email']
        Ph=request.GET['PhoneNo']
        return render(request,"legal.html",{"username":un,"Password":p,"email":Em,"phoneno":Ph})
    if request.method=='POST':
        un=request.POST['Username']
        p=request.POST['Password']
        Em=request.POST['Email']
        Ph=request.POST['PhoneNo']
        s1=models.Student(Username=un,Password=p,Email=Em,PhoneNo=Ph)
        s1.save()
        return render(request,"legal.html",{"username":un,"password":p,"email":Em,"phoneno":Ph})
   