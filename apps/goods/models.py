from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.

class GoodsCategory(models.Model):
    """
        商品类别
    """
    name = models.CharField(max_length=30,default="",verbose_name="类别名",help_text="类别名")
    code = models.CharField(max_length=30,default="",verbose_name="类别代码",help_text="类别代码")
    desc =  models.TextField(default="",verbose_name="类别描述",help_text="类别描述")

    category_type_choices = (
        (1,"一级类目"),
        (2,"二级类目"),
        (3,"三级类目"),
    )
    category_type = models.SmallIntegerField(choices=category_type_choices,verbose_name="类目级别",help_text="类目级别")
    parent_category = models.ForeignKey(to="self",verbose_name="父级商品类别",null=True,blank=True,related_name="sub_cat")
    is_tab = models.BooleanField(default=False,verbose_name="是否添加到导航栏")

    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = "商品类别"

    def __str__(self):
        return self.name

class GoodsCategoryBrand(models.Model):
    """
        商品类别中的品牌
    """
    name = models.CharField(default="",max_length=30,verbose_name="品牌名",help_text="品牌名")
    desc = models.TextField(default="",verbose_name="品牌描述",help_text="品牌描述")
    #指定图片上传的路径,ImageField字段其实在数据库就是一个char,所以需要指定长度
    image = models.ImageField(max_length=200,upload_to="brand/images/")

    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = "品牌"

    def __str__(self):
        return self.name

class Goods(models.Model):
    """
        商品
    """
    category = models.ForeignKey(to="GoodsCategory",verbose_name="商品类别")
    goods_sn = models.CharField(max_length=50,default="",verbose_name="商品编码")
    name = models.CharField(max_length=300,verbose_name="商品名")
    click_num = models.IntegerField(default=0,verbose_name="点击次数")
    sold_num = models.IntegerField(default=0,verbose_name="商品销量")
    fav_num = models.IntegerField(default=0,verbose_name="收藏数")
    goods_num = models.IntegerField(default=0,verbose_name="库存数量")
    market_price = models.IntegerField(default=0,verbose_name="市场价格")
    shop_price = models.IntegerField(default=0,verbose_name="本店价格")
    goods_brief = models.CharField(max_length=500,verbose_name="商品简短描述")
    goods_desc = UEditorField(verbose_name=u"内容",imagePath="goods/images/",width=1000
                              ,height=800,filePath="goods/files/",default="")
    ship_free = models.BooleanField(default=True,verbose_name="是否承担运费")
    goods_front_image = models.ImageField(upload_to="",null=True,blank=True,verbose_name="")
    # goods_front_image_url = models.CharField(max_length=300,default="",verbose_name="")
    is_new  = models.BooleanField(default=False,verbose_name="是否新品")
    is_hot = models.BooleanField(default=False,verbose_name="是否热销")

    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"

    def __str__(self):
        return self.name

class GoodsImage(models.Model):
    """
        商品轮播图
        说明：一个商品有多张轮播图的图片
    """
    goods = models.ForeignKey(to="Goods",verbose_name="商品",related_name="images")
    image = models.ImageField(upload_to="",verbose_name="图片",null=True,blank=True)
    image_url = models.CharField(max_length=300,null=True,blank=True,verbose_name="图片url")

    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")

    class Meta:
        verbose_name = "商品轮播图"
        verbose_name_plural = "商品轮播图"

    def __str__(self):
        self.goods.name

class Banner(models.Model):
    """
        首页轮播横幅图片
    """
    goods = models.ForeignKey(Goods,verbose_name="商品")
    image = models.ImageField(upload_to="banner",verbose_name="轮播图片")
    index = models.IntegerField(default=0,verbose_name="轮播顺序")

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = "轮播商品"
        verbose_name_plural = "轮播商品"

    def __str__(self):
        return self.goods.name

