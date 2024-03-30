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


admin.site.register(MainEnergyProductionModel, MainEnergyProductionAdmin)
admin.site.register(RegionalResourceFacilitiesModel, RegionalResourceFacilitiesModelAdmin)