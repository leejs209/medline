from django.shortcuts import render, redirect
from .models import consult
from .forms import ConsultForm
from django.contrib import messages
from django.urls import reverse
import datetime
from django.utils import timezone
from django.http import HttpResponse

def home(request):
    name = '홈'
    userid = request.user.id

    return render(request, 'medline/home.html', {'userid': userid, 'title': name})


def contact(request):
    name = '연락처'
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
    consulthistory = consult.objects.filter(user=userid, is_finished=True)
    if not request.user.is_authenticated:
        messages.error(request, "로그인이 필요합니다.")
        return redirect('login')
    return render(request, 'medline/finished_consult.html',
                  {'userid': userid, 'title': name, 'history': consulthistory})


def pending_consult(request):
    name = '상담내역'
    userid = request.user.id
    consulthistory = consult.objects.filter(user=userid, reserve_date__gt=timezone.now(),
                                            is_finished=False)
    if not request.user.is_authenticated:
        messages.error(request, "로그인이 필요합니다.")
        return redirect('login')
    return render(request, 'medline/pending_consult.html', {'userid': userid, 'title': name, 'history': consulthistory})


def expired_consult(request):
    name = '상담내역'
    userid = request.user.id
    history = consult.objects.filter(user=userid, reserve_date__lte=timezone.now(),
                                            is_finished=False)
    if not request.user.is_authenticated:
        messages.error(request, "로그인이 필요합니다.")
        return redirect('login')
    return render(request, 'medline/expired_consult.html', {'userid': userid, 'title': name, 'history': history})


def get_consultform(request):
    if request.method == "POST":
        form = ConsultForm(request.POST, request.FILES)
        if form.is_valid():
            # add to the `consult` model
            added_consult = form.save(commit=False)
            added_consult.user = request.user
            added_consult.image = form.cleaned_data['image']
            added_consult.save()
            messages.success(request, '상담이 신청되었습니다')
            consult_details = consult.objects.get(pk=added_consult.pk)
            return redirect('/consult/details/%s' % (consult_details.pk))
            #todo: redirect after showing message
    else:
        messages.error(request, "잘못 들어오셨어요")
    return redirect('home')


def details(request, pk):
    userid = request.user.id
    chosen_consult = consult.objects.get(pk=pk)
    if not chosen_consult.user == request.user:
        messages.error(request,"상담을 신청하신 분이 아니므로 접근이 거부됩니다.")
        return redirect('login')
    return render(request, 'medline/details.html', {'userid': userid, 'consult': chosen_consult})

def emergency(request):
    pass