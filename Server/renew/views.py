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

from django.views.decorators.cache import cache_page

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


#  主要能源品种产量
@api_view(['GET', ])
@permission_classes(())
def get_region_energy_production(request, id=12):
    if request.method == 'GET':
        data_objects = MainEnergyProductionModel.objects.filter(region=methods.region_dict(id)).first()
        data = MainEnergyProductionSerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  地区资源设施使用情况
@api_view(['GET', ])
@permission_classes(())
@extend_schema(responses=RegionalResourceFacilitiesSerializer)
def get_regional_resource_facilities(request, id=12):
    if request.method == 'GET':
        data_objects = RegionalResourceFacilitiesModel.objects.filter(region=methods.region_dict(id)).all()
        data = RegionalResourceFacilitiesSerializer(instance=data_objects, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  地区再生能源储量
@api_view(['GET', ])
@permission_classes(())
@extend_schema(responses=EnergyReserveSerializer)
def get_energy_reserve(request, id=12):
    if request.method == 'GET':
        data_objects = EnergyReserveModel.objects.filter(province=methods.region_dict(id)).first()
        data = EnergyReserveSerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  地区再生能源结构
@api_view(['GET', ])
@permission_classes(())
@extend_schema(responses=EnergyStructureSerializer)
def get_energy_structure(request, id=12):
    if request.method == 'GET':
        data_objects = EnergyReserveModel.objects.filter(province=methods.region_dict(id)).first()
        data = EnergyStructureSerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  地区再生能源产能
@api_view(['GET', ])
@permission_classes(())
@extend_schema(responses=EnergyCapacitySerializer)
def get_energy_capacity(request, id=12):
    if request.method == 'GET':
        data_objects = EnergyReserveModel.objects.filter(province=methods.region_dict(id)).first()
        data = EnergyCapacitySerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  地区再生能源排行
# @cache_page(10)
@api_view(['GET', ])
@permission_classes(())
@extend_schema(responses=EnergyRankingSerializer)
def get_energy_ranking(request, id=12):
    if request.method == 'GET':
        data_objects = EnergyReserveModel.objects.filter(province=methods.region_dict(id)).first()
        data = EnergyRankingSerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  地区再生能源储量概况
@api_view(['GET', ])
@permission_classes(())
@extend_schema(responses=EnergyReserveGeneralSerializer)
def get_energy_reserve_general(request, id=12):
    if request.method == 'GET':
        data_objects = EnergyReserveModel.objects.filter(province=methods.region_dict(id)).first()
        data = EnergyReserveGeneralSerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)