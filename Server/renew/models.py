import uuid

from django.contrib.admin.models import LogEntry
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.utils import timezone
from datetime import timedelta, datetime


class my_methods:
    @staticmethod
    def province():
        s = (
            ('北京', '北京'),
            ('天津', '天津'),
            ('河北', '河北'),
            ('山西', '山西'),
            ('内蒙古', '内蒙古'),
            ('辽宁', '辽宁'),
            ('吉林', '吉林'),
            ('黑龙江', '黑龙江'),
            ('上海', '上海'),
            ('江苏', '江苏'),
            ('浙江', '浙江'),
            ('安徽', '安徽'),
            ('福建', '福建'),
            ('江西', '江西'),
            ('山东', '山东'),
            ('河南', '河南'),
            ('湖北', '湖北'),
            ('湖南', '湖南'),
            ('广东', '广东'),
            ('广西', '广西'),
            ('海南', '海南'),
            ('重庆', '重庆'),
            ('四川', '四川'),
            ('贵州', '贵州'),
            ('云南', '云南'),
            ('西藏', '西藏'),
            ('陕西', '陕西'),
            ('甘肃', '甘肃'),
            ('青海', '青海'),
            ('宁夏', '宁夏'),
            ('新疆', '新疆'),
        )
        return s


#  各省份规模以上企业主要能源品种产量
class MainEnergyProductionModel(models.Model):
    region = models.CharField(max_length=100, verbose_name='行政单位', choices=my_methods.province())
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000)
    raw_coal = models.DecimalField(max_digits=10, decimal_places=1, default=1.0, verbose_name='原煤', help_text='万吨')
    crude_oil = models.DecimalField(max_digits=10, decimal_places=1, default=1.0, verbose_name='原油', help_text='万吨')
    fire_power = models.DecimalField(max_digits=10, decimal_places=1, default=1.0, verbose_name='火力发电量',
                                     help_text='亿千瓦时')
    water_power = models.DecimalField(max_digits=10, decimal_places=1, default=1.0, verbose_name='水力发电量',
                                      help_text='亿千瓦时')
    wind_power = models.DecimalField(max_digits=10, decimal_places=1, default=1.0, verbose_name='风力发电量',
                                     help_text='亿千瓦时')
    sun_power = models.DecimalField(max_digits=10, decimal_places=1, default=1.0, verbose_name='太阳能发电量',
                                    help_text='亿千瓦时')
    nuclear_power = models.DecimalField(max_digits=10, decimal_places=1, default=1.0, verbose_name='核能发电量',
                                        help_text='亿千瓦时')
    all_power = models.DecimalField(max_digits=10, decimal_places=1, default=1.0, verbose_name='总发电量',
                                    help_text='亿千瓦时')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        unique_together = ('year', 'region')
        verbose_name_plural = '规模以上企业主要能源产量'

    def __str__(self):
        return f"{self.region} - {self.year} - 规模以上企业主要能源产量"


#  能源设施
class RegionalResourceFacilitiesModel(models.Model):
    region = models.CharField(max_length=100, verbose_name='行政单位', choices=my_methods.province())
    name = models.CharField(max_length=30, verbose_name='设施')
    do = models.CharField(max_length=30, verbose_name='工作')
    number = models.DecimalField(default=0, max_digits=7, decimal_places=2, verbose_name='数目')
    up = models.CharField(max_length=10, choices=(
        ('吨', '吨'),
        ('万吨', '万吨'),
        ('公顷', '公顷'),
        ('万公顷', '万公顷'),
        ('亩', '亩'),
        ('万亩', '万亩'),
        ('千瓦时', '千瓦时'),
        ('万千瓦时', '万千瓦时'),
        ('亿千瓦时', '亿千瓦时'),
    ), default='吨', verbose_name='单位')
    when = models.DateField(verbose_name='时间')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        unique_together = ('region', 'name')
        verbose_name_plural = '地区资源设施使用情况'

    def __str__(self):
        return f"{self.region} - {self.name}"


#  地区再生能源储量/产量/结构/重要再生能源排行/概况
class EnergyReserveModel(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000)
    province = models.CharField(max_length=10, verbose_name='省份', choices=my_methods.province(), default='安徽')

    wind_pro = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                   verbose_name='风能',
                                   help_text='亿千瓦时（产量）')
    water_pro = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                    verbose_name='水利',
                                    help_text='亿千瓦时（产量）')
    light_pro = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                    verbose_name='光伏',
                                    help_text='亿千瓦时（产量）')
    biomass_energy_pro = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                             verbose_name='生物质能',
                                             help_text='亿千瓦时（产量）')
    geothermal_pro = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                         verbose_name='地热',
                                         help_text='亿千瓦时（产量）')
    sea_pro = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                  verbose_name='海洋',
                                  help_text='亿千瓦时（产量）')

    wind_res = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                   verbose_name='风能',
                                   help_text='兆瓦时（储量）')
    water_res = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                    verbose_name='水利',
                                    help_text='亿千瓦时（储量）')
    light_res = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                    verbose_name='光伏',
                                    help_text='亿千瓦时（储量）')
    biomass_energy_res = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                             verbose_name='生物质能',
                                             help_text='亿千瓦时（储量）')
    geothermal_res = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                         verbose_name='地热',
                                         help_text='亿千瓦时（储量）')
    sea_res = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                  verbose_name='海洋',
                                  help_text='亿千瓦时（储量）')

    hydrogen = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                   verbose_name='氢能',
                                   help_text='亿千瓦时（产量）')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '地区能源储量/产量统计'

    def __str__(self):
        return f"{self.year}年 - {self.province}省 - 能源储量/产量统计"
