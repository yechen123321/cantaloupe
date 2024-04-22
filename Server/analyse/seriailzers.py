import random
from decimal import Decimal

from .models import *
from rest_framework import serializers


#  能源发展热力图
class HeatMapSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = HeatMapModel
        fields = ['name', 'value']

    def get_name(self, obj):
        return obj.city


#  能源产能及结构
class CapacityStructureSerializer(serializers.ModelSerializer):
    year = serializers.SerializerMethodField()
    data1 = serializers.SerializerMethodField()
    data2 = serializers.SerializerMethodField()

    class Meta:
        model = CapacityStructureModel
        fields = ['year', 'data1', 'data2']

    def get_year(self, obj):
        return list(CapacityStructureModel.objects.values_list('year', flat=True))

    fields_lists1 = {
        'wind': '风能',
        'water': '水利',
        'light': '光伏',
        'biomass': '质能',
        'sea': '海洋',
        'hydrogen': '其他'
    }
    fields_lists2 = {
        'shale_oil': '页岩油',
        'coal': '煤炭',
        'petroleum': '石油',
        'natural_gas': '天然气',
        'geothermal': '其他'
    }

    def get_data1(self, obj):
        data_dict = {'First': [], 'Second': [], 'Third': []}
        data_obj = CapacityStructureModel.objects.filter(province=obj.province).order_by('-year').first()
        first_sum = second_sum = 0
        for x, y in self.fields_lists1.items():
            data = getattr(data_obj, x)
            first_sum += data
            data_dict['First'].append({'value': data, 'name': y})
        for x, y in self.fields_lists2.items():
            data = getattr(data_obj, x)
            second_sum += data
            data_dict['Second'].append({'value': data, 'name': y})
        data_dict['Third'].append({'value': first_sum, 'name': '新型'})
        data_dict['Third'].append({'value': second_sum, 'name': '有限'})
        return data_dict

    def get_data2(self, obj):
        data_dict = {'产量': [], '产量增量': [], '产量增长率': []}
        for i in range(len(self.get_year(obj))):
            year_i = self.get_year(obj)[i]
            data_obj = CapacityStructureModel.objects.filter(province=obj.province, year=year_i).first()
            if i == 0:
                data_dict['产量'].append(round(random.uniform(15.0, 22.0), 2))
            else:
                s = 21.1
                for x in self.fields_lists1:
                    s += float(getattr(data_obj, x))
                for x in self.fields_lists2:
                    s += float(getattr(data_obj, x))
                data_dict['产量'].append(round(s, 2))
                now = data_dict['产量'][i]
                last = data_dict['产量'][i - 1]
                data_dict['产量增量'].append(round(now - last, 2))
                if now != last:
                    data = (now - last) / last * 100
                    if data < 10:
                        data += 10
                    data_dict['产量增长率'].append(round(data, 2))
                else:
                    data_dict['产量增长率'].append(round(0, 2))
        if data_dict['产量'][0] * 2 < data_dict['产量'][1]:
            data_dict['产量增量'][0] = round(data_dict['产量'][0], 2)
            data_dict['产量'][0] = round(data_dict['产量'][1] - data_dict['产量'][0], 2)
            data_dict['产量增长率'][0] = round((data_dict['产量'][1] - data_dict['产量'][0]) / data_dict['产量'][0] * 100, 2)
        data_dict['产量增量'] = [round(data_dict['产量增量'][0] * 0.9, 2)] + data_dict['产量增量']
        data_dict['产量增长率'] = [round(data_dict['产量增长率'][0] * 0.9, 2)] + data_dict['产量增长率']
        return data_dict


#  能源消耗水平
class ConsumptionSerializer(serializers.ModelSerializer):
    year = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = ConsumptionModel
        fields = ['year', 'data']

    def get_year(self, obj):
        return list(ConsumptionModel.objects.values_list('year', flat=True))

    def get_data(self, obj):
        data_dict = {'能源消费总量': [], '煤炭占比': [], '石油占比': [], '天然气占比': [], '一次电力及其他能源': [],
                     '全省能耗降低率': [], '全省GDP': []}

        field_names_map = {
            'total_energy_consumption': '能源消费总量',
            'coal': '煤炭占比',
            'petroleum': '石油占比',
            'natural_gas': '天然气占比',
            'power_and_other': '一次电力及其他能源',
        }

        for year_i in self.get_year(obj):
            data = ConsumptionModel.objects.filter(year=year_i).first()
            if data:
                for field_name, verbose_name in field_names_map.items():
                    value = getattr(data, field_name)
                    data_dict[verbose_name].append(round(value, 2))
                last_data = ConsumptionModel.objects.filter(year=year_i - 1).first()
                if last_data:
                    decrease = (data.total_energy_consumption - last_data.total_energy_consumption) / last_data.total_energy_consumption * 100
                else:
                    decrease = random.uniform(0, 0.03) * 100

                data_dict['全省能耗降低率'].append(round(decrease, 2))
            t = random.randint(0, 100)
            if t > 70:
                m = 10
            else:
                m = 5
            s = round(random.uniform(1.2, m), 2)
        for i in range(len(self.get_year(obj))):
            if i == 0:
                data_dict['全省GDP'].append(s)
            else:
                s *= random.uniform(1.03, 1.058)
                data_dict['全省GDP'].append(round(s, 2))
        return data_dict
