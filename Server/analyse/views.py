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


"""
========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
API
========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
"""


#  能源发展热力图
@api_view(['GET', ])
@permission_classes(())
def get_heat_map(request, id=12):
    if request.method == 'GET':
        data_objects = HeatMapModel.objects.filter(province=methods.region_dict(num=id)).all()
        data = HeatMapSerializer(instance=data_objects, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  能源产能及结构
@api_view(['GET', ])
@permission_classes(())
def get_capacity_structure(request, id=12):
    if request.method == 'GET':
        data_objects = CapacityStructureModel.objects.filter(province=methods.region_dict(num=id)).first()
        data = CapacityStructureSerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  能源消耗水平
@api_view(['GET', ])
@permission_classes(())
def get_consumption(request, id=12):
    if request.method == 'GET':
        data_objects = ConsumptionModel.objects.filter(province=methods.region_dict(num=id)).first()
        data = ConsumptionSerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)
