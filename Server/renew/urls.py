from django.urls import path

from .views import *

urlpatterns = [
    path('renew/get_region_energy_production/<int:id>/', get_region_energy_production, name='get_region_energy_production'),
    path('renew/electric_field_fault/', ElectricFieldFault.as_view(), name='ElectricFieldFault'),

]