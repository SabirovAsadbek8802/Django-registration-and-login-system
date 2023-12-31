from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN='ADMIN','ADMIN'


    base_role=Role.ADMIN

    role=models.CharField(max_length=10,choices=Role.choices)

    def save(self,*args,**kwargs):
        if not self.pk:
            self.role=self.base_role
            return super().save(*args,**kwargs)
