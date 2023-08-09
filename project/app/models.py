from django.db import models


# Create your models here.
class Detail(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    Phone = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=250)
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    material = models.CharField(max_length=100)

    def __str__(self):
        return self.name
