from django.contrib.admin.models import LogEntry
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from django.utils import timezone
from datetime import timedelta


class APIRequest(models.Model):
    path = models.CharField(max_length=255, verbose_name='请求路径')
    request_time = models.DateTimeField(auto_now_add=True, verbose_name='请求时间')


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


#  能源设施
class RegionalResourceFacilitiesModel(models.Model):
    my_choices = method.region()
    up_choice = (
        ('吨', '吨'),
        ('万吨', '万吨'),
        ('公顷', '公顷'),
        ('万公顷', '万公顷'),
        ('亩', '亩'),
        ('万亩', '万亩'),
        ('千瓦时', '千瓦时'),
        ('亿千瓦时', '亿千瓦时'),
    )

    region = models.CharField(max_length=100, verbose_name='行政单位', choices=my_choices)
    name = models.CharField(max_length=30, verbose_name='设施')
    do = models.CharField(max_length=30, verbose_name='工作')
    number = models.DecimalField(default=0, max_digits=7, decimal_places=2, verbose_name='数目')
    up = models.CharField(max_length=10, choices=up_choice, default='吨', verbose_name='单位')
    when = models.DateField(verbose_name='时间')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        unique_together = ('region', 'name')
        verbose_name_plural = '地区资源设施使用情况'

    def __str__(self):
        return f"{self.region} - {self.name}"


#  矿产能源
class MineralDevelopmentModel(models.Model):
    my_choices = method.region()

    region = models.CharField(max_length=100, verbose_name='行政单位', choices=my_choices)
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000, unique=True)
    coal = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='煤炭', help_text='亿吨')
    petroleum = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='石油', help_text='亿吨')
    gas = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='天然气', help_text='亿立方米')
    coalbed_methane = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='煤层气',
                                          help_text='亿立方米')
    shale_gas = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='页岩气',
                                    help_text='亿立方米')
    iron = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='铁矿', help_text='亿吨')
    manganese = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='锰矿', help_text='亿吨')
    ferrochrome = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='铬铁矿',
                                      help_text='亿吨')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        unique_together = ('year', 'region')
        verbose_name_plural = '矿产开发产量'

    def __str__(self):
        return f"{self.region} - {self.year}"


#  能源进出口量
class EnergyImportAndExportModel(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000, unique=True)
    petroleum_i = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='石油',
                                      help_text='进口（万吨）')
    coal_i = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='煤炭',
                                 help_text='进口（万吨）')
    power_i = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='电力',
                                  help_text='进口（亿千瓦时）')

    petroleum_e = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='石油',
                                      help_text='出口（万吨）')
    coal_e = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='煤炭',
                                 help_text='出口（万吨）')
    power_e = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='电力',
                                  help_text='出口（亿千瓦时）')
    all_i = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='可供消费的能源总量',
                                help_text='进口（万吨标准煤）')
    all_e = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='可供消费的能源总量',
                                help_text='出口（万吨标准煤）')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '能源进出口量'

    def __str__(self):
        return f"{self.year}年 - 能源进出口量"


#  发电装机容量
class PowerGenerationInstalledCapacityModel(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000, unique=True)
    thermal_power = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='火电',
                                        help_text='万千瓦')
    hydropower = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='水电',
                                     help_text='万千瓦')
    nuclear_power = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='核电',
                                        help_text='万千瓦')

    wind_power = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='风电',
                                     help_text='万千瓦')
    solar_power_generation = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                                 verbose_name='太阳能发电',
                                                 help_text='万千瓦')
    other_power = models.DecimalField(max_digits=10, decimal_places=2, default=1.0, verbose_name='其他',
                                      help_text='万千瓦')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '发电装机容量'

    def __str__(self):
        return f"{self.year}年 - 发电装机容量"


#  能源平衡总和
class EnergyProductionAndInventoryModel(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000, unique=True)
    total_energy_available_for_consumption = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                                                 verbose_name='可供消费的能源总量',
                                                                 help_text='万吨标准煤')
    total_production_of_primary_energy = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                                             verbose_name='一次能源生产总量',
                                                             help_text='万吨标准煤')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '能源平衡总和'

    def __str__(self):
        return f"{self.year}年 - 能源平衡总和"


#  能源消耗水平
class EnergyConsumptionModel(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000, unique=True)
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


