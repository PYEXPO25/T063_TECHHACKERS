from django.shortcuts import render, redirect
from .forms import  CustomUserCreationForm, ComplaintForm, PersonalInfoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import Admin, PersonalInfo

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
            # Fetch user from the Admin model
            user = Admin.objects.get(username=username)

            # Check if the password matches the stored password
            if user.password == password:
                messages.success(request, "Login Successful!")
                return redirect("dashboard/")  # Redirect to the dashboard page
            else:
                messages.error(request, "Invalid password. Try again.")

        except Admin.DoesNotExist:
            messages.error(request, "User does not exist.")

    return render(request, 'adminlogin.html')

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
    if request.method == 'POST':
        personal_form = PersonalInfoForm(request.POST)
        complaint_form = ComplaintForm(request.POST, request.FILES)

        print("Personal Form Errors:", personal_form.errors)
        print("Complaint Form Errors:", complaint_form.errors)

        if personal_form.is_valid() and complaint_form.is_valid():
            email = personal_form.cleaned_data['email']
            personal_info, created = PersonalInfo.objects.get_or_create(
                email=email,
                defaults={
                    'full_name': personal_form.cleaned_data['full_name'],
                    'phone': personal_form.cleaned_data['phone'],
                    'gender': personal_form.cleaned_data['gender'],
                    'address': personal_form.cleaned_data['address'],
                }
            )

            # Create complaint and link it to the user
            complaint = complaint_form.save(commit=False)
            complaint.personal_info = personal_info
            complaint.save()

            print("Complaint Saved:", complaint)  # Debugging

            return redirect('track/')

    else:
        personal_form = PersonalInfoForm()
        complaint_form = ComplaintForm()

    return render(request, 'complaintpage.html', {'personal_form': personal_form, 'complaint_form': complaint_form})

def admin_login(request):
    return render(request,"adminlogin.html")

def submit_complaint(request):
    return render(request, 'error.html', {'error_message': 'Invalid request'})

def about(request):
    return render(request,"aboutus.html")
def contact(request):
    return render(request, "contactpage.html")
def track(request):
    return render(request, 'track.html')
