from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
   
    is_admin=models.BooleanField('Admin', default=False)
    is_appstaff=models.BooleanField('AppStaff', default=False)
    is_rep=models.BooleanField('OutsideRep', default=False)
    
    class Meta:
        permissions = (
            ('is_admin','Admin'),
            ('is_appstaff','AppStaff'),
            ('is_rep','OutsideRep')
           )
