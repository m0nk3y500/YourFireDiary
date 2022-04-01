from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

class FFDiary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stichwort = models.CharField(max_length=20)
    create_at = models.DateTimeField(default=timezone.now)
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)
    content = models.CharField(max_length=200)
