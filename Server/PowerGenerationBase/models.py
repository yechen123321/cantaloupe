from django.db import models


#  电场信息
class ElectricFieldModel(models.Model):
    my_choices = (
        ('综合性发电', '综合性发电'),
        ('火力发电', '火力发电'),
        ('水力发电', '水力发电'),
        ('风力发电', '风力发电'),
        ('太阳能发电', '太阳能发电'),
    )
    province = models.CharField(max_length=100, verbose_name='省级', null=True)
    station_type = models.CharField(max_length=100, verbose_name='电场类型', choices=my_choices)
    station_name = models.CharField(max_length=100, verbose_name='电场名称', null=True)
    state = models.BooleanField(default=True, verbose_name='运行状态')
    created_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '电场信息'

    def __str__(self):
        return f"{self.province}市 - {self.station_name} - {self.created_at}"


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
        return f"{self.electric_field.province}市 - {self.electric_field.station_name}"