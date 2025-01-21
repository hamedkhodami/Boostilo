from django.db import models
from apps.core.models import BaseModel
from django.contrib.auth.models import User
from .enums import UserRole


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

    def get_image(self):
        if self.images:
            return self.images.url
        return '/static/assets/public/images/logo.png' # TODO: should change image


