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

    @staticmethod
    def province_dict():
        s = {
            '北京': [
                '石景山', '房山', '通州', '顺义', '昌平', '大兴', '怀柔', '平谷', '延庆', '密云', '西城', '海淀',
                '朝阳', '丰台', '门头沟'
            ],
            '浙江': [
                '杭州', '宁波', '温州', '绍兴', '湖州', '嘉兴', '金华', '衢州', '台州', '丽水', '舟山'
            ],
            '重庆': [
                '渝中', '大渡口', '江北', '南岸', '北碚', '巴南', '九龙坡', '南川', '江津', '永川', '合川', '綦江',
                '潼南', '铜梁', '万盛'
            ],
            '西藏': [
                '拉萨', '昌都', '日喀则'],
            '四川': [
                '成都', '绵阳', '自贡', '攀枝花', '泸州', '德阳', '广元', '遂宁', '内江', '乐山', '资阳', '宜宾',
                '南充', '达州', '雅安', '广安', '巴中', '眉山'
            ],
            '山东': [
                '济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁', '泰安', '威海', '日照', '滨州', '德州',
                '聊城', '临沂', '菏泽'
            ],
            '上海': [
                '黄浦', '徐汇', '长宁', '静安', '普陀', '虹口', '杨浦', '闵行', '宝山', '嘉定', '浦东新区', '金山',
                '松江', '青浦', '奉贤', '崇明'
            ],
            '广东': [
                '深圳', '广州', '珠海', '东莞', '佛山', '中山', '惠州', '汕头', '江门', '湛江', '肇庆', '梅州', '茂名',
                '阳江', '清远', '韶关', '揭阳', '汕尾', '潮州', '河源', '云浮'
            ],
            '广西': [
                '南宁', '柳州', '桂林', '梧州', '北海', '崇左', '来宾', '贺州', '玉林', '百色', '河池', '钦州',
                '防城港', '贵港'
            ],
            '安徽': [
                '合肥', '芜湖', '蚌埠', '淮北', '亳州', '宿州', '阜阳', '淮南', '滁州', '六安', '马鞍山', '宣城',
                '铜陵', '池州', '安庆', '黄山'
            ]
        }
        return s


#  各省份规模以上企业主要能源品种产量
class MainEnergyProductionModel(models.Model):
    province = models.CharField(max_length=100, verbose_name='行政单位', choices=my_methods.province())
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
        unique_together = ('year', 'province')
        verbose_name_plural = '规模以上企业主要能源产量'

    def __str__(self):
        return f"{self.province} - {self.year} - 规模以上企业主要能源产量"


#  能源设施
class RegionalResourceFacilitiesModel(models.Model):
    province = models.CharField(max_length=100, verbose_name='行政单位', choices=my_methods.province())
    type = models.CharField(max_length=20, verbose_name='能源归类', choices=(
        ('再生能源', '再生能源'),
        ('有限能源', '有限能源')
    ), default='再生能源')
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
        unique_together = ('province', 'name')
        verbose_name_plural = '地区资源设施使用情况'

    def __str__(self):
        return f"{self.province} - {self.name}"


#  地区再生能源储量/产量/结构/重要再生能源排行/概况/建设投资
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
        verbose_name_plural = '地区再生能源储量/产量统计'

    def __str__(self):
        return f"{self.year}年 - {self.province}省 - 再生能源储量/产量统计"


#  地区再生能源装机容量
class RenewableEnergyInstallationModel(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000)
    province = models.CharField(max_length=10, verbose_name='省份', choices=my_methods.province(), default='安徽')
    water = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='水电装机',
                                help_text='万千瓦')
    wind = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='风电装机',
                               help_text='万千瓦')
    sun = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                              verbose_name='光伏发电',
                              help_text='万千瓦')
    biomass = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                  verbose_name='生物质发电',
                                  help_text='万千瓦')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '地区可再生能源装机'

    def __str__(self):
        return f"{self.year}年 - {self.province}省 - 可再生能源装机"
