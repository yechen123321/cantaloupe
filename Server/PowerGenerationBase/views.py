import json

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt  # 取消 csrf 限制的装饰器
from django.utils.decorators import method_decorator
from datetime import datetime, timedelta

from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize

from django.apps import apps
from django.db.models import Count, F
from rest_framework.views import APIView

from .seriailzers import *
from .models import *


class methods:
    @staticmethod
    def region_dict(num=12):
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
        return s[num]

    @staticmethod
    def province_dict(self, num=12):
        s = {
            '北京': [

            ],
            '天津': [

            ],
            '河北': [

            ],
            '山西': [

            ],
            '内蒙古': [

            ],
            '辽宁': [

            ],
            '吉林': [

            ],
            '黑龙江': [

            ],
            '上海': [

            ],
            '江苏': [

            ],
            '浙江': [

            ],
            '安徽': [
                '合肥', '芜湖', '蚌埠', '淮北', '亳州', '宿州', '阜阳', '淮南', '滁州', '六安', '马鞍山', '宣城',
                '铜陵', '池州', '安庆', '黄山'
            ],
            '福建': [

            ],
            '江西': [

            ],
            '山东': [

            ],
            '河南': [

            ],
            '湖北': [

            ],
            '湖南': [

            ],
            '广东': [

            ],
            '广西': [

            ],
            '海南': [

            ],
            '重庆': [

            ],
            '四川': [

            ],
            '贵州': [

            ],
            '云南': [

            ],
            '西藏': [

            ],
            '陕西': [

            ],
            '甘肃': [

            ],
            '青海': [

            ],
            '宁夏': [

            ],
            '新疆': [

            ],
        }
        return s[self.region_dict(num)]

    def is_json(myjson):
        try:
            json_object = json.loads(myjson)
        except ValueError as e:
            return False
        return True


"""
========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
API
========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
"""


#  电场故障信息GET
@api_view(['GET', ])
@permission_classes(())
def get_electric_field_fault(request, id=12):
    if request.method == 'GET':
        fault_data = list(ElectricFieldModel.objects.filter(province__in=methods.province_dict(self=methods, num=id),
                                                            state=False).values_list('id'))
        fault_data = [it[0] for it in fault_data if isinstance(it, tuple)]
        data_objects = ElectricFieldFaultModel.objects.filter(electric_field_id__in=fault_data).all()
        data = ElectricFieldFaultSerializer(instance=data_objects, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  电场故障信息PUT
@api_view(['PUT', ])
@permission_classes(())
def put_electric_field_fault(request):
    #  获取用户提交的故障信息请求
    if request.method == 'PUT':
        #  故障电场的名称和故障原因对应上即视为正确数据
        data = request.data
        print(data)
        ElectricFieldFaultModel.objects.filter(electric_field__station_name=data['name'],
                                               malfunction_reason=data['reason']).update(send_times=F('send_times') + 1)
        return Response(status=status.HTTP_200_OK)
