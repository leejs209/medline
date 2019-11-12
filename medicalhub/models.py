from django.db import models
from django.utils import timezone
from multiselectfield import MultiSelectField
import medline.models as medline
import users.models as users


class MedicineType(models.Model):
    name = models.CharField(max_length=30, blank=False, default="")
    image = models.ImageField(upload_to="consult_image", blank=True, default="consult_image/notfound.png")
    description = models.TextField(blank=True, default="")
    code = models.CharField(max_length=10, blank=False)  # max_length is arbitrary; find out what is proper

    @property
    def shortened_description(self):
        limit = 30
        if len(self.description) <= limit:
            return self.description
        return self.description[0:limit] + '...'