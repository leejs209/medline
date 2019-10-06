from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth import login
from django.contrib import messages

def signup(request):
    name = '회원가입'
    userid = request.user.id
    if userid != None:
        return redirect('home')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "가입에 성공하였습니다. 로그인해 주십시오.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'userid': userid, 'title': name})


def login(request):
    name = '로그인'
    userid = request.user.id
    return render(request, 'registration/login.html', {'userid': userid, 'title': name})