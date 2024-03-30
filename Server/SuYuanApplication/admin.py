from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.admin.options import ModelAdmin

from .models import *

admin.site.site_header = 'SuYuan'


#  历史记录
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_id', 'object_repr', 'user', 'action_flag', 'action_time']
    list_filter = ['content_type', 'action_flag', 'user']
    search_fields = ['object_repr', 'change_message']
    date_hierarchy = 'action_time'

    list_per_page = 12


admin.site.register(LogEntry, LogEntryAdmin)


# class FileModelAdmin(admin.ModelAdmin):
#     list_filter = ('name', 'type')
#     list_display = ('path', )
#     search_fields = ('name', 'type')


#  矿产能源
class MineralDevelopmentModelAdmin(admin.ModelAdmin):
    list_filter = ('year', 'region')
    search_fields = ('year', 'region')


#  能源进出口量
class EnergyImportAndExportAdmin(admin.ModelAdmin):
    list_filter = ('year',)
    search_fields = ('year', )


#  发电装机容量
class PowerGenerationInstalledCapacityAdmin(admin.ModelAdmin):
    list_filter = ('year',)
    search_fields = ('year',)


#  能源平衡总和
class EnergyProductionAndInventoryAdmin(admin.ModelAdmin):
    list_filter = ('year',)
    search_fields = ('year',)


#  能源消耗水平
class EnergyConsumptionAdmin(admin.ModelAdmin):
    list_filter = ('year',)
    search_fields = ('year',)


#  新能源结构与趋势
class NewEnergyAdmin(admin.ModelAdmin):
    list_filter = ('year', 'energy_type')
    search_fields = ('year', 'energy_type')


#  全国市场交易及投资建设
class MarketInvestmentAdmin(admin.ModelAdmin):
    list_filter = ('year',)
    search_fields = ('year',)


#  全国能源开发与需求
class EnergyDevelopAndDemandAdmin(admin.ModelAdmin):
    list_filter = ('year',)
    search_fields = ('year',)


#  全国/全球能源储量统计
class EnergyReserveAdmin(admin.ModelAdmin):
    list_filter = ('year', 'range')
    search_fields = ('year', 'range')


# admin.site.register(FileModel, FileModelAdmin)
admin.site.register(PowerGenerationInstalledCapacityModel, PowerGenerationInstalledCapacityAdmin)
admin.site.register(MineralDevelopmentModel, MineralDevelopmentModelAdmin)
admin.site.register(EnergyImportAndExportModel, EnergyImportAndExportAdmin)
admin.site.register(EnergyProductionAndInventoryModel, EnergyProductionAndInventoryAdmin)
admin.site.register(EnergyConsumptionModel, EnergyConsumptionAdmin)
admin.site.register(NewEnergyModel, NewEnergyAdmin)
admin.site.register(MarketInvestmentModel, MarketInvestmentAdmin)
admin.site.register(EnergyDevelopAndDemandModel, EnergyDevelopAndDemandAdmin)
admin.site.register(EnergyReserveModel, EnergyReserveAdmin)
