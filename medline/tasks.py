from __future__ import absolute_import, unicode_literals
from celery import shared_task
import medline.models as medline
from users.models import CustomUser
from django.core.exceptions import ObjectDoesNotExist
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

def send_sms(phone, message):
    api_key = "#ENTER_YOUR_OWN#"
    api_secret = "#ENTER_YOUR_OWN#"
    print("Sending SMS...")
    ## 4 params(to, from, type, text) are mandatory. must be filled
    params = dict()
    params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
    params['to'] = phone # Recipients Number '01000000000,01000000001'
    params['from'] = '01083311390' # Sender number
    params['text'] = message # Message

    cool = Message(api_key, api_secret)
    try:
        response = cool.send(params)
        if "error_list" in response:
            print("Error List : %s" % response['error_list'])

    except CoolsmsException as e:
        print("Error Code : %s" % e.code)
        print("Error Message : %s" % e.msg)

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