from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse

from datetime import datetime, timedelta

from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes  # 装饰器
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser  # 权限装饰器
from django.core.serializers import serialize

from django.apps import apps
from django.db.models import Count

from .permissions import MyPermission
from .seriailzers import *
from .models import *


def index(request):
    # Page from the theme
    return render(request, 'pages/dashboard.html')


def my_logout(request):
    response = redirect(reverse('admin:index'))
    request.session.delete(request.session.session_key)
    return response


def my_login(request):
    response = redirect(reverse('admin:login'))
    return response


class methods:
    @staticmethod
    def region_dict():
        s = {
            1: '北京',
            2: '天津',
            3: '河北',
            4: '山西',
            5: '内蒙古',
            6: '辽宁',
            7: '吉林',
            8: '黑龙江',
            9: '上海',
            10: '江苏',
            11: '浙江',
            12: '安徽',
            13: '福建',
            14: '江西',
            15: '山东',
            16: '河南',
            17: '湖北',
            18: '湖南',
            19: '广东',
            20: '广西',
            21: '海南',
            22: '重庆',
            23: '四川',
            24: '贵州',
            25: '云南',
            26: '西藏',
            27: '陕西',
            28: '甘肃',
            29: '青海',
            30: '宁夏',
            31: '新疆'
        }
        return s


"""
========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
API
========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
"""


@api_view(['GET', ])
@permission_classes([MyPermission])
def index_data(request):
    #  用户数量
    Users = get_user_model()
    user_num_now = Users.objects.all().count()
    user_num_last = Users.objects.filter(date_joined__gte=timezone.now() - timedelta(days=3)).count()

    #  总数据量
    total_data_now = 0
    total_data_last = 0
    for model in apps.get_models():
        if hasattr(model, 'created_at'):
            total_data_now += model.objects.all().count()
        if hasattr(model, 'created_at'):
            total_data_last += model.objects.filter(created_at__gte=timezone.now() - timedelta(days=3)).count()
    data_volume_now = total_data_now

    data_volume_last = total_data_last

    #  今日访问量
    visits_now = APIRequest.objects.filter(path__icontains='/api/',
                                           request_time__range=[datetime.now() - timedelta(days=1),
                                                                datetime.now()]).values('path').count()
    visits_last = APIRequest.objects.filter(path__icontains='/api/',
                                            request_time__range=[datetime.now() - timedelta(days=2),
                                                                 datetime.now() - timedelta(days=1)]).values(
        'path').count()

    # 接口使用量
    total_requests_now = APIRequest.objects.filter(path__icontains='/api/',
                                                   request_time__range=[datetime.now() - timedelta(days=1),
                                                                        datetime.now()]).values(
        'path').distinct().count()
    total_requests_last = APIRequest.objects.filter(path__icontains='/api/',
                                                    request_time__range=[datetime.now() - timedelta(days=2),
                                                                         datetime.now() - timedelta(days=1)]).values(
        'path').distinct().count()

    # 获取一周前的日期
    one_week_ago = timezone.now().date() - timedelta(weeks=1)
    w_data = []

    for i in range(1, 8):
        # 计算当前日期
        current_date = one_week_ago + timedelta(days=i)
        # 当天的 00:00:00
        start_time = datetime.combine(current_date, datetime.min.time())
        # 当天的 23:59:59
        end_time = datetime.combine(current_date, datetime.max.time())
        w_data.append(APIRequest.objects.filter(
            path='/api/power/put_electric_field_fault/',
            request_time__range=[start_time, end_time]
        ).count())
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=6)
    date_week_list = []
    current_date = start_date
    while current_date <= end_date:
        weekday = current_date.weekday()
        date_week_list.append(weekday)
        current_date += timedelta(days=1)
    w_labels = []
    weekly_list = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    for i in date_week_list:
        w_labels.append(weekly_list[i])

    today = datetime.today()
    start_date = today - timedelta(days=350)
    monthly_list = []
    current_date = start_date
    while current_date <= today:
        month_year = current_date.strftime("%m")
        monthly_list.append(int(month_year))
        current_date += timedelta(days=30)
    m_list = ['0', '一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
    m_labels = []
    for i in monthly_list:
        m_labels.append(m_list[i])
    m_data = {'added': [], 'changed': []}
    last_month = 0
    now_year = datetime.now().year - 1
    for i in monthly_list:
        if last_month > i:
            now_year += 1
        m_data['added'].append(LogEntry.objects.filter(change_message__contains='added', action_time__month=i, action_time__year=now_year).count())
        m_data['changed'].append(LogEntry.objects.filter(change_message__contains='changed', action_time__month=i, action_time__year=now_year).count())
        last_month = i

    #  ======================================================================
    data = {"total_requests": [total_requests_now, total_requests_last], "visits": [visits_now * 12, visits_last * 12],
            "data_volume": [data_volume_now, data_volume_last], "user_num": [user_num_now, user_num_last],
            "weekly_submission_quantity": {
                "labels": w_labels,
                "data": w_data},
            "month_log_update": {
                "labels": m_labels,
                "data": m_data}
            }
    return JsonResponse(data)


#  地区资源设施使用情况
@api_view(['GET', ])
@permission_classes(())
@extend_schema(responses=MineralDevelopmentSerializer)
def get_mineral_develop(request, id=1):
    region_dict = methods.region_dict()
    if request.method == 'GET':
        data_objects = MineralDevelopmentModel.objects.filter(region=region_dict[id]).first()
        data = MineralDevelopmentSerializer(instance=data_objects, many=False, context={'region': region_dict[id]})
        return Response(data=data.data, status=status.HTTP_200_OK)


#  能源进出口量
@api_view(['GET', ])
@permission_classes(())
def get_energy_import_and_export(request):
    if request.method == 'GET':
        data_objects = EnergyImportAndExportModel.objects.first()
        data = EnergyImportAndExportSerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  发电装机容量
@api_view(['GET', ])
@permission_classes(())
def get_power_generation_installed_capacity(request):
    if request.method == 'GET':
        data_objects = PowerGenerationInstalledCapacityModel.objects.first()
        data = PowerGenerationInstalledCapacitySerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  能源平衡总和
@api_view(['GET', ])
@permission_classes(())
def get_energy_production_and_inventory(request):
    if request.method == 'GET':
        data_objects = EnergyProductionAndInventoryModel.objects.first()
        data = EnergyProductionAndInventorySerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  能源消耗水平
@api_view(['GET', ])
@permission_classes(())
def get_energy_consumption(request):
    if request.method == 'GET':
        data_objects = EnergyConsumptionModel.objects.first()
        data = EnergyConsumptionSerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  新能源结构及趋势
@api_view(['GET', ])
@permission_classes(())
def get_new_energy(request):
    if request.method == 'GET':
        data_objects = NewEnergyModel.objects.first()
        data = NewEnergySerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  全国市场交易及投资建设
@api_view(['GET', ])
@permission_classes(())
def get_market_investment(request):
    if request.method == 'GET':
        data_objects = NewEnergyModel.objects.first()
        data = MarketInvestmentSerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  全国能源开发与需求
@api_view(['GET', ])
@permission_classes(())
def get_energy_develop_demand(request):
    if request.method == 'GET':
        data_objects = EnergyDevelopAndDemandModel.objects.first()
        data = EnergyDevelopAndDemandSerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  全国能源储量统计
@api_view(['GET', ])
@permission_classes(())
def get_energy_reserve(request):
    if request.method == 'GET':
        data_objects = EnergyReserveModel.objects.first()
        data = EnergyReserveSerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)
