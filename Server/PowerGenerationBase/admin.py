from django.contrib import admin

from .models import *


#  电场信息
class ElectricFieldAdmin(admin.ModelAdmin):
    list_filter = ('station_name', 'state')
    search_fields = ('station_name', 'state')
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


admin.site.register(ElectricFieldModel, ElectricFieldAdmin)
admin.site.register(ElectricFieldFaultModel, ElectricFieldFaultAdmin)