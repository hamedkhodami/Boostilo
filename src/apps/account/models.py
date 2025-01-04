from django.db import models
from apps.core.models import BaseModel
from django.contrib.auth.models import User
from .enums import UserRole
from .managers import ActiveUserManager
# Create your models here.

class ProfileTeam(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    fullname = models.CharField(max_length=50,verbose_name="Full Name")
    role = models.CharField(max_length=150,choices=[(role.value,role.name.capitalize())
                                                    for role in UserRole]
                            ,verbose_name="Role")
    bio = models.TextField(verbose_name="Biography")
    photo = models.ImageField(upload_to='images/profiles/',null=True,blank=True,verbose_name="Profile Photo")


    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class ClientModel(models.Model):
    fullname = models.CharField(max_length=150,verbose_name='Full Name')
    jobs = models.CharField(max_length=150,verbose_name='Job Title')
    email = models.EmailField(unique=True,verbose_name='Email Address')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Creation Date')

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

class AccessControl(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='access_control')
    is_active = models.BooleanField(default=True,verbose_name='Active Status')
    can_edit = models.BooleanField(default=False,verbose_name='Can Edit Content')
    can_delete = models.BooleanField(default=False,verbose_name='Can Delete Content')
    is_superuser = models.BooleanField(default=False,verbose_name='Superuser Status')

    objects = ActiveUserManager()

    class Meta:
        verbose_name = 'Access Control'
        verbose_name_plural = 'Access Controls'