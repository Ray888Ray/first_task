from django.db import models

# Create your models here.

class CardGreeting(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')
    city = models.CharField(max_length=20, verbose_name='city')
    username = models.CharField(max_length=20, verbose_name='username')
    chat_id = models.CharField(max_length=50, blank=True, null=True, verbose_name='chat ID')
