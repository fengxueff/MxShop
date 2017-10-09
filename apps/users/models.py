from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    '''
        用户表
        以下字段为新增字段，其他字段如：密码字段会继承AbstractUser中的password字段
    '''
    name = models.CharField(max_length=30,null=True,blank=True,verbose_name="姓名")
    birthday = models.DateField(null=True,blank=True,verbose_name="出生年月")
    mobile = models.CharField(max_length=11,verbose_name="电话")
    gender_choices = (("male","男"),("female","女"))
    gender = models.CharField(max_length=6,choices=gender_choices,default="male",verbose_name="性别")
    email = models.CharField(max_length=100,null=True,blank=True,verbose_name="邮箱")

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.name

class VerfiyCode(models.Model):
    """
        短信验证码
    """
    code = models.CharField(max_length=10,verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = "短信验证码"

    def __str__(self):
        return self.code
