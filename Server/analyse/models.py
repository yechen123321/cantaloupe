from django.contrib.admin.models import LogEntry
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class method:
    @staticmethod
    def region():
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


#  能源发展热力图
class HeatMapModel(models.Model):
    province = models.CharField(max_length=100, verbose_name='省级', null=True, choices=method.region(), default='安徽')
    city = models.CharField(max_length=100, verbose_name='市级', null=True)
    value = models.FloatField(verbose_name='数值', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '能源发展情况(权重)'

    def __str__(self):
        return f"{self.province}省 - {self.city}市 - 能源发展情况"


#  能源产能及结构
class CapacityStructureModel(models.Model):
    province = models.CharField(max_length=100, verbose_name='省级', null=True, choices=method.region(), default='安徽')
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000)
    wind = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                               verbose_name='风能',
                               help_text='亿千瓦时')
    water = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                verbose_name='水利',
                                help_text='亿千瓦时')
    light = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                verbose_name='光伏',
                                help_text='亿千瓦时')
    biomass = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                  verbose_name='质能',
                                  help_text='亿千瓦时')
    sea = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                              verbose_name='海洋',
                              help_text='亿千瓦时')
    hydrogen = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                   verbose_name='氢能',
                                   help_text='亿千瓦时')  # 其他

    shale_oil = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                    verbose_name='页岩油',
                                    help_text='亿吨')
    coal = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                               verbose_name='煤炭',
                               help_text='亿吨')
    petroleum = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                    verbose_name='石油',
                                    help_text='亿吨')
    natural_gas = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                      verbose_name='天然气',
                                      help_text='亿吨')
    geothermal = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                     verbose_name='地热',
                                     help_text='亿千瓦时')  # 其他

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '能源产能及结构'

    def __str__(self):
        return f"{self.province}省 - 能源产能及结构"


#  能源消耗水平
class ConsumptionModel(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000)
    province = models.CharField(max_length=100, verbose_name='省级', null=True, choices=method.region(), default='安徽')
    total_energy_consumption = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                                   verbose_name='能源消费总量',
                                                   help_text='万吨标准煤')
    coal = models.DecimalField(max_digits=3, decimal_places=1, default=1.0,
                               verbose_name='煤炭占比',
                               help_text='%')
    petroleum = models.DecimalField(max_digits=3, decimal_places=1, default=1.0,
                                    verbose_name='石油占比',
                                    help_text='%')
    natural_gas = models.DecimalField(max_digits=3, decimal_places=1, default=1.0,
                                      verbose_name='天然气占比',
                                      help_text='%')
    power_and_other = models.DecimalField(max_digits=3, decimal_places=1, default=1.0,
                                          verbose_name='一次电力及其他能源',
                                          help_text='%')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '能源消耗水平'

    def __str__(self):
        return f"{self.year}年 - 能源消耗水平"
