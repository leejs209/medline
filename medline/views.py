from django.shortcuts import render, redirect
from .models import consult

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

    return render(request, 'medline/consultform.html', {'userid': userid, 'title': name})

def consulthistory(request):
    name = '상담내역'
    userid = request.user.id
    consulthistory = consult.objects.filter(user=userid)

    return render(request, 'medline/consulthistory.html', {'user': userid, 'title': name, 'history': consulthistory})