#  新能源结构及趋势
class NewEnergyModel(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000)
    energy_type = models.CharField(max_length=50, verbose_name='能源类型', choices=(
        ('太阳能源', '太阳能源'), ('风力能源', '风力能源'), ('水利能源', '水利能源'), ('生物质能', '生物质能'),
        ('其他能源', '其他能源')), default='其他能源')
    value = models.DecimalField(max_digits=10, decimal_places=1, default=1.0,
                                verbose_name='产量',
                                help_text='亿千瓦时')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '新能源结构及趋势'

    def __str__(self):
        return f"{self.year}年 - 新能源结构及趋势"


#  全国市场交易及投资建设
class MarketInvestmentModel(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000)
    energy_investment = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                            verbose_name='能源重点项目投资',
                                            help_text='亿元')
    new_energy_storage_projects_power = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                                            verbose_name='投运新型储能项目累计装机规模',
                                                            help_text='万千瓦(功率)')
    new_energy_storage_projects = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                                      verbose_name='投运新型储能项目累计装机规模',
                                                      help_text='万千瓦时(电量)')
    electricity_trading = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                              verbose_name='电力市场交易电量',
                                              help_text='亿千瓦时')
    coal_methane = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                       verbose_name='煤层气产量',
                                       help_text='亿立方米')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '全国市场交易及投资建设'

    def __str__(self):
        return f"{self.year}年 - 全国市场交易及投资建设"


#  全国能源开发与需求
class EnergyDevelopAndDemandModel(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000)
    #  电力消纳量demand
    north_China_dm = models.DecimalField(max_digits=10, decimal_places=1, default=1.0,
                                         verbose_name='华北',
                                         help_text='亿千瓦(需求)')
    northeast_dm = models.DecimalField(max_digits=10, decimal_places=1, default=1.0,
                                       verbose_name='东北',
                                       help_text='亿千瓦(需求)')
    east_China_dm = models.DecimalField(max_digits=10, decimal_places=1, default=1.0,
                                        verbose_name='华东',
                                        help_text='亿千瓦(需求)')
    central_South_dm = models.DecimalField(max_digits=10, decimal_places=1, default=1.0,
                                           verbose_name='中南',
                                           help_text='亿千瓦(需求)')
    southwest_dm = models.DecimalField(max_digits=10, decimal_places=1, default=1.0,
                                       verbose_name='西南',
                                       help_text='亿千瓦(需求)')
    northwest_dm = models.DecimalField(max_digits=10, decimal_places=1, default=1.0,
                                       verbose_name='西北',
                                       help_text='亿千瓦(需求)')

    #  开发dv
    north_China_dv = models.DecimalField(max_digits=10, decimal_places=1, default=1.0,
                                         verbose_name='华北',
                                         help_text='亿千瓦(开发)')
    northeast_dv = models.DecimalField(max_digits=10, decimal_places=1, default=1.0,
                                       verbose_name='东北',
                                       help_text='亿千瓦(开发)')
    east_China_dv = models.DecimalField(max_digits=10, decimal_places=1, default=1.0,
                                        verbose_name='华东',
                                        help_text='亿千瓦(开发)')
    central_South_dv = models.DecimalField(max_digits=10, decimal_places=1, default=1.0,
                                           verbose_name='中南',
                                           help_text='亿千瓦(开发)')
    southwest_dv = models.DecimalField(max_digits=10, decimal_places=1, default=1.0,
                                       verbose_name='西南',
                                       help_text='亿千瓦(开发)')
    northwest_dv = models.DecimalField(max_digits=10, decimal_places=1, default=1.0,
                                       verbose_name='西北',
                                       help_text='亿千瓦(开发)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '全国能源开发与需求'

    def __str__(self):
        return f"{self.year}年 - 全国能源开发与需求"


#  全国能源储量统计
class EnergyReserveModel(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000)
    range = models.CharField(max_length=10,  verbose_name='统计范围', choices=(('全国', '全国'), ('全球', '全球')), default='全球')
    coal = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                               verbose_name='煤炭',
                               help_text='万亿吨')
    petroleum = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                    verbose_name='石油',
                                    help_text='亿吨')
    natural_gas = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                      verbose_name='天然气',
                                      help_text='万亿立方米')
    geothermal = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                     verbose_name='地热',
                                     help_text='万千瓦')
    wind = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                               verbose_name='风能',
                               help_text='亿千瓦')
    sun = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                              verbose_name='太阳能',
                              help_text='亿千瓦')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '全国能源储量统计'

    def __str__(self):
        return f"{self.year}年 - {self.range} - 能源储量统计"
