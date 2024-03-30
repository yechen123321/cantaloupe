from django.contrib import admin

from .models import *


#  能源发展热力图
class HeatMapAdmin(admin.ModelAdmin):
    list_filter = ('name', 'created_at')
    search_fields = ('name', 'created_at')

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(HeatMapModel, HeatMapAdmin)
