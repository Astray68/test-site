from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/signup.html', {'form': form})
