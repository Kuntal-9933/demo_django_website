from django.db import models


# Create your models here.
class Contact(models.Model):

    email=models.CharField(max_length=122,unique=True)
    password=models.CharField(max_length=122,default=0)
    date=models.DateField()

    def __str__(self) -> str:
        return self.email