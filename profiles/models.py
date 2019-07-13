from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, related_name="profile",
                                verbose_name='Пользователь', on_delete=models.CASCADE)
    email = models.EmailField(
        null=True, blank=True, unique=True, verbose_name='Email')
    last_activity= models.DateTimeField(
        default=timezone.now, blank=True, verbose_name='Activity')
    avatar = models.ImageField(
        upload_to='profiles/list', blank=True, verbose_name='Аватар')
