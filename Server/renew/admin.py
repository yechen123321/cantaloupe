from django.contrib import admin

from .models import *


#  各省份规模以上企业主要能源品种产量
class MainEnergyProductionAdmin(admin.ModelAdmin):
    list_filter = ('year', 'region')
    search_fields = ('year', 'region')

    def has_change_permission(self, request, obj=None):
        # 编辑后数据只可读
        return False


#  能源设施
class RegionalResourceFacilitiesModelAdmin(admin.ModelAdmin):
    list_filter = ('region', 'name')
    search_fields = ('region', 'name')

    def has_change_permission(self, request, obj=None):
        return False


#  地区再生能源储量/产量/结构/重要再生能源排行/概况
class EnergyReserveAdmin(admin.ModelAdmin):
    list_filter = ('year', 'province')
    search_fields = ('year', 'province')

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(MainEnergyProductionModel, MainEnergyProductionAdmin)
admin.site.register(RegionalResourceFacilitiesModel, RegionalResourceFacilitiesModelAdmin)
admin.site.register(EnergyReserveModel, EnergyReserveAdmin)
