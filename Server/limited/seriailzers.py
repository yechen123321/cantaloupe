import random
from decimal import Decimal

from .models import *
from rest_framework import serializers


#  地区有限能源经济形势
class MarketInvestmentSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    number = serializers.SerializerMethodField()
    up = serializers.SerializerMethodField()
    num = serializers.SerializerMethodField()

    class Meta:
        model = MarketInvestmentModel
        fields = ['year', 'name', 'number', 'up', 'num']

    def get_year(self, obj):
        #  最新一年
        return getattr(MarketInvestmentModel.objects.order_by('-year')[0], 'year')

    def get_name(self, obj):
        name_list = []
        field_name_list = MarketInvestmentModel._meta.get_fields()
        for field in field_name_list:
            if field.name == 'year' or field.name == 'created_at' or field.name == 'id' or field.name == 'province':
                continue
            name_list.append(field.verbose_name)
        return name_list

    def get_number(self, obj):
        number_list = []
        data_obj = MarketInvestmentModel.objects.filter(year=self.get_year(obj)).first()
        field_list = MarketInvestmentModel._meta.get_fields()
        for field in field_list:
            if field.name == 'year' or field.name == 'created_at' or field.name == 'id' or field.name == 'province':
                continue
            data = getattr(data_obj, field.name)
            if data:
                number_list.append(data)
        return number_list

    def get_up(self, obj):
        up_list = []
        up_map = {
            'natural_gas': '亿立方米',
            'coal': '千万吨',
            'coal_methane': '亿立方米',
        }
        field_list = MarketInvestmentModel._meta.get_fields()
        for field in field_list:
            if field.name == 'year' or field.name == 'created_at' or field.name == 'id' or field.name == 'province':
                continue
            up_list.append(up_map[field.name])
        return up_list

    def get_num(self, obj):
        num_list = []
        #  同比增长
        data_obj = MarketInvestmentModel.objects.order_by('-year').first()
        next_obj = MarketInvestmentModel.objects.order_by('-year')[1]
        field_list = MarketInvestmentModel._meta.get_fields()
        for field in field_list:
            if field.name == 'year' or field.name == 'created_at' or field.name == 'id' or field.name == 'province':
                continue
            data = getattr(data_obj, field.name)
            next_data = getattr(next_obj, field.name)
            num_list.append(round((data - next_data) / next_data * 100, 1))
        return num_list


#  地区不可再生能源结构
class EnergyStructureSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['data']

    type = ['石油', '天然气', '煤炭', '核能', '其他']
    field_map = {
        '石油': 'petroleum',
        '天然气': 'natural_gas',
        '煤炭': 'coal',
        '核能': 'nuclear',
        '其他': 'other'
    }

    def get_data(self, obj):
        data_dict = {'地区开发': [], '地区消耗': []}

        data_obj = EnergyReserveModel.objects.filter(province=obj.province).order_by('-year').first()
        if data_obj:
            for x, y in self.field_map.items():
                data_dict['地区开发'].append({'value': getattr(data_obj, y + '_pro'), 'name': x})
                data_dict['地区消耗'].append({'value': getattr(data_obj, y + '_res'), 'name': x})
        return data_dict


#  地区不可再生能源产能
class EnergyCapacitySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['name', 'data']

    type = ['石油', '天然气', '煤炭', '核能', '其他']
    field_map = {
        '石油': 'petroleum_pro',
        '天然气': 'natural_gas_pro',
        '煤炭': 'coal_pro',
        '核能': 'nuclear_pro',
        '其他': 'other_pro'
    }

    def get_name(self, obj):
        return self.type

    def get_data(self, obj):
        year = list(
            EnergyReserveModel.objects.filter(province=obj.province).order_by('year').values_list('year', flat=True))
        data_dict = {'年份': year}
        for x, y in self.field_map.items():
            data_dict[x] = []
            for year_i in year:
                data_obj = getattr(EnergyReserveModel.objects.filter(province=obj.province, year=year_i).first(), y)
                data_dict[x].append(data_obj)
        return data_dict


