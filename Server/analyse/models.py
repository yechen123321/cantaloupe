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
    province = models.CharField(max_length=100, verbose_name='省级', null=True, choices=method.region())
    name = models.CharField(max_length=100, verbose_name='市级', null=True)
    value = models.FloatField(verbose_name='数值', null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name_plural = '能源发展情况(权重)'

    def __str__(self):
        return f"{self.province}省 - {self.name}市 - 能源发展情况"
