from django.db import models
import users.models as users
import medline.models as medline
from multiselectfield import MultiSelectField
import datetime



class consult(models.Model):
    symptoms_choices = [
        ('a1', 'First Symptom'),
        ('a2', 'Second Symptom'),
        ('a3', 'Third Symptom'),
        ('a4', 'Fourth Symptom'),
        # go on...
    ]

    status_choices = [
        ('wait', '상담 예정'),
        ('done', '상담 완료'),
        ('expire', '기간 만료')
    ]

    # CASCADE means that all of an user's consulting history will be deleted upon deletion of the user
    user = models.ForeignKey(users.CustomUser, on_delete=models.CASCADE)

    title = models.CharField(max_length=100, default='제목없음')
    message = models.CharField(max_length=3000)
    added_datetime = models.DateTimeField(auto_now_add=True, blank=False)
    reserve_datetime = models.DateTimeField(blank=False, default=datetime.datetime.now)
    #status = models.CharField(max_length=5, choices=status_choices)

    image = models.ImageField(upload_to="consult_image", blank=True, default="consult_image/notfound.png")
    symptoms = MultiSelectField(choices=symptoms_choices, blank=False, max_choices=5, max_length=30)

    #def update(self):
        # logic to update the status only for objects that need to have its `status` updated
    def __str___(self):
        return self.title

    def is_expired(self):
        if datetime.now() >= self.reserve_datetime:
            return True
        return False

class pendingConsult(models.Model):
    consult = models.ForeignKey(medline.consult, on_delete=models.CASCADE)
    done = models.BooleanField()
