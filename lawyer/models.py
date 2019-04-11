# coding=utf-8
__author__ = 'yy'

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
# import datetime

#律师事务所
class Law(models.Model):
    name = models.CharField(verbose_name='名称', max_length=50)
    f_name = models.CharField(verbose_name='法定代表人', max_length=20, blank=True,null=True)
    tel = models.IntegerField(verbose_name='电话', blank=True,null=True)
    usernames=models.CharField(verbose_name='开户行',max_length=50,blank=True,null=True)
    card=models.CharField(verbose_name='账号',max_length=50,blank=True,null=True)
    address = models.CharField(verbose_name='地址', max_length=250, blank=True)
    enter_date = models.DateField(verbose_name='创建时间', auto_now_add=True, auto_now=False)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '律师事务所'
        verbose_name_plural = '律师事务所'

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User,verbose_name='律师名称')
    law = models.ForeignKey(Law,verbose_name=u'律师事务所', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='lawe')
    tel = models.CharField(verbose_name='电话',max_length=20,blank=True, null=True)
    address = models.CharField(verbose_name='地址', max_length=500, blank=True, null=True)
    code = models.CharField(verbose_name='身份证号', max_length=500, blank=True, null=True)



    class Meta:
        verbose_name = '律师'
        verbose_name_plural = '律师'

    def __str__(self):
        return '1111'

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)


post_save.connect(create_user_profile, sender=User)