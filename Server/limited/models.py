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


#  地区有限能源结构
class NewEnergyModel(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000)
    province = models.CharField(max_length=20, verbose_name='省份', choices=method.region(), default='安徽')
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
        return f"{self.year}年 - {self.province}省 - 新能源结构及趋势"


#  地区有限能源经济形势
class MarketInvestmentModel(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2099)], verbose_name='年份',
                               default=2000)
    province = models.CharField(max_length=20, verbose_name='省份', choices=method.region(), default='安徽')
    natural_gas = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                      verbose_name='天然气累计消费量',
                                      help_text='亿立方米')
    coal = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                               verbose_name='原煤产量',
                               help_text='千万吨')
    coal_methane = models.DecimalField(max_digits=10, decimal_places=2, default=1.0,
                                       verbose_name='煤层气产量',
                                       help_text='亿立方米')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '地区市场交易及投资建设'

    def __str__(self):
        return f"{self.year}年 - {self.province}省 - 有限能源经济形势"
