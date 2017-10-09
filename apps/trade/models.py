from django.db import models

# from users.models import UserProfile
#此函数能够直接获取到用户认证表，所以也就不需要直接指定UserProfile.这样也就做到了解藕
from django.contrib.auth import get_user_model
from goods.models import Goods
# Create your models here.

#此处获取到了UserProfile类
User = get_user_model()

class ShoppingCart(models.Model):
    """
        购物车
    """
    user = models.ForeignKey(User,verbose_name="用户")
    goods = models.ForeignKey(Goods,verbose_name="商品")
    goods_num = models.IntegerField(default=0,verbose_name="购买数量")

    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s(%d)"%(self.goods.name,self.goods_num)

class OrderInfo(models.Model):
    """
        订单
    """
    ORDER_STATUS = (
        ("success","支付成功"),
        ("cancel","取消"),
        ("cancel","待支付"),
    )
    PAY_TYPE=(
        ("alipay","支付宝"),
        ("wechat","微信"),
    )
    user = models.ForeignKey(User,verbose_name="用户")
    order_sn = models.CharField(max_length=30,unique=True,verbose_name="订单编号")
    trade_no = models.CharField(max_length=100,unique=True,null=True,blank=True,verbose_name="")
    pay_status = models.BooleanField(choices=ORDER_STATUS,max_length=10,verbose_name="订单状态")
    post_script = models.CharField(max_length=200,verbose_name="订单留言")
    order_mount = models.FloatField(default=0.0,verbose_name="订单金额")
    pay_time = models.DateTimeField(null=True,blank=True,verbose_name="支付时间")

    #用户信息   
    address = models.CharField(max_length=100,default="",verbose_name="收货地址")
    signer_name = models.CharField(max_length=20,default="",verbose_name="签收人")
    signer_mobile = models.CharField(max_length=11,verbose_name="联系电话")


    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

class OrderGoods(models.Model):
    """
        订单的商品详情
    """
    order = models.ForeignKey(OrderInfo,verbose_name="订单信息")
    goods = models.ForeignKey(Goods,verbose_name="商品")
    goods_num = models.IntegerField(default=0,verbose_name="商品数量")

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "订单商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order.order_sn


