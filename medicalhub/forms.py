from django import forms
from medicalhub.models import MedicineType
from medline.models import PrescribedMedicine


class MedicineTypeForm(forms.ModelForm):
    class Meta:
        model = MedicineType
        fields = ['name', 'description', 'code', 'image']
        labels = {
            'name': '이름',
            'description': '설명',
            'code': '약 코드',
            'image': '사진'

        }

    field_order = ['name', 'description', 'code', 'image']


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = PrescribedMedicine
        fields = ['medicine', 'schedule', 'consult', 'number_of_pills']
        labels = {
            'medicine': '약 종류',
            'schedule': '복용 시간',
            'number_of_pills': '복용할 약의 개수',
            'consult': '처방할 상담의 제목',
        }
    field_order = ['medicine', 'schedule', 'number_of_pills']