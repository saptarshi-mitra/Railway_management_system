from django.shortcuts import render, redirect
from .forms import NameForm


def home_page(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # search db
            return render(request, 'accounts/login', {'form': form})
    else:
        form = NameForm()
    return render(request, 'train/home_page.html', {'form': form})
