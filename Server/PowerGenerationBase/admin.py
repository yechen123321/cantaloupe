from django.contrib import admin

from .models import *


#  电场信息
class ElectricFieldAdmin(admin.ModelAdmin):
    list_filter = ('state', 'station_type')
    search_fields = ('state', 'station_type')

    # readonly_fields = [field.name for field in ElectricFieldModel._meta.fields]

    def has_change_permission(self, request, obj=None):
        return False


#  电场故障信息
class ElectricFieldFaultAdmin(admin.ModelAdmin):
    list_filter = ('electric_field__station_name', 'created_at')
    search_fields = ('electric_field__station_name', 'created_at')
    readonly_fields = ('send_times',)

    def has_change_permission(self, request, obj=None):
        # 编辑后数据只可读
        return False


#  电场故障信息
class BaseDistributionAdmin(admin.ModelAdmin):
    list_filter = ('created_at',)
    search_fields = ('created_at',)
    readonly_fields = ()

    def has_change_permission(self, request, obj=None):
        # 编辑后数据只可读
        return False


#  地区基地设备运行相关信息
class BaseEquipmentWorkingInformationAdmin(admin.ModelAdmin):
    list_filter = ('province', 'device_state')
    search_fields = ('province', 'device_state')

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(ElectricFieldModel, ElectricFieldAdmin)
admin.site.register(ElectricFieldFaultModel, ElectricFieldFaultAdmin)
admin.site.register(BaseDistributionModel, BaseDistributionAdmin)
admin.site.register(BaseEquipmentWorkingInformationModel, BaseEquipmentWorkingInformationAdmin)
