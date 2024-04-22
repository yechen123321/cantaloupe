from django.urls import path

from .views import *


urlpatterns = [
    #  能源发展热力图
    path('get_heat_map/<int:id>/', get_heat_map, name='get_heat_map'),
    #  能源产能及结构
    path('get_capacity_structure/<int:id>/', get_capacity_structure, name='get_capacity_structure'),
    #  能源消耗水平
    path('get_consumption/<int:id>/', get_consumption, name='get_consumption'),

]
