
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pword = request.POST['pword']
        cpword = request.POST['cpword']

        myuser = User.objects.create_user(username,email,pword)
        myuser.first_name = fname
        myuser.last_name  = lname

        myuser.save()

        messages.success(request,"Your Account has been Successfully Created.")

        return redirect('Login')

    return render(request,"authentication/signup.html")

def Login(request):

    if request.method == "POST":
        username = request.POST['username']
        pword = request.POST['pword']

        user = authenticate(username=username,password=pword)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request,'authentication/index.html',{'fname':fname})
        
        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')


    return render(request,"authentication/Login.html")

def Logout(request):
    logout(request)
    messages.success(request,"You're successfully logout")
    return redirect("home")

def Register(request):
    return render(request,"authentication/Register.html")

    


