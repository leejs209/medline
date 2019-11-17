from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
import datetime
import users.models as users
import medicalhub.models as medicalhub

class consult(models.Model):
    symptoms_choices = [
        ('a1', '복통'),
        ('a2', '외상'),
        ('a3', '두통'),
        ('a4', '어지로움'),
        # go on...
    ]
    reservetime_choices = [
        ('bf', '아침시간'),
        ('a1', '1교시 후'),  # after 1, 2, ...
        ('a2', '2교시 후'),
        ('a3', '3교시 후'),
        ('a4', '4교시 후'),
        ('a5', '5교시 후'),
        ('lu', '점심시간'),
       ('a6', '6교시 후'),
        ('a7', '7교시 후'),
        # etc...
    ]

    user = models.ForeignKey(users.CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default='', blank=False)
    message = models.TextField(blank=False)
    added_datetime = models.DateTimeField(auto_now_add=True, blank=False)
    reserve_date = models.DateField(blank=False, default=timezone.now)
    reserve_time = models.CharField(blank=False, choices=reservetime_choices, default='a1', max_length=2)

    image = models.ImageField(upload_to="consult_image", blank=True, default="consult_image/notfound.png")
    symptoms = MultiSelectField(choices=symptoms_choices, blank=True, max_length=300)
    is_finished = models.BooleanField(default=False)
    prescription_exists = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def shortened_message(self):
        limit = 30
        if len(self.message) <= limit:
            return self.message
        return self.message[0:limit] + '...'


class PrescribedMedicine(models.Model):
    schedule_choices = [
        ('morning', '아침'),
        ('lunch', '점심'),
        ('dinner', '저녁'),
    ]

    number_of_pills = models.SmallIntegerField(default=0)
    #todo: 약 몇개인지 details에서 보여주기
    medicine = models.ForeignKey(medicalhub.MedicineType, on_delete=models.CASCADE)
    schedule = MultiSelectField(choices=schedule_choices, blank=True, max_length=300)
    consult = models.ForeignKey(consult, on_delete=models.CASCADE, null=True, blank=True)