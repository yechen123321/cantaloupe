from django.urls import path

from .views import *

urlpatterns = [
    #  电场故障信息GET
    path('get_electric_field_fault/<int:id>/', get_electric_field_fault, name='get_electric_field_fault'),
    #  电场故障信息PUT
    path('put_electric_field_fault/', put_electric_field_fault, name='put_electric_field_fault'),
    #  地区基地分布
    path('get_base_distribution/<int:id>/<int:typeNum>/', get_base_distribution, name='get_base_distribution'),
    #  地区电场运行状况
    path('get_operation_status/<int:id>/<int:typeNum>/', get_operation_status, name='get_operation_status'),
    #  地区基地设备运行相关信息
    path('get_base_equipment_working_information/<int:id>/<int:typeNum>/', get_base_equipment_working_information, name='get_base_equipment_working_information'),

]
