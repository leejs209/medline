from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
import medline.models as medline
import users.models as users

class medicineType(models.Model):
    name = models.CharField(max_length=30, blank=False, default="")
    description = models.TextField(blank=True, default="")
    code = models.CharField(max_length = 10, blank=False)       #find out how much chars to use as max_length

class medicinePackage(models.Model):
    type = models.ForeignKey(medicineType, on_delete=models.CASCADE)
    number = models.IntegerField(blank=False)
    location = models.CharField(max_length=30)