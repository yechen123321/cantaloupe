from django.contrib import admin

from .models import *


#  地区有限能源经济形势
class MarketInvestmentAdmin(admin.ModelAdmin):
    list_filter = ('province', 'created_at')
    search_fields = ('province', 'created_at')


#  地区不可再生能源储量/产量/结构/概况/
class EnergyReserveAdmin(admin.ModelAdmin):
    list_filter = ('province', 'created_at')
    search_fields = ('province', 'created_at')


#  地区不可再生能源开采效率
class ExtractionEfficiencyAdmin(admin.ModelAdmin):
    list_filter = ('province', 'created_at')
    search_fields = ('province', 'created_at')


admin.site.register(MarketInvestmentModel, MarketInvestmentAdmin)
admin.site.register(EnergyReserveModel, EnergyReserveAdmin)
admin.site.register(ExtractionEfficiencyModel, ExtractionEfficiencyAdmin)