#  地区不可再生能源储量概况
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
            data_dict['max'] = round(max(EnergyReserveModel.objects.filter(province=obj.province).values_list(field.name, flat=True)) * Decimal(
                str(random.uniform(1.1, 1.2))), 2)
            name_list.append(data_dict)
        return name_list

    def get_data(self, obj):
        data_dict = {'全国平均': [], '省内总量': [], '发展占比': None}

        data_obj = EnergyReserveModel.objects.filter(province=obj.province).order_by('-year').first()
        field_list = EnergyReserveModel._meta.get_fields()
        for field in field_list:
            if '_res' in field.name:
                data = getattr(data_obj, field.name)
                data_dict['全国平均'].append(data * Decimal(str(1.45)))
                data = getattr(data_obj, field.name)
                data_dict['省内总量'].append(round(data / Decimal(str(1.43)), 2))
        data_dict['发展占比'] = str(random.randint(65, 85)) + '%'
        return data_dict


#  地区不可再生能源储能图
class EnergyReserveSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['name', 'data']

    type = ['石油', '天然气', '煤炭', '核能', '其他']
    field_map = {
        '石油': 'petroleum',
        '天然气': 'natural_gas',
        '煤炭': 'coal',
        '核能': 'nuclear',
        '其他': 'other'
    }

    def get_name(self, obj):
        year = list(
            EnergyReserveModel.objects.filter(province=obj.province).order_by('year').values_list('year', flat=True))
        name_list = [year, self.type]
        return name_list

    def get_data(self, obj):
        year = list(
            EnergyReserveModel.objects.filter(province=obj.province).order_by('year').values_list('year', flat=True))
        data_dict = {'储量': [], '供量': [], '储量增长率': [], '供量增长率': []}

        for i in range(len(year)):
            data_obj = EnergyReserveModel.objects.filter(province=obj.province, year=year[i]).first()
            if data_obj:
                sum_res = sum_pro = 0
                for field_name, field in self.field_map.items():
                    sum_res += getattr(data_obj, field + '_res')
                    sum_pro += getattr(data_obj, field + '_pro')
                data_dict['储量'].append(sum_res)
                data_dict['供量'].append(sum_pro)
            if i == 0:
                data_dict['储量增长率'].append(round(random.uniform(10.0, 25.0), 1))
                data_dict['供量增长率'].append(round(random.uniform(10.0, 25.0), 1))
            else:
                data_dict['储量增长率'].append((data_dict['储量'][i] - data_dict['储量'][i - 1]) / data_dict['储量'][i - 1] * 100)
                data_dict['供量增长率'].append((data_dict['供量'][i] - data_dict['供量'][i - 1]) / data_dict['供量'][i - 1] * 100)
        return data_dict


#  地区不可再生能源开采效率
class ExtractionEfficiencySerializer(serializers.ModelSerializer):
    year = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = ExtractionEfficiencyModel
        fields = ['year', 'data']

    def get_year(self, obj):
        year = list(
            ExtractionEfficiencyModel.objects.filter(province=obj.province).order_by('year').values_list('year', flat=True))
        return year

    def get_data(self, obj):
        year = list(
            ExtractionEfficiencyModel.objects.filter(province=obj.province).order_by('year').values_list('year', flat=True))
        data_dict = {'开采耗费': [], '获取能量': [], '能耗降低率': []}
        for i in range(len(year)):
            data_obj = ExtractionEfficiencyModel.objects.filter(province=obj.province, year=year[i]).first()
            data_dict['开采耗费'].append(getattr(data_obj, 'cost'))
            data_dict['获取能量'].append(getattr(data_obj, 'get'))

            if i == 0:
                data_dict['能耗降低率'].append(round(random.uniform(0.5, 2.5), 1))
            else:
                now = data_dict['开采耗费'][i] - data_dict['获取能量'][i]
                last = data_dict['开采耗费'][i - 1] - data_dict['获取能量'][i - 1]
                t = round((last - now) / last, 1)
                if t < 0:
                    t = -t
                data_dict['能耗降低率'].append(t)

        return data_dict
