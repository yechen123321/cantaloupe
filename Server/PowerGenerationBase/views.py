import json
from random import shuffle

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


class my_methods:
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
                '石景山', '房山', '通州', '顺义', '昌平', '大兴', '怀柔', '平谷', '延庆', '密云', '西城', '海淀',
                '朝阳', '丰台', '门头沟'
            ],
            '浙江': [
                '杭州', '宁波', '温州', '绍兴', '湖州', '嘉兴', '金华', '衢州', '台州', '丽水', '舟山'
            ],
            '重庆': [
                '渝中', '大渡口', '江北', '南岸', '北碚', '巴南', '九龙坡', '南川', '江津', '永川', '合川', '綦江',
                '潼南', '铜梁', '万盛'
            ],
            '西藏': [
                '拉萨', '昌都', '日喀则'],
            '四川': [
                '成都', '绵阳', '自贡', '攀枝花', '泸州', '德阳', '广元', '遂宁', '内江', '乐山', '资阳', '宜宾',
                '南充', '达州', '雅安', '广安', '巴中', '眉山'
            ],
            '山东': [
                '济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁', '泰安', '威海', '日照', '滨州', '德州',
                '聊城', '临沂', '菏泽'
            ],
            '上海': [
                '黄浦', '徐汇', '长宁', '静安', '普陀', '虹口', '杨浦', '闵行', '宝山', '嘉定', '浦东新区', '金山',
                '松江', '青浦', '奉贤', '崇明'
            ],
            '广东': [
                '深圳', '广州', '珠海', '东莞', '佛山', '中山', '惠州', '汕头', '江门', '湛江', '肇庆', '梅州', '茂名',
                '阳江', '清远', '韶关', '揭阳', '汕尾', '潮州', '河源', '云浮'
            ],
            '广西': [
                '南宁', '柳州', '桂林', '梧州', '北海', '崇左', '来宾', '贺州', '玉林', '百色', '河池', '钦州',
                '防城港', '贵港'
            ],
            '安徽': [
                '合肥', '芜湖', '蚌埠', '淮北', '亳州', '宿州', '阜阳', '淮南', '滁州', '六安', '马鞍山', '宣城',
                '铜陵', '池州', '安庆', '黄山'
            ]
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
        fault_data = list(ElectricFieldModel.objects.filter(province__in=my_methods.province_dict(self=my_methods, num=id),
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


#  地区基地分布
@api_view(['GET', ])
@permission_classes(())
def get_base_distribution(request, id=12, typeNum=0):
    type_list = ['火电厂', '水电厂', '光电场', '风电场']
    if request.method == 'GET':
        data_objects = BaseDistributionModel.objects.filter(electric_field__province=my_methods.region_dict(num=id), electric_field__station_type=type_list[typeNum]).all()
        data = BaseDistributionSerializer(instance=data_objects, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  地区电场运行状况
@api_view(['GET', ])
@permission_classes(())
def get_operation_status(request, id=12, typeNum=0):
    type_list = ['火电厂', '水电厂', '光电场', '风电场']
    if request.method == 'GET':
        data_objects = BaseDistributionModel.objects.filter(electric_field__province=my_methods.region_dict(num=id), electric_field__station_type=type_list[typeNum]).first()
        data = OperationStatusSerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  地区基地设备运行相关信息
@api_view(['GET', ])
@permission_classes(())
def get_base_equipment_working_information(request, id=12, typeNum=0):
    type_list = ['火电厂', '水电厂', '光电场', '风电场']
    if request.method == 'GET':
        data_objects = BaseEquipmentWorkingInformationModel.objects.filter(province=my_methods.region_dict(num=id), type_in=type_list[typeNum]).all()
        data_list = list(data_objects)
        shuffle(data_list)  # 乱序
        data = BaseEquipmentWorkingInformationSerializer(instance=data_list, many=True)
        return Response(data=data.data, status=status.HTTP_200_OK)
