from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # ✅ Added for showing form validation messages
from .forms import RegisterForm, LoginForm  # ✅ Import the new forms
from django.shortcuts import render

# Static pages
def home(request):
    return render(request, 'aboutpage.html')  # or 'home.html'

def aboutpage(request):
    return render(request, 'aboutpage.html')

def blogpage(request):
    return render(request, 'blogpage.html')

def change_address(request):
    return render(request, 'change_address.html')

def write_letter(request):
    return render(request, 'write_letter.html')

def write_letter2(request):
    return render(request, 'write_letter2.html')

def write_letter3(request):
    return render(request, 'write_letter3.html')

def write_letter4(request):
    return render(request, 'write_letter4.html')

# Auth Views
# Register View using RegisterForm
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('dashboard')  # Change 'dashboard' to the appropriate page
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login View using LoginForm
def login_view(request):  # This is your login page view
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Change 'dashboard' to the appropriate page
        else:
            messages.error(request, "Login failed. Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Change 'dashboard' to your actual success URL name
        else:
            messages.error(request, 'Invalid username or password')  # ✅ Added message feedback
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def custom_logout(request):
    logout(request)
    return redirect('login')

# application1/views.py
from django.shortcuts import render

def register(request):
    return render(request, 'register.html')


def dashboard_view(request):
    # Your view logic here
    return render(request, 'dashboard.html')

def register(request):
    if request.method == 'POST':  # If the form has been submitted
        form = UserCreationForm(request.POST)  # Create form with the submitted data
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the new user
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()  # Create an empty form if it's a GET request

    return render(request, 'register.html', {'form': form})  # Pass the form to the template
