from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FisherMan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField("姓名", max_length=20, default="")
    phone = models.CharField("电话", max_length=11)
    email = models.EmailField("邮箱", max_length=50)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    class Meta:
        ordering = ['id']
        db_table = 'fisherman'
        verbose_name = '养殖户'
        verbose_name_plural = '养殖户'

    def __str__(self):
        return self.name

class HydroData(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField("监测时间")
    water_quality = models.CharField("水质类别", max_length=20)
    temperature = models.FloatField("水温(℃)")
    ph = models.FloatField("pH(无量纲)")
    dissolved_oxygen = models.FloatField("溶氧量(mg/L)")
    conductivity = models.FloatField("电导率(μS/cm)")
    turbidity = models.FloatField("浊度(NTU)")
    permanganate_index = models.FloatField("高锰酸盐指数(mg/L)")
    ammonia_nitrogen = models.FloatField("氨氮(mg/L)")
    total_nitrogen = models.FloatField("总氮(mg/L)")
    total_phosphorus = models.FloatField("总磷(mg/L)")
    site_condition = models.CharField("站点情况", max_length=100)

    class Meta:
        ordering = ['id']
        db_table = 'hydrodata'
        verbose_name = '水质数据'
        verbose_name_plural = '水质数据'

    def __str__(self):
        return self.water_quality
    
class Fish(models.Model):
    id = models.AutoField(primary_key=True)
    species = models.CharField("鱼种", max_length=20)
    weight = models.FloatField("重量(g)")
    length = models.FloatField("长度(cm)")
    height = models.FloatField("高度(cm)")
    width = models.FloatField("宽度(cm)")

    class Meta:
        ordering = ['id']
        db_table = 'fish'
        verbose_name = '鱼类'
        verbose_name_plural = '鱼类'

    def __str__(self):
        return self.species
    