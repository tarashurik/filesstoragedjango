# from django.db import models
# from django.contrib.auth.models import User
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='Пользователь')
#     tel = models.CharField(max_length=12, null=True, blank=True, verbose_name='Телефон')
#     city = models.CharField(max_length=20, null=True, blank=True, verbose_name='Город')
#     is_verificated = models.BooleanField(default=False, verbose_name='Верифицирован')
#     news_count = models.IntegerField(default=0, verbose_name='Количество новостей')
