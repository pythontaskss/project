from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from app.models import Detail


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.set_password(password)
                user.is_staff = True
                user.save()
                return redirect('login_user')
    else:
        print("this is not post method")
        return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('new')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login_user')

    else:
        return render(request, 'login.html')


def detail(request):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        district = request.POST['district']
        branch = request.POST['branch']
        account = request.POST['account']
        material = request.POST['material']
        user = Detail(name=name, dob=dob, age=age, gender=gender, phone=phone, email=email,address=address,district=district,branch=branch,account=account,material=material)
        user.save()
        return redirect('form')

    else:
        return render(request, 'detail.html')


def new(request):
    return render(request, 'new.html')


def form(request):
    return render(request, 'form.html')


def logout_user(request):
    auth.logout(request)
    return redirect('home')
