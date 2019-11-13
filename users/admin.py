from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
import medline.models as medline
import medicalhub.models as medicalhub


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(medline.consult)
admin.site.register(medline.PrescribedMedicine)
admin.site.register(medicalhub.MedicineType)