from django.urls import path

from .views import *

urlpatterns = [
    #  主要能源品种产量
    path('get_region_energy_production/<int:id>/', get_region_energy_production, name='get_region_energy_production'),
    #  地区资源设施使用情况
    path('get_regional_resource_facilities/<int:id>/', get_regional_resource_facilities, name='get_regional_resource_facilities'),
    #  地区再生能源储量
    path('get_energy_reserve/<int:id>/', get_energy_reserve, name='get_energy_reserve'),
    #  地区再生能源结构
    path('get_energy_structure/<int:id>/', get_energy_structure, name='get_energy_structure'),
    #  地区再生能源产能
    path('get_energy_capacity/<int:id>/', get_energy_capacity, name='get_energy_capacity'),
    #  地区再生能源排行
    path('get_energy_ranking/<int:id>/', get_energy_ranking, name='get_energy_ranking'),
    #  地区再生能源储量概况
    path('get_energy_reserve_general/<int:id>/', get_energy_reserve_general, name='get_energy_reserve_general'),
    #  地区再生能源装机容量
    path('get_energy_installation/<int:id>/', get_energy_installation, name='get_energy_installation'),
    #  地区再生能源建设投资
    path('get_energy_construction_investment/<int:id>/', get_energy_construction_investment, name='get_energy_construction_investment'),

    #  地区分种类发电储能
    path('get_classification_capacity/<int:id>/', get_classification_capacity, name='get_classification_capacity'),
    #  地区分种类能源结构
    path('get_classification_structure/<int:id>/', get_classification_structure, name='get_classification_structure'),
    #  地区分种类发电装机容量
    path('get_classification_installation/<int:id>/', get_classification_installation, name='get_classification_installation'),
    #  地区分种类储量概况
    path('get_classification_reserve_general/<int:id>/', get_classification_reserve_general, name='get_classification_reserve_general'),

]
