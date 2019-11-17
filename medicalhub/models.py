from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
import medline.models as medline
import users.models as users


class MedicineType(models.Model):
    name = models.CharField(max_length=100, blank=False, default="")
    description = models.TextField(blank=True, default="")
    code = models.CharField(max_length=10, blank=False)  # max_length is arbitrary; find out what is proper

    def __str__(self):
        return self.name

    @property
    def shortened_description(self):
        limit = 60
        if len(self.description) <= limit:
            return self.description
        return self.description[0:limit] + '...'