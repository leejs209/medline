from django.shortcuts import render, redirect
from medline.models import consult
from django.contrib import messages
from django.http import HttpResponse

def home(request):
    name = '관리 패널'
    userid = request.user.id
    consulthistory = consult.objects.all().order_by('reserve_date')
    if not request.user.is_superuser:
        messages.error(request, "권한이 없습니다")
        return redirect('home')
    return render(request, 'medicalhub/admin.html', {'userid': userid, 'title': name, 'history': consulthistory})

def details(request, pk):
    userid = request.user.id
    chosen_consult = consult.objects.get(pk=pk)
    if request.user.is_superuser:
        return render(request, 'medicalhub/details.html', {'userid': userid, 'consult': chosen_consult})
    messages.error(request, "관리자가 아니므로 접근이 거부됩니다.")
    return redirect('login')
