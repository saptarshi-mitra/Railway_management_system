from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #redirect to right place
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup_page.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            #redirect to correct place
            return redirect('accounts:login')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login_page.html', {'form': form})


def logout_page(request):
    if request.method == 'POST':
        logout(request)
    return redirect(request, 'accounts:login')
