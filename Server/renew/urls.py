from django.urls import path

from .views import *

urlpatterns = [
    #  主要能源品种产量
    path('get_region_energy_production/<int:id>/', get_region_energy_production, name='get_region_energy_production'),
    #  地区资源设施使用情况
    path('get_regional_resource_facilities/<int:id>/', get_regional_resource_facilities, name='get_regional_resource_facilities'),
    #  地区再生能源储量
    path('get_energy_reserve/<int:id>/', get_energy_reserve, name='get_energy_reserve'),

]
