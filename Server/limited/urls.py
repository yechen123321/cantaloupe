from django.urls import path

from .views import *


urlpatterns = [
    #  地区市场交易及投资建设
    path('get_market_investment/<int:id>/', get_market_investment, name='get_market_investment'),

]
