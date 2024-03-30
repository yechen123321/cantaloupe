import random

from .models import *
from rest_framework import serializers


#  主要能源品种产量
class MainEnergyProductionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = MainEnergyProductionModel
        fields = ['name', 'data']

    def get_name(self, obj):
        return obj.region

    def get_data(self, obj):
        data_dict = {'水生电能': 0, '光生电能': 0, '风生电能': 0}
        field_names_map = {
            'water_power': '水生电能',
            'sun_power': '光生电能',
            'wind_power': '风生电能'
        }

        data_obj = MainEnergyProductionModel.objects.filter(region=obj.region).order_by('-year').first()
        if data_obj:
            for field_name, verbose_name in field_names_map.items():
                value = getattr(data_obj, field_name)
                data_dict[verbose_name] = value
        return data_dict


#  电场故障信息
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

    def update(self, instance, validated_data):
        """更新，instance为要更新的对象实例"""
        # 需要返回 instance
        return instance

