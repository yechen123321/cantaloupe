from django.urls import path

from .views import *


urlpatterns = [
    #  能源发展热力图
    path('get_heat_map/<int:id>/', get_heat_map, name='get_heat_map'),

]
