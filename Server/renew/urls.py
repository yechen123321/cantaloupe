from django.urls import path

from .views import *

urlpatterns = [
    #  主要能源品种产量
    path('get_region_energy_production/<int:id>/', get_region_energy_production, name='get_region_energy_production'),
    #  电场故障信息GET
    path('get_electric_field_fault/<int:id>/', get_electric_field_fault, name='get_electric_field_fault'),
    #  电场故障信息PUT
    path('put_electric_field_fault/', put_electric_field_fault, name='put_electric_field_fault'),
]
