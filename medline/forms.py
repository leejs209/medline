from django import forms
from medline.models import consult
from medicalhub.models import MedicineType


class ConsultForm(forms.ModelForm):
    class Meta:
        model = consult
        fields = ['symptoms', 'reserve_date', 'reserve_time', 'title', 'message', 'image']
        labels = {
            'symptoms': '증상',
            'title': '제목',
            'message': '내용',
            'image': '사진 첨부',
            'reserve_date': '상담 날짜',
            'reserve_time': '상담 시간',
        }

    field_order = ['symptoms', 'reserve_date', 'reserve_time', 'title', 'message', 'image']
