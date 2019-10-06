from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth import login

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            signed_up = CustomUser.objects.create_user(**form.cleaned_data)
            login(request, signed_up)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
        return render(request, 'registration/signup.html', {'form': form})
# Create your views here.


def login(request):
    name = '로그인'
    userid = request.user.id
    return render(request, 'registration/login.html', {'userid': userid, 'title': name})

