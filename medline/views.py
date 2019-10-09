from django.shortcuts import render, redirect
from .models import consult
from .forms import ConsultForm
from django.contrib import messages
from django.urls import reverse
import datetime

def home(request):
    name = '홈'
    userid = request.user.id

    return render(request, 'medline/home.html', {'userid': userid, 'title': name})


def contact(request):
    name = '연락'
    userid = request.user.id

    return render(request, 'medline/contact.html', {'userid': userid, 'title': name})


def consultform(request):
    name = '상담신청'
    userid = request.user.id
    form = ConsultForm()
    if not request.user.is_authenticated:
        messages.error(request, "로그인이 필요합니다.")
        return redirect('login')
    return render(request, 'medline/consultform.html', {'userid': userid, 'title': name, 'form': form})


def finished_consult(request):
    name = '상담내역'
    userid = request.user.id
    consulthistory = consult.objects.filter(user=userid)
    if not request.user.is_authenticated:
        messages.error(request, "로그인이 필요합니다.")
        return redirect('login')
    return render(request, 'medline/finished_consult.html', {'userid': userid, 'title': name, 'history': consulthistory})

def pending_consult(request):
    name = '상담내역'
    userid = request.user.id
    consulthistory = consult.objects.filter(user=userid, reserve_datetime__gt = datetime.datetime.now())
    if not request.user.is_authenticated:
        messages.error(request, "로그인이 필요합니다.")
        return redirect('login')
    return render(request, 'medline/pending_consult.html', {'userid': userid, 'title': name, 'history': consulthistory})

def get_consultform(request):
    if request.method == "POST":
        form = ConsultForm(request.POST, request.FILES)
        if form.is_valid:
            # add to the `consult` model
            consult = form.save(commit=False)
            consult.user = request.user
            consult.image = form.cleaned_data['image']
            consult.save()
            messages.success(request, '상담이 신청되었습니다')
            return redirect(reverse('pending_consult'))
    else:
        messages.error(request, "잘못 들어오셨어요")
        return redirect('home')