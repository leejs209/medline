from django.shortcuts import render, redirect, get_object_or_404
from medline.models import consult, PrescribedMedicine
from medicalhub.models import MedicineType
from django.contrib import messages
from django.http import HttpResponse
from .forms import MedicineTypeForm, PrescriptionForm
from users.models import CustomUser
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    name = '예정된 상담'
    tab='pending'
    if not request.user.is_superuser:
        messages.error(request, "권한이 없습니다")
        return redirect('home')
    consulthistory = consult.objects.filter(is_finished=False, prescription_exists=False).order_by('reserve_date')
    return render(request, 'medicalhub/consult.html', {'title': name, 'history': consulthistory, 'tab': tab})

def ongoing(request):
    name = '진행 중인 상담'
    tab='ongoing'
    if not request.user.is_superuser:
        messages.error(request, "권한이 없습니다")
        return redirect('home')
    consulthistory = consult.objects.filter(is_finished=False, prescription_exists=True).order_by('reserve_date')
    return render(request, 'medicalhub/consult.html', {'title': name, 'history': consulthistory, 'tab': tab})

def finished(request):
    name = '완료된 상담'
    tab='finished'
    if not request.user.is_superuser:
        messages.error(request, "권한이 없습니다")
        return redirect('home')
    consulthistory = consult.objects.filter(is_finished=True).order_by('reserve_date')
    return render(request, 'medicalhub/consult.html', {'title': name, 'history': consulthistory, 'tab': tab})

def details(request, pk):
    chosen_consult = consult.objects.get(pk=pk)
    prescription_queryset = PrescribedMedicine.objects.filter(consult=chosen_consult)
    if request.user.is_superuser:
        return render(request, 'medicalhub/details.html', {'consult': chosen_consult, 'prescription': prescription_queryset})
    messages.error(request, "관리자가 아니므로 접근이 거부됩니다.")
    return redirect('login')


def medicine_type_form(request):
    name = '약 등록'
    form = MedicineTypeForm()
    if not request.user.is_superuser:
        messages.error(request, "권한이 없습니다")
        return redirect('login')
    return render(request, 'medicalhub/medicine_type_form.html', {'title': name, 'form': form})


def get_medicine_type_form(request):
    if request.method == "POST":
        if not request.user.is_superuser:
            messages.error(request, "권한이 없습니다")
            return redirect('login')
        form = MedicineTypeForm(request.POST)
        if form.is_valid():
            # add to the `consult` model
            added_medicinetype = form.save()
            added_medicinetype_queryset = MedicineType.objects.get(pk=added_medicinetype.pk)
            return redirect('/medicalhub/medicine-type-details/%s' % added_medicinetype_queryset.pk)
        else:
            messages.error(request, "잘못된 입력입니다")
    else:
        messages.error(request, "잘못 들어오셨어요")
    return redirect('home')


def delete_medicine_type(request, pk):
    chosen_medicine_type = MedicineType.objects.get(pk=pk)
    if request.method == "POST":
        if request.user.is_superuser:
            chosen_medicine_type.delete()
            return redirect('medicine_type_list')
        else:
            messages.error(request, "권한이 없습니다")
    else:
        messages.error(request, "잘못 들어오셨어요")
    return redirect('home')


def medicine_type_list(request):
    name = '약 목록'
    medicine_type = MedicineType.objects.all()
    if not request.user.is_superuser:
        messages.error(request, "권한이 없습니다")
        return redirect('home')
    return render(request, 'medicalhub/medicine_type_list.html', {'title': name, 'medicine_type': medicine_type})


def medicine_type_details(request, pk):
    chosen_medicine_type = MedicineType.objects.get(pk=pk)
    if request.user.is_superuser:
        return render(request, 'medicalhub/medicine_type_details.html', {'medicine_type': chosen_medicine_type})
    messages.error(request, "관리자가 아니므로 접근이 거부됩니다.")
    return redirect('login')


def prescription_form(request, consult_pk):
    name = '처방 등록'
    consult_obj = get_object_or_404(consult, pk=consult_pk)
    form = PrescriptionForm({'consult': consult_obj})
    if not request.user.is_superuser:
        messages.error(request, "권한이 없습니다")
        return redirect('login')
    return render(request, 'medicalhub/prescription_form.html', {'title': name, 'form': form})

def get_prescription_form(request):
    if request.method == "POST":
        if not request.user.is_superuser:
            messages.error(request, "권한이 없습니다")
            return redirect('login')
        form = PrescriptionForm(request.POST)
        if form.is_valid() and request.user.is_superuser:
            added_prescription = form.save()
            prescription_object = PrescribedMedicine.objects.get(pk=added_prescription.pk)
            consult.objects.filter(pk=prescription_object.consult.pk).update(prescription_exists=True)
            return redirect('/medicalhub/details/%s' % prescription_object.consult.pk)
        else:
            messages.error(request, "잘못된 입력입니다")
    else:
        messages.error(request, "잘못 들어오셨어요")
    return redirect('home')

def search_by_username(request, username):
    name = username + ' 검색 결과'
    no_matching_user = False
    user = None

    try:
        user = CustomUser.objects.get(username=username)
    except ObjectDoesNotExist:
        no_matching_user = True
    consulthistory = consult.objects.filter(user=user).order_by('reserve_date')


    if not request.user.is_superuser:
        messages.error(request, "권한이 없습니다")
        return redirect('home')
    return render(request, 'medicalhub/search-by-username.html', {'title': name, 'history': consulthistory, 'no_matching_user': no_matching_user})