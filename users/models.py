from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    grade_choices = [
        ('h1', '고1'),
        ('h2', '고2'),
        ('h3', '고3'),
        ('t', '선생님')
    ]

    division_choices = [
        ('1', '1반'),
        ('2', '2반'),
        ('3', '3반'),
        ('4', '4반'),
        ('5', '5반'),
        ('6', '6반'),
        ('7', '7반'),
        ('8', '8반'),
        ('9', '9반'),
        ('10', '10반'),
        ('11', '11반'),
        ('12', '12반'),
        ('13', '13반'),
        ('14', '14반'),
    ]
    name = models.CharField(max_length=30, blank=False, default='홍길동')
    barcode = models.CharField(max_length=50)
    grade = models.CharField(max_length=2, choices=grade_choices, blank=False, default='h1')
    division = models.CharField(max_length=2, choices=division_choices, blank=False, default='1')
    studentno = models.SmallIntegerField( default=1)

    # add profile image with models.filepath and uploads