from django.urls import path

from .views import *

urlpatterns = [
    #  矿产开发产量
    path('get_regional_resource_facilities/<int:id>/', get_regional_resource_facilities, name='get_regional_resource_facilities'),
    #  地区资源设施使用情况
    path('get_mineral_develop/<int:id>/', get_mineral_develop, name='get_mineral_develop'),
    #  能源进出口量
    path('get_energy_import_and_export/', get_energy_import_and_export, name='get_energy_import_and_export'),
    #  发电装机容量
    path('get_power_generation_installed_capacity/', get_power_generation_installed_capacity, name='get_power_generation_installed_capacity'),
    #  能源平衡总和
    path('get_energy_production_and_inventory/', get_energy_production_and_inventory, name='get_energy_production_and_inventory'),
    #  能源消耗水平
    path('get_energy_consumption/', get_energy_consumption, name='get_energy_consumption'),
    #  新能源结构及趋势
    path('get_new_energy/', get_new_energy, name='get_new_energy'),
]