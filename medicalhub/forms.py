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
        fields = ['medicine', 'schedule', 'consult']
