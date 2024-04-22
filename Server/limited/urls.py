from django.urls import path

from .views import *


urlpatterns = [
    #  地区有限能源经济形势
    path('get_market_investment/<int:id>/', get_market_investment, name='get_market_investment'),
    #  地区不可再生能源结构
    path('get_energy_structure/<int:id>/', get_energy_structure, name='get_energy_structure'),
    #  地区不可再生能源产能
    path('get_energy_capacity/<int:id>/', get_energy_capacity, name='get_energy_capacity'),
    #  地区不可再生能源储量概况
    path('get_energy_reserve_general<int:id>/', get_energy_reserve_general, name='get_energy_reserve_general'),
    #  地区不可再生能源储能图
    path('get_energy_reserve/<int:id>/', get_energy_reserve, name='get_energy_reserve'),
    #  地区不可再生能源开采效率
    path('get_extraction_efficiency/<int:id>/', get_extraction_efficiency, name='get_extraction_efficiency'),

]
