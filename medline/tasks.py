from __future__ import absolute_import, unicode_literals
from celery import shared_task
import medline.models as medline
from users.models import CustomUser
from django.core.exceptions import ObjectDoesNotExist
from webpush import send_user_notification

payload = {"head": "Welcome!", "body": "Hello World"}

send_user_notification(user=user, payload=payload, ttl=1000)

@shared_task
def morning_notification():
    user = CustomUser.objects.all()
    for x in user:
        try:
            medicine = medline.PrescribedMedicine.objects.filter(schedule__icontains='아침', consult__user=x)
            message = 'Medline - '
            for y in medicine:
                message += medicine.name
                message += ' '
                message += medicine.number_of_pills
                message += '개, '
            message += '를 복용하세'
            if len(message.encode('utf-8')) > 80
        except ObjectDoesNotExist:
            pass