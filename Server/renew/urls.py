from django.urls import path

from .views import *

urlpatterns = [
    #  主要能源品种产量
    path('get_region_energy_production/<int:id>/', get_region_energy_production, name='get_region_energy_production'),
    #  电场故障信息
    path('electric_field_fault/<int:id>/', ElectricFieldFault.as_view(), name='ElectricFieldFaultGET'),
]
