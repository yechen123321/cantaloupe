import SuYuanApplication, renew, limited

from django.contrib import admin
from django.urls import include, path

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from SuYuanApplication.views import my_logout

schema_view = get_schema_view(
    openapi.Info(
        title="SuYuanAPI",
        default_version='v2.0',
        #  文档描述
        description="=================================  接口具体应用，参考以下信息：  =================================\n\n"
                    "矿产开发产量——————get_regional_resource_facilities/<int:id>/\n"
                    "地区资源设施使用情况——————get_mineral_develop/<int:id>/\n"
                    "能源进出口量——————get_energy_import_and_export/\n"
                    "发电装机容量——————get_power_generation_installed_capacity/\n"
                    "能源平衡总和——————get_energy_production_and_inventory/\n"
                    "能源消耗水平——————get_energy_consumption/\n"
                    "水光风发电量——————get_region_energy_production/\n"
                    "新能源结构及趋势——————get_new_energy/\n"
                    
                    
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
    path('api/', include('renew.urls')),
    path('api/', include('limited.urls')),
    path('api_docs/', schema_view.with_ui('swagger',
                                          cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += [
    path('logout/', my_logout, name='logout'),
]
