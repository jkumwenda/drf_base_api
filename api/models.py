from enum import auto
from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Profiles(models.Model):
    pk_profileid = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    mobile = models.CharField(max_length=20)

    class Meta:
        db_table = 'profiles'

class UserLogs(models.Model):
    pk_user_logid  = models.AutoField(primary_key=True)
    fk_userid  = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    log  = models.TextField()
    tag  = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_logs'     