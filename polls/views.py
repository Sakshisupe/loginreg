from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'base.html')
        else:
            messages.error(request,"invalid credentials")
            return render(request,"login.html")
    return render(request,'login.html')
def register(request):

    if request.method=='POST':
        first_name=request.POST.get('f_name')
        last_name=request.POST.get('l_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
       

        user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
        user.save()
        print("created")
        # return redirect('/')
        messages.success(request,"registration succesful.Please log in")
        
    else:
        return render(request,'register.html')
    return render(request,'register.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')
