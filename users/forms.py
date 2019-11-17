from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('grade', 'division', 'studentno', 'name', 'birthday', 'username')
        labels = {
            'grade': '학년',
            'division': '학반',
            'studentno': '번호',
            'name': '성명',
            'birthday': '생년월일',
        }
    field_order = ['grade', 'division', 'studentno', 'name', 'birthday', 'username']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = {'username', 'email'}

