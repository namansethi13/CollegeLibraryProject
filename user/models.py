from django.db import models
from django.dispatch import receiver 
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.validators import validate_image_file_extension


class Profile (models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    about=models.CharField(max_length=200,blank=True)
    image=models.ImageField(default='default.jpeg',upload_to='Profile_Pics',blank=True,null=True,validators=[validate_image_file_extension])


    def __str__(self):
        return str(self.user)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()    

