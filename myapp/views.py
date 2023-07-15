from django.shortcuts import render,HttpResponse
from myapp.models import Contact
from django.contrib import messages

from datetime import datetime

def index(request):
    context={
        'var':'This is my first django page'
    }
    # return HttpResponse("Welcome Kuntal !!")
    # messages.info(request,"High there !!")
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
    # return HttpResponse("Welcome Kuntal to the about page!!")
def services(request):
    return render(request,'services.html')
    # return HttpResponse("Welcome Kuntal to the services page !!")
def contact(request):
    if request.method=='POST':
        email=request.POST.get('email')
        pwd=request.POST.get('password')
        connect=Contact(email=email,password=pwd,date=datetime.today())
        connect.save()
        messages.success(request, "Profile details updated.")
    return render(request,'contact.html')
    # return HttpResponse("Welcome Kuntal to the contact page!!")


# Create your views here.
