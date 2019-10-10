from django.db import models
import users.models as users
import medline.models as medline
from multiselectfield import MultiSelectField
import datetime



class consult(models.Model):
    symptoms_choices = [
        ('a1', '복통'),
        ('a2', '외상'),
        ('a3', '두통'),
        ('a4', '어지로움'),
        # go on...
    ]

    status_choices = [
        ('wait', '상담 예정'),
        ('done', '상담 완료'),
        ('expire', '기간 만료')
    ]

    reservetime_choices = [
        ('08:05:00', '아침시간'),
        ('09:20:00', '1교시 후'),
        ('10:20:00', '2교시 후'),
        ('11:20:00', '3교시 후'),
        ('12:20:00', '4교시 후'),
        ('13:20:00', '5교시 후'),
        ('14:10:00', '점심시간'),
        ('15:10:00', '6교시 후'),
        ('16:10:00', '7교시 후'),
        # etc...
    ]


    # CASCADE means that all of an user's consulting history will be deleted upon deletion of the user
    user = models.ForeignKey(users.CustomUser, on_delete=models.CASCADE)

    title = models.CharField(max_length=100, default='', blank=False)
    message = models.TextField(blank=False)
    added_datetime = models.DateTimeField(auto_now_add=True, blank=False)
    reserve_date = models.DateField(blank=False, default=datetime.datetime.now)
    reserve_time = models.TimeField(blank=False, choices=reservetime_choices, default=datetime.datetime.now)

    #status = models.CharField(max_length=5, choices=status_choices)

    image = models.ImageField(upload_to="consult_image", blank=True, default="consult_image/notfound.png")
    symptoms = MultiSelectField(choices=symptoms_choices, blank=False, max_choices=5, max_length=30)
    is_finished = models.BooleanField(default=False)
    #def update(self):
        # logic to update the status only for objects that need to have its `status` updated
    def __str___(self):
        return self.title

