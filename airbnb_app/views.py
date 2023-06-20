from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout,decorators

from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
from django.core import validators
from django.core.exceptions import ValidationError
from .models import Customer
# Create your views here.


def index(request):
    return render(request, 'airbnb_app/index.html')




def customerLogin(request):

    if request.method == 'POST':
        print(request.POST)
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request,username=email,password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully')
            
            if "house-register/login/" in request.path:
               
                return redirect('house-register')
            else:
                return redirect('home')

        else:
            messages.success(request, 'Incorrect credentials')
            return redirect('app-login')
    elif request.user.is_authenticated:

        return redirect('home')

    else :

        return render( request, 'airbnb_app/login.html')
        

def signup(request):

    if request.method == 'POST':
        print(request.POST)
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        mobileNumber = request.POST['mobileNumber']
        gender = request.POST['gender']
        dateOfBirth = request.POST['dateOfBirth']
        try:
            validators.validate_email(email)
            validate_password(password)
            if (not str(mobileNumber).isnumeric()) or len(mobileNumber) != 10:

                raise ValidationError("Please Check Your Mobile number !!")


            
        except ValidationError as err:
            messages.success(request, err.messages[0])
            return render(request,'airbnb_app/signup.html',{"data":request.POST})

        print(request.POST)

        user = Customer()
        user.first_name = fname
        user.last_name = lname
        user.set_password(password)
        user.email = email
        user.mobileNumber = mobileNumber
        user.gender = gender
        user.dateOfBirth = dateOfBirth
        user.save()
        messages.success(request, 'Saved!!!')
        return redirect('home')
    
    elif request.user.is_authenticated:

        return redirect('home')
    
    else:
        return render(request, 'airbnb_app/signup.html')


def customerLogout(request):

    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        return redirect('app-login')


def houseReg(request):
    if request.user.is_authenticated:
        return render(request, 'airbnb_app/signup.html')
    else:
        messages.success(request, 'please sign in')
        return render(request, 'airbnb_app/login.html',{"data" : "from_regpage"})