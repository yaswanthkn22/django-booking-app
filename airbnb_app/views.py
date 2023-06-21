from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout,decorators
from django.db import transaction
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
from django.core import validators
from django.core.exceptions import ValidationError
from .models import Customer, House, HouseImg, Owner
import datetime
# Create your views here.


def index(request):
    return render(request, 'airbnb_app/index.html')


def houseDetails(request):

    return HttpResponse("house details")

def customerLogin(request):

    if request.method == 'POST':
       
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
    

        image = request.FILES.get('profileImage')
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = str(request.POST['email'])
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

      

        user = Customer()
        user.first_name = fname
        user.last_name = lname
        user.set_password(password)
        
        user.email = email.lower()
        user.mobileNumber = mobileNumber
        user.gender = gender
        user.dateOfBirth = dateOfBirth
        if image:
            user.profileImg = image
        user.save()
        login(request,user)
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
        if request.method == 'POST':
            blockingStartDate = request.POST.get('booking_start')
            blockingEndDate = request.POST.get('booking_end')

            if blockingStartDate and blockingEndDate and blockingStartDate >= blockingEndDate:
                messages.success(request, 'start block date should not be greater than or equal to end block date')
                return redirect('house-register')

            user = request.user
           
            name = request.POST.get('name')
            country = request.POST.get('country')
            state = request.POST.get('state')
            district = request.POST.get('district')
            nearestTown = request.POST.get('nearest_town')
            pricePerDay = request.POST.get('price_per_day')
            amenitiesList = list(request.POST.getlist('amenities'))
            amenities = ','.join(amenitiesList)
            images = request.FILES.getlist('images')
            try:
                with transaction.atomic():
                    owner = Owner(user=user)
                    owner.save()
                    house = House()
                    house.owner = owner
                    if blockingEndDate and blockingStartDate:
                        house.bookingStart = blockingStartDate
                        house.bookingEnd = blockingEndDate
                    
                
                    house.aminities = amenities
                    house.name = name
                    house.country = country
                    house.state = state
                    house.district = district
                    house.nearestTown = nearestTown
                    house.pricePerDay = pricePerDay
                    house.save()
                    
                    for image in images:
                            HouseImg.objects.create(image=image, houseId=house)

                    return redirect('home')
            except Exception as e:
                messages.success(request, e)
                return redirect('house-register')
        else:
            return render(request, 'airbnb_app/houseReg.html')

    else:
        messages.success(request, 'please sign in')
        return render(request, 'airbnb_app/login.html',{"data" : "from_regpage"})