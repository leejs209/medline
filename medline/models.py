from django.db import models
import users.models as users
from multiselectfield import MultiSelectField

class consult(models.Model):
    symptoms_choices=[
        ('a1', 'First Symptom'),
        ('a2', 'Second Symptom'),
        ('a3', 'Third Symptom'),
        ('a4', 'Fourth Symptom'),
        # go on...
    ]


    # CASCADE means that all of an user's consulting history will be deleted upon deletion of the user
    user = models.ForeignKey(users.CustomUser, on_delete=models.CASCADE)

    title = models.CharField(max_length=100, default='제목없음')
    added_datetime = models.DateTimeField(auto_now_add=True, blank=False)

    message = models.TextField
    image = models.ImageField(upload_to="consult_image", blank=True)
    symptoms = MultiSelectField(choices=symptoms_choices, blank=False, max_choices=5, max_length=30)