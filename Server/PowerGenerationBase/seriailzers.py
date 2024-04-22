import random

from .models import *
from rest_framework import serializers


class my_methods:
    @staticmethod
    def province_dict():
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
        return s


#  电场故障信息GET
class ElectricFieldFaultSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    reason = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()

    class Meta:
        model = ElectricFieldFaultModel
        fields = ['name', 'reason', 'time']

    def get_name(self, obj):  # 故障电厂名称
        return obj.electric_field.station_name

    def get_reason(self, obj):  # 故障原因
        return obj.malfunction_reason

    def get_time(self, obj):  # 故障时间（即创建时间）
        return obj.created_at


#  电场故障信息PUT
class ElectricFieldFaultSerializerPUT(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    reason = serializers.SerializerMethodField()

    class Meta:
        model = ElectricFieldFaultModel
        fields = ['name', 'reason']

    def get_name(self, obj):
        return obj.electric_field.station_name

    def get_reason(self, obj):
        return obj.malfunction_reason


#  地区基地分布
class BaseDistributionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = BaseDistributionModel
        fields = ['name', 'value', 'thing']

    def get_name(self, obj):
        return obj.electric_field.city


#  地区电场运行状况
class OperationStatusSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        fields = ['data']
        model = BaseDistributionModel

    def get_data(self, obj):
        province = obj.electric_field.province
        name_list = list(
            BaseDistributionModel.objects.filter(electric_field__city__in=my_methods.province_dict()[province]).values_list('electric_field__station_name', flat=True))
        data_dict = {'name': random.sample(name_list, min(4, len(name_list))), 'thing': []}
        for i in range(len(data_dict['name'])):
            data = BaseDistributionModel.objects.filter(electric_field__station_name=data_dict['name'][i]).values_list('electric_field__state').first()
            if data[0]:
                data_dict['thing'].append('正常运行')
            else:
                data_dict['thing'].append('运行异常')
        return data_dict


#  地区基地设备运行相关信息
class BaseEquipmentWorkingInformationSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    manage = serializers.SerializerMethodField()

    class Meta:
        model = BaseEquipmentWorkingInformationModel
        fields = ['name', 'type', 'state', 'manage', 'when']

    def get_name(self, obj):
        return obj.device_name

    def get_type(self, obj):
        return obj.device_type

    def get_state(self, obj):
        return obj.device_state

    def get_manage(self, obj):
        return obj.device_information
