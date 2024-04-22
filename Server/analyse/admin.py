from django.contrib import admin

from .models import *


#  能源发展热力图
class HeatMapAdmin(admin.ModelAdmin):
    list_filter = ('city', 'created_at')
    search_fields = ('city', 'created_at')

    def has_change_permission(self, request, obj=None):
        return False


#  能源产能及结构
class CapacityStructureAdmin(admin.ModelAdmin):
    list_filter = ('province', 'created_at')
    search_fields = ('province', 'created_at')

    def has_change_permission(self, request, obj=None):
        return False


#  能源消耗水平
class ConsumptionAdmin(admin.ModelAdmin):
    list_filter = ('province', 'created_at')
    search_fields = ('province', 'created_at')

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(HeatMapModel, HeatMapAdmin)
admin.site.register(CapacityStructureModel, CapacityStructureAdmin)
admin.site.register(ConsumptionModel, ConsumptionAdmin)
