from django import forms
from medline.models import consult


class ConsultForm(forms.ModelForm):
    class Meta:
        model = consult
        fields = ['symptoms', 'reserve_datetime', 'title', 'message', 'image']
        labels = {
            'symptoms': '증상',
            'title': '제목',
            'message': '내용',
            'image': '사진 첨부',
            'reserve_datetime': '예약 시간'
        }

    field_order = ['symptoms','reserve_datetime', 'title', 'message', 'image']
