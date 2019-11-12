from django.shortcuts import render, redirect
from medline.models import consult
from medicalhub.models import MedicineType
from django.contrib import messages
from django.http import HttpResponse
from .forms import MedicineTypeForm

def home(request):
    name = '관리 패널'
    consulthistory = consult.objects.all().order_by('reserve_date')
    if not request.user.is_superuser:
        messages.error(request, "권한이 없습니다")
        return redirect('home')
    return render(request, 'medicalhub/admin.html', {'title': name, 'history': consulthistory})

def details(request, pk):
    chosen_consult = consult.objects.get(pk=pk)
    if request.user.is_superuser:
        return render(request, 'medicalhub/details.html', {'consult': chosen_consult})
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
        form = MedicineTypeForm(request.POST, request.FILES)
        if form.is_valid():
            # add to the `consult` model
            added_medicinetype = form.save(commit=False)
            added_medicinetype.image = form.cleaned_data['image']
            added_medicinetype.save()
            added_medicinetype_queryset = consult.objects.get(pk=added_medicinetype.pk)
            return redirect('/medicalhub/medicine-type-details/%s' % added_medicinetype_queryset.pk)
        else:
            messages.error(request, "잘못된 입력입니다")
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