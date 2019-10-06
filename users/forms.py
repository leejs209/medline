from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('grade', 'division', 'studentno', 'name', 'barcode', 'username')

    field_order = ['grade', 'division', 'studentno', 'name', 'barcode', 'username']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = {'username', 'email'}

