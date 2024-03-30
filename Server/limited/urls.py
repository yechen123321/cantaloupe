from django.urls import path

from .views import *


urlpatterns = [
    #  地区有限能源经济形势
    path('get_market_investment/<int:id>/', get_market_investment, name='get_market_investment'),

]
