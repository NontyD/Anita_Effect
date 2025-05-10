from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@csrf_exempt  # Disable CSRF protection for this view (optional, but useful for GET requests)
def custom_logout_view(request):
    if request.method == 'GET' or request.method == 'POST':  # Allow both GET and POST
        logout(request)
        return redirect('/accounts/login/')
    return redirect('/')  # Fallback for unsupported methods

def home(request):
    return render(request, 'home.html')