from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User

# Landing page with buttons
def landing_page(request):
    return render(request, 'landing.html')

# Signup page
def signup_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm_password']
        role = request.POST['role']

        if password != confirm:
            return render(request, 'signup.html', {'error': "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': "Username already exists"})

        User.objects.create_user(username=username, email=email, password=password, role=role)
        return redirect('login_page')

    return render(request, 'signup.html')

# Login page
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'home.html', {'user': user})
        else:
            return render(request, 'login.html', {'error': "Invalid credentials"})

    return render(request, 'login.html')
