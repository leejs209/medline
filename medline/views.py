from django.shortcuts import render, redirect, get_object_or_404
from .models import consult
from .forms import ConsultForm
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse, Http404

from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from users.models import CustomUser as User
from django.views.decorators.csrf import csrf_exempt
import json


def home(request):
    name = '홈'
    return render(request, 'medline/home.html', {'title': name})


def contact(request):
    name = '연락처'
    return render(request, 'medline/contact.html', {'title': name})


def consultform(request):
    name = '상담신청'
    form = ConsultForm()
    if not request.user.is_authenticated:
        messages.error(request, "로그인이 필요합니다.")
        return redirect('login')
    return render(request, 'medline/consultform.html', {'title': name, 'form': form})


def finished_consult(request):
    name = '상담내역'
    userid = request.user.id
    if not request.user.is_authenticated:
        messages.error(request, "로그인이 필요합니다.")
        return redirect('login')
    consulthistory = consult.objects.filter(user=request.user, is_finished=True)
    return render(request, 'medline/finished_consult.html', {'userid': userid, 'title': name, 'history': consulthistory})


def pending_consult(request):
    name = '상담내역'
    userid = request.user.id
    if not request.user.is_authenticated:
        messages.error(request, "로그인이 필요합니다.")
        return redirect('login')
    history = consult.objects.filter(user=request.user, is_finished=False, prescription_exists=False).order_by('reserve_date')
    return render(request, 'medline/pending_consult.html', {'userid': userid, 'title': name, 'history': history})


def ongoing_consult(request):
    name = '상담내역'
    if not request.user.is_authenticated:
        messages.error(request, "로그인이 필요합니다.")
        return redirect('login')
    history = consult.objects.filter(user=request.user,is_finished=False, prescription_exists=True).order_by('reserve_date')
    return render(request, 'medline/ongoing_consult.html', { 'title': name, 'history': history})


def finish_consult(request, pk):
    if request.method == "POST":
        if request.user.is_superuser:
            consult.objects.filter(pk=pk).update(is_finished=True)
            return redirect('/medicalhub/details/%s' % pk)
        else:
            messages.error(request, "관리자가 아니므로 접근이 거부됩니다.")
    else:
        messages.error(request, "잘못 들어오셨어요")

    return redirect('home')


def get_consultform(request):
    if request.method == "POST":
        form = ConsultForm(request.POST, request.FILES)
        if form.is_valid():
            # add to the `consult` model
            added_consult = form.save(commit=False)
            now = timezone.now().date()
            if added_consult.reserve_date >= now:
                added_consult.user = request.user
                added_consult.image = form.cleaned_data['image']
                added_consult.save()
                messages.success(request, '상담이 신청되었습니다')
                consult_details = consult.objects.get(pk=added_consult.pk)
                return redirect('/consult/details/%s' % consult_details.pk)
            messages.error(request, "과거로는 상담을 신청할 수 없습니다!")
        else:
            messages.error(request, "잘못된 입력입니다")
    else:
        messages.error(request, "잘못 들어오셨어요")
    return redirect('home')


def details(request, pk):
    chosen_consult = get_object_or_404(consult, pk=pk)
    if chosen_consult.user == request.user:
        return render(request, 'medline/details.html', {'consult': chosen_consult, 'title': chosen_consult.title})
    messages.error(request, "상담을 신청하신 분이 아니므로 접근이 거부됩니다.")
    return redirect('login')


def delete_consult(request, pk):
    chosen_consult = consult.objects.get(pk=pk)
    if request.method == "POST":
        if (chosen_consult.user == request.user and not chosen_consult.is_finished) or request.user.is_superuser:
            chosen_consult.delete()
            return redirect('operation_complete')
        else:
            messages.error(request, "권한이 없습니다.")
    else:
        messages.error(request, "잘못 들어오셨어요")
    return redirect('home')


def operation_complete(request):
    return render(request, 'medline/operation_complete.html')


def undo_finish_consult(request, pk):
    if request.method == "POST":
        if (request.user.is_superuser):
            consult.objects.filter(pk=pk).update(is_finished=False)
            return redirect('/medicalhub/details/%s' % pk)
        else:
            messages.error(request, "관리자가 아니므로 접근이 거부됩니다.")
    else:
        messages.error(request, "잘못 들어오셨어요")
    return redirect('home')

# make a custom edit page if enough time
# def edit_consult(request, pk):
#    instance = get_object_or_404(consult, pk=pk)
#    form = ConsultForm(request.POST, instance=instance)
#    if form.is_valid():
#        form.save()
#        return redirect('')
#    return render(request, 'medline/consultform.html', {'form': form})
