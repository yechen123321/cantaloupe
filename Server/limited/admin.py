from django.contrib import admin

from .models import *


#  地区有限能源结构
class NewEnergyAdmin(admin.ModelAdmin):
    list_filter = ('province', 'created_at')
    search_fields = ('province', 'created_at')


admin.site.register(NewEnergyModel, NewEnergyAdmin)
