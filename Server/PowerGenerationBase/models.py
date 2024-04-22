from django.core.exceptions import ValidationError
from django.db import models


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


#  电场信息
class ElectricFieldModel(models.Model):
    province = models.CharField(max_length=100, verbose_name='省份', default='安徽', choices=my_methods.province())
    city = models.CharField(max_length=10, verbose_name='市级', choices=my_methods.province(), default='合肥')
    station_type = models.CharField(max_length=100, verbose_name='隶属电场类型', choices=(
        ('综合性发电', '综合性发电'),
        ('火电厂', '火电厂'),
        ('水电厂', '水电厂'),
        ('光电场', '光电场'),
        ('风电场', '风电场')
    ), default='综合性发电')
    station_name = models.CharField(max_length=100, verbose_name='电场名称', null=True)
    state = models.BooleanField(default=True, verbose_name='运行状态')
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '电场信息'

    def __str__(self):
        return f"{self.city}市 - {self.station_name} - {self.created_at}"


#  自定义管理器
class FalseElectricFieldManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(state=False)


#  电场故障信息
class ElectricFieldFaultModel(models.Model):
    electric_field = models.ForeignKey(ElectricFieldModel, on_delete=models.CASCADE, verbose_name='电场信息',
                                       limit_choices_to={'state': False}, unique=True)
    malfunction_reason = models.CharField(max_length=100, verbose_name='故障原因')
    send_times = models.IntegerField(default=0, verbose_name='通知维修次数')
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '电场故障'

    def __str__(self):
        return f"{self.electric_field.city}市 - {self.electric_field.station_name}"


#  地区基地分布
class BaseDistributionModel(models.Model):
    electric_field = models.ForeignKey(ElectricFieldModel, on_delete=models.CASCADE, verbose_name='电场信息', unique=True)
    value = models.IntegerField(default=100, verbose_name='范围')
    thing = models.CharField(max_length=10, verbose_name='名称', default='一号电厂')
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '基地分布'
        unique_together = (('electric_field', 'thing'), )

    def __str__(self):
        return f"{self.electric_field.province}省 - {self.electric_field.city}市 - 基地分布"

    def save(self, *args, **kwargs):
        # 检查联合唯一键的唯一性
        if BaseDistributionModel.objects.filter(electric_field__city=self.electric_field.city, thing=self.thing).exists():
            raise ValidationError('联合唯一键冲突')
        super().save(*args, **kwargs)


#  地区基地设备运行相关信息
class BaseEquipmentWorkingInformationModel(models.Model):
    province = models.CharField(max_length=100, verbose_name='省份', default='安徽', choices=my_methods.province())
    device_name = models.CharField(max_length=20, verbose_name='设备名称', default='未知设备')
    device_type = models.CharField(max_length=20, verbose_name='设备类型', default='未知类型')
    type_in = models.CharField(max_length=100, verbose_name='隶属电场类型', choices=(
        ('综合性发电', '综合性发电'),
        ('火电厂', '火电厂'),
        ('水电厂', '水电厂'),
        ('光电场', '光电场'),
        ('风电场', '风电场')
    ), default='综合性发电')
    device_state = models.CharField(max_length=10, verbose_name='设备状态', default='正常', choices=(
        ('正常', '正常'),
        ('异常', '异常')
    ))
    device_information = models.CharField(max_length=50, verbose_name='设备实时信息', default='未知')
    when = models.DateField(verbose_name='时间')

    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '基地设备运行相关信息'

    def __str__(self):
        return f"{self.province}省 - {self.device_name} - 运行状态: {self.device_state}"
