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
        name_list = [self.year, self.type]
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


#  地区再生能源结构
class EnergyStructureSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['data']

    type = ['风能', '水利', '光伏', '质能', '其他']
    field_map = {
        '光伏': 'light',
        '水利': 'water',
        '风能': 'wind',
        '质能': 'biomass_energy',
    }
    other_map = {
        '地热': 'geothermal',
        '海洋': 'sea'
    }

    def get_data(self, obj):
        data_dict = {'地区开发': [], '地区消耗': []}

        data_obj = EnergyReserveModel.objects.order_by('year').first()
        if data_obj:
            for x, y in self.field_map.items():
                t_dict = {'name': x, 'value': getattr(data_obj, y + '_pro')}
                data_dict['地区开发'].append(t_dict)
            other_data = 0
            for x, y in self.other_map.items():
                other_data += getattr(data_obj, y + '_pro')
            data_dict['地区开发'].append({'name': '其他', 'value': other_data})

            for x, y in self.field_map.items():
                t_dict = {'name': x, 'value': getattr(data_obj, y + '_res')}
                data_dict['地区消耗'].append(t_dict)
            other_data = 0
            for x, y in self.other_map.items():
                other_data += getattr(data_obj, y + '_res')
            data_dict['地区消耗'].append({'name': '其他', 'value': other_data})
        return data_dict


#  地区再生能源产能
class EnergyCapacitySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['name', 'data']

    year = list(EnergyReserveModel.objects.order_by('year').values_list('year', flat=True))
    type = ['光能', '水能', '风能', '生物质能', '氢能', '海洋', '地热']
    field_map = {
        '光能': 'light_pro',
        '水能': 'water_pro',
        '风能': 'wind_pro',
        '生物质能': 'biomass_energy_pro',
        '氢能': 'hydrogen',
        '海洋': 'sea_pro',
        '地热': 'geothermal_pro',
    }

    def get_name(self, obj):
        return self.type

    def get_data(self, obj):
        data_dict = {'年份': self.year}
        for it in self.type:
            data_dict[it] = []
            t = self.field_map[it]
            for year_i in self.year:
                data_obj = getattr(EnergyReserveModel.objects.filter(year=year_i).first(), t)
                data_dict[it].append(data_obj)
        return data_dict


#  地区再生能源排行
class EnergyRankingSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['data']

    year = list(EnergyReserveModel.objects.order_by('year').values_list('year', flat=True))
    type = ['太阳能', '水能', '风能', '生物质能', '氢能', '海洋能', '地热能', '核能', '沼气']
    rank = [800, 700, 600, 500, 450, 400, 300, 200]

    def get_data(self, obj):
        data_list = []
        random.shuffle(self.type)
        for i in range(len(self.type) - 1):
            t = {'name': self.type[i], 'value': self.rank[i]}
            data_list.append(t)
        return data_list


#  地区再生能源储量概况
class EnergyReserveGeneralSerializer(serializers.ModelSerializer):
    indicator = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['indicator', 'data']

    def get_indicator(self, obj):
        name_list = []
        field_name_list = EnergyReserveModel._meta.get_fields()
        for it in field_name_list:
            print(it)
        for field in field_name_list:
            data_dict = {}
            if '_res' not in field.name:
                continue
            data_dict['name'] = field.verbose_name
            data_dict['max'] = round(max(EnergyReserveModel.objects.values_list(field.name, flat=True)) * Decimal(
                str(random.uniform(1.1, 1.2))), 2)
            name_list.append(data_dict)
        return name_list

    def get_data(self, obj):
        data_dict = {'全国平均': [], '省内总量': [], '发展占比': None}

        data_obj = EnergyReserveModel.objects.order_by('-year').first()

        field_list = EnergyReserveModel._meta.get_fields()
        for field in field_list:
            if '_res' in field.name:
                data = getattr(data_obj, field.name)
                data_dict['全国平均'].append(data * Decimal(str(1.45)))
                data = getattr(data_obj, field.name)
                data_dict['省内总量'].append(round(data / Decimal(str(1.43)), 2))
        data_dict['发展占比'] = str(random.randint(65, 85)) + '%'
        return data_dict
