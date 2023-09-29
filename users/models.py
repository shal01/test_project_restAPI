from django.db import models
from django.contrib.auth.models import User
from django.utils.deconstruct import deconstructible
import os

@deconstructible
class Generate_profile_imagepath(object):

    def __init__(self):
        pass;

    def __str__(self,instance,filename):
        ext=filename.split('.')[-1]
        path=f'media/acccount/{instance.user.id}/image/'
        name=f'profile_image.{ext}'
        return os.path.join(path,name)

user_profile_image_path=Generate_profile_imagepath();

class Profile(models.Model):
    objects = object
    user=models.OneToOneField(User,on_delete=models.CASCADE);
    image=models.FileField(upload_to=user_profile_image_path,blank=True,null=True)

    def __str__(self):
        return f'{self.user.username}\'s profile'
