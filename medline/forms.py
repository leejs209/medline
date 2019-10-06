from django import forms
from medline.models import consult


class ConsultForm(forms.ModelForm):
    class Meta:
        model = consult
        fields = ['symptoms', 'title', 'message', 'image']
        labels = {
            'symptoms': '증상',
            'title': '제목',
            'message': '내용',
            'image': '사진 첨부'
        }

    field_order = ['symptoms', 'title', 'message', 'image']
