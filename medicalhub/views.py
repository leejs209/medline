from django.shortcuts import render, redirect
from medline.models import consult
from django.contrib import messages
from django.urls import reverse
import datetime
from django.http import HttpResponse

def adminpanel(request):
    name = '관리 패널'
    userid = request.user.id
    consulthistory = consult.objects.all()
    if not request.user.is_superuser:
        messages.error(request, "권한이 없습니다")
        return HttpResponse("<p>권한이 없습니다<p>")
    return render(request,'medicalhub/admin.html', {'userid': userid, 'title': name, 'history': consulthistory})