from decimal import Decimal
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


#  能源设施
class RegionalResourceFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionalResourceFacilitiesModel
        fields = ['name', 'do', 'number', 'up', 'when']


#  地区再生能源储量
class EnergyReserveSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['name', 'data']

    year = list(EnergyReserveModel.objects.order_by('year').values_list('year', flat=True))
    type = ['风能', '水利', '光伏', '质能', '其他']
    field_map = {
        '风能': 'wind_res',
        '水利': 'water_res',
        '光伏': 'light_res',
        '质能': 'biomass_energy_res'
    }

    def get_name(self, obj):
        name_list = []
        name_list.append(self.year)
        name_list.append(
            self.type
        )
        return name_list

    def get_data(self, obj):
        data_dict = {}
        for it in self.type:
            data_dict[it] = []
        for year_i in self.year:
            data_obj = EnergyReserveModel.objects.filter(year=year_i).first()
            if data_obj:
                for field_name, field in self.field_map.items():
                    value = getattr(data_obj, field)
                    data_dict[field_name].append(value)
            data_obj_other = EnergyReserveModel.objects.filter(year=year_i).first()
            if data_obj_other:
                value = getattr(data_obj_other, 'geothermal_res') + getattr(data_obj_other, 'sea_res')
                data_dict['其他'].append(value)

        return data_dict