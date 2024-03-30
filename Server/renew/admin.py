from django.contrib import admin

from .models import *


#  各省份规模以上企业主要能源品种产量
class MainEnergyProductionAdmin(admin.ModelAdmin):
    list_filter = ('year', 'region')
    search_fields = ('year', 'region')

    def has_change_permission(self, request, obj=None):
        # 编辑后数据只可读
        return False


#  电场信息
class ElectricFieldAdmin(admin.ModelAdmin):
    list_filter = ('station_name', 'created_at')
    search_fields = ('station_name', 'created_at')
    # readonly_fields = [field.name for field in ElectricFieldModel._meta.fields]

    def has_change_permission(self, request, obj=None):
        return False


#  电场故障信息
class ElectricFieldFaultAdmin(admin.ModelAdmin):
    list_filter = ('electric_field__station_name', 'created_at')
    search_fields = ('electric_field__station_name', 'created_at')
    readonly_fields = ('send_times', )

    def has_change_permission(self, request, obj=None):
        # 编辑后数据只可读
        return False


admin.site.register(MainEnergyProductionModel, MainEnergyProductionAdmin)
admin.site.register(ElectricFieldModel, ElectricFieldAdmin)
admin.site.register(ElectricFieldFaultModel, ElectricFieldFaultAdmin)
