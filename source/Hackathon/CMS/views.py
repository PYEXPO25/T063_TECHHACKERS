from django.shortcuts import render, redirect
from .forms import  ComplaintForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Admin


def start(request):
    return render(request, "start.html")

def admin_dashboard(request):
    return render(request, "admin.html")

def home(request):
    return render(request, "home/home.html")

def adminlogin(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            # Check if user exists
            user = Admin.objects.get(username=username)

            # Check if password matches
            if user.password == password:  
                messages.success(request, "Login Successful!")
                return redirect("dashboard")  # Redirects to another page
            else:
                messages.error(request, "Invalid password. Try again.")

        except Admin.DoesNotExist:
            messages.error(request, "User does not exist.")

    return render(request,'adminlogin.html')

def userlogin(request):
    if request.method == 'POST':
        action = request.POST.get("action")

        if action == "login":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                # Get the username and password from the form
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                # Authenticate the user
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    # If user exists, log them in
                    login(request, user)
                    messages.success(request, "You have successfully logged in!")
                    return redirect('complaints/')  # Redirect to the next page, replace with actual URL
                else:
                    # If authentication failed
                    messages.error(request, "Invalid credentials, please try again.")
            else:
                messages.error(request, "Invalid form submission.")

        elif action == "signup":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()  # This saves the new user to the database
                messages.success(request, 'Account created successfully!')
                return redirect('complaints/')  # Redirect to login page or dashboard
            else:
                messages.error(request, 'Error: Could not create account. Please check the form.')
        
        return redirect("complaints")

    return render(request, 'userlogin.html')

def complaints_view(request):
    return render(request, 'complaint.html')

