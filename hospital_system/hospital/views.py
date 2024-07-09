from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('hospital:dashboard')
            '''if user is not None:
                login(request, user)
                messages.success(request, f' we'come {user.username} !!')
                return redirect('hospital:dashboard', username=user.username)
            else:
                messages.info(request, f'account done not exit plz sign in')'''
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard(request):
    # user = get_object_or_404(CustomUser, username=username)
    return render(request, 'registration/dashboard.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('hospital:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('hospital:login')
