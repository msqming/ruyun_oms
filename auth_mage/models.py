from django.db import models

class Staff(models.Model):
    """员工管理"""
    name = models.CharField(max_length=32,verbose_name='登录用户名')
    pwd = models.CharField(max_length=64,verbose_name='登录密码')