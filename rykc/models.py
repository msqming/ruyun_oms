from django.db import models


class CommInfo(models.Model):
    """用户管理"""
    xinghao = models.CharField(max_length=32, null=False)
    pinglei = models.CharField(max_length=68, null=False)
    new_old = models.CharField(max_length=16, null=False)
    dingwei = models.CharField(max_length=64, null=False)
    pingming = models.CharField(max_length=128, null=False)
    cpu = models.CharField(max_length=16, null=False)
    xianka = models.CharField(max_length=64, null=False)
    neicun = models.CharField(max_length=32, null=False)
    ssd = models.CharField(max_length=64, null=False)
    hhd = models.CharField(max_length=64,null=False)
    model_name = models.CharField(max_length=128,null=True)
    config = models.TextField(null=True)
    pn = models.CharField(max_length=16, null=True)
