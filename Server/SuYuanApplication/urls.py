from django.urls import path

from .views import *

urlpatterns = [
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
    #  全国市场交易及投资建设
    path('get_market_investment/', get_market_investment, name='get_market_investment'),
    #  全国能源开发与需求
    path('get_energy_develop_demand/', get_energy_develop_demand, name='get_energy_develop_demand'),
    #  全国能源储量统计
    path('get_energy_reserve/', get_energy_reserve, name='get_energy_reserve'),
]
