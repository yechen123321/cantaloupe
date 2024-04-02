import SuYuanApplication

from django.contrib import admin
from django.urls import include, path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from SuYuanApplication.views import my_login, my_logout

schema_view = get_schema_view(
    openapi.Info(
        title="SuYuanAPI",
        default_version='v2.0',
        #  文档描述
        description="=================================  接口具体应用，参考以下信息：  =================================\n\n"
                    "---------------------------------- natural ----------------------------------\n\n"
                    "矿产开发产量—————————————get_regional_resource_facilities/<int:id>/\n"
                    "地区资源设施使用情况——————get_mineral_develop/<int:id>/\n"
                    "能源进出口量—————————————get_energy_import_and_export/\n"
                    "发电装机容量—————————————get_power_generation_installed_capacity/\n"
                    "能源平衡总和—————————————get_energy_production_and_inventory/\n"
                    "能源消耗水平—————————————get_energy_consumption/\n"
                    "水光风发电量—————————————get_region_energy_production/\n"
                    "新能源结构及趋势—————————get_new_energy/\n"
                    "全国市场交易及投资建设————get_market_investment/\n"
                    "全国能源开发与需求———————get_energy_develop_demand/\n"
                    "全国能源储量统计—————————get_energy_reserve/\n"

                    "\n\n---------------------------------- renew ----------------------------------\n\n"

                    "主要能源品种产量—————————get_region_energy_production/<int:id>/\n"
                    "地区资源设施使用情况——————get_regional_resource_facilities/<int:id>/\n"
                    "地区再生能源储量—————————get_energy_reserve/<int:id>/\n"
                    "地区再生能源结构—————————get_energy_structure/<int:id>/\n"
                    "地区再生能源产能—————————get_energy_capacity/<int:id>/\n"
                    "地区再生能源排行—————————get_energy_ranking/<int:id>/\n"
                    "地区再生能源结构概况—————get_energy_reserve_general/<int:id>/\n"

                    "\n\n---------------------------------- limited ----------------------------------\n\n"
                    "地区有限能源经济形势—————get_market_investment/<int:id>/"

                    "\n\n---------------------------------- analyse ----------------------------------\n\n"
                    "能源发展热力图———————————get_heat_map/<int:id>/\n"

                    "\n\n---------------------------------- PowerGenerationBase ----------------------------------\n\n"
                    "电场故障信息获取—————————get_electric_field_fault/<int:id>/\n"
                    "电场故障信息通知—————————put_electric_field_fault/<int:id>/\n"


                    "\n\n===============================================================================================\n\n"
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path('index_data/', SuYuanApplication.views.index_data, name='index_data'),
]

urlpatterns += [
    path('api/', include('SuYuanApplication.urls')),
    path('api/renew/', include('renew.urls')),
    path('api/limited/', include('limited.urls')),
    path('api/analyse/', include('analyse.urls')),
    path('api/power/', include('PowerGenerationBase.urls')),
    path('api_docs/', schema_view.with_ui('swagger',
                                          cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += [
    path('', my_login, name='login'),
    path('logout/', my_logout, name='logout'),
]