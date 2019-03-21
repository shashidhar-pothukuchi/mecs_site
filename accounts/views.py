from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from accounts.models import Account

# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['pass']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'You are logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['firstname']
        user_name=request.POST['username']
        last_name=request.POST['lastname']
        gender=request.POST['gender']
        branch=request.POST['branch']
        roll_no=request.POST['rollno']
        email_id=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirmpass']
    #Passwords match
        if password==confirm_password:
            #email check
            if User.objects.filter(email=email_id).exists():
                messages.error(request,  'Email aldready exists.Please login')
                return redirect('register')
            else:
                #Roll no check
                if Account.objects.filter(RollNo=roll_no).exists():
                    messages.error(request,  'Roll-no aldready Registered.Please Login')
                    return redirect('register')
                else:
                    #all-good
                    user=User.objects.create_user(username=user_name, password=password, email=email_id, 
                    first_name=first_name,last_name=last_name)
                    account=Account.objects.create(user=user, gender=gender, RollNo=roll_no, branch=branch)
                    user.save()
                    account.save()
                    messages.success(request,'You are now Registered and can Log in')
                    return redirect('index')
   
        else:
            messages.error(request,'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')