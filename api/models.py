from django.db import models

# Create your models here.

class LocDepartment(models.Model):
    location = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)

    class Meta:
        verbose_name = "LocDepartment"

