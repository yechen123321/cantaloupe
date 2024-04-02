import random
from decimal import Decimal

from .models import *
from rest_framework import serializers


#  矿产能源
class MineralDevelopmentSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = MineralDevelopmentModel
        fields = ['name', 'data']

    mineral_type = ['煤炭', '石油', '天然气', '煤层气', '页岩气', '铁矿', '锰矿', '铬铁矿']
    mineral_type_dict = {
        0: 'coal',
        1: 'petroleum',
        2: 'gas',
        3: 'coalbed_methane',
        4: 'shale_gas',
        5: 'iron',
        6: 'manganese',
        7: 'ferrochrome'
    }

    def get_name(self, obj):
        name_list = []

        for i in range(len(self.mineral_type)):
            name_list.append(self.mineral_type[i])
        return name_list

    def get_data(self, obj):
        data_list = [[]]
        for it in range(2016, 2023):
            data_list[0].append(f'{it}年')

        for it in range(len(self.mineral_type)):
            data_list.append([])
            for year in range(2016, 2023):
                data_list[it + 1].append(
                    list(MineralDevelopmentModel.objects.filter(year=year,
                                                                region=self.context.get('region')).values_list(
                        self.mineral_type_dict[it], flat=True))
                )

        return data_list


#  能源进出口量
class EnergyImportAndExportSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyImportAndExportModel
        fields = ['name', 'data']

    year = list(EnergyImportAndExportModel.objects.values_list('year', flat=True))

    def get_name(self, obj):
        return self.year

    def get_data(self, obj):
        data_dict = [{'name': '进口', 'data': {'石油': [], '煤炭': [], '电力': []}}, {'name': '出口', 'data': {'石油': [], '煤炭': [], '电力': []}}]

        field_names_map = {
            'petroleum_i': '石油',
            'coal_i': '煤炭',
            'power_i': '电力',
            'petroleum_e': '石油',
            'coal_e': '煤炭',
            'power_e': '电力'
        }

        for year_i in self.year:
            data = EnergyImportAndExportModel.objects.filter(year=year_i).first()
            if data:
                for field_name, verbose_name in field_names_map.items():
                    value = getattr(data, field_name)
                    if field_name[-1] == 'i':
                        data_dict[0]['data'][verbose_name].append(value)
                    else:
                        data_dict[1]['data'][verbose_name].append(value)
        return data_dict


#  发电装机容量
class PowerGenerationInstalledCapacitySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = PowerGenerationInstalledCapacityModel
        fields = ['name', 'data']

    year = list(PowerGenerationInstalledCapacityModel.objects.values_list('year', flat=True))

    def get_name(self, obj):
        # year = obj.year
        return self.year

    def get_data(self, obj):
        data_dict = {'火电': [], '水电': [], '核电': [], '风力': [], '太阳能发电': [], '其他': []}

        field_names_map = {
            'thermal_power': '火电',
            'hydropower': '水电',
            'nuclear_power': '核电',
            'wind_power': '风力',
            'solar_power_generation': '太阳能发电',
            'other_power': '其他'
        }

        for year_i in self.year:
            data = PowerGenerationInstalledCapacityModel.objects.filter(year=year_i).first()
            if data:
                for field_name, verbose_name in field_names_map.items():
                    value = getattr(data, field_name)
                    data_dict[verbose_name].append(value)

        return data_dict


#  能源平衡总和
class EnergyProductionAndInventorySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyProductionAndInventoryModel
        fields = ['name', 'data']

    year = list(EnergyProductionAndInventoryModel.objects.values_list('year', flat=True))

    def get_name(self, obj):
        # year = obj.year
        return self.year[3:]

    def get_data(self, obj):
        data_dict = {'存量': [], '产量': [], '产量增长率': []}

        field_names_map = {
            'total_energy_available_for_consumption': '存量',
            'total_production_of_primary_energy': '产量',
        }

        for year_i in self.year[3:]:
            data = EnergyProductionAndInventoryModel.objects.filter(year=year_i).first()
            if data:
                for field_name, verbose_name in field_names_map.items():
                    value = getattr(data, field_name)
                    data_dict[verbose_name].append(value / 1000)
                last_data = EnergyProductionAndInventoryModel.objects.filter(year=year_i - 1).first()
                if last_data:
                    increase = round((
                                             data.total_production_of_primary_energy - last_data.total_production_of_primary_energy) / last_data.total_production_of_primary_energy,
                                     5) * 100
                else:
                    increase = round(random.uniform(0, 0.03), 5) * 100

                data_dict['产量增长率'].append(increase)

        return data_dict


#  能源消耗水平
class EnergyConsumptionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyConsumptionModel
        fields = ['name', 'data']

    year = list(EnergyConsumptionModel.objects.values_list('year', flat=True))

    def get_name(self, obj):
        # year = obj.year
        return self.year[self.year.index(2017):]

    def get_data(self, obj):
        data_dict = {'能源消费总量': [], '煤炭占比': [], '石油占比': [], '天然气占比': [], '一次电力及其他能源': [],
                     '全国能耗降低率': [], '全国GDP': []}

        field_names_map = {
            'total_energy_consumption': '能源消费总量',
            'coal': '煤炭占比',
            'petroleum': '石油占比',
            'natural_gas': '天然气占比',
            'power_and_other': '一次电力及其他能源',
        }

        for year_i in self.year[self.year.index(2017):]:
            data = EnergyConsumptionModel.objects.filter(year=year_i).first()
            if data:
                for field_name, verbose_name in field_names_map.items():
                    value = getattr(data, field_name)
                    data_dict[verbose_name].append(value)
                last_data = EnergyConsumptionModel.objects.filter(year=year_i - 1).first()
                if last_data:
                    decrease = round((
                                             data.total_energy_consumption - last_data.total_energy_consumption) / last_data.total_energy_consumption,
                                     5) * 100
                else:
                    decrease = round(random.uniform(0, 0.03), 5) * 100

                data_dict['全国能耗降低率'].append(decrease)
        gdps = [83.2, 91.93, 98.65, 101.36, 114.36, 120.47]  # 2017 ~ 2022
        for gdp in gdps:
            data_dict['全国GDP'].append(gdp)

        return data_dict


#  新能源结构及趋势
class NewEnergySerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = NewEnergyModel
        fields = ['data']

    def get_data(self, obj):
        data_dict = {'太阳能源': [], '风力能源': [], '水利能源': [], '生物质能': [], '其他能源': []}

        field_names_list = [
            '太阳能源',
            '风力能源',
            '水利能源',
            '生物质能',
            '其他能源',
        ]
        data_dict['年份'] = NewEnergyModel.objects.values_list('year', flat=True).distinct().order_by('year')

        for year_i in data_dict['年份']:
            sum_data = 0
            for field_name in field_names_list:
                data_obj = NewEnergyModel.objects.filter(year=year_i, energy_type=field_name).values_list('value')
                for data in data_obj:
                    sum_data += float(data[0])
            t = round(random.uniform(2900.0, 3600.0), 1)
            sum_data += t
            for field_name in field_names_list:
                data_obj = NewEnergyModel.objects.filter(year=year_i, energy_type=field_name).values_list('value')
                for data in data_obj:
                    data_dict[field_name].append(round(data[0] / Decimal(str(sum_data)) * 100, 2))
            data_dict['其他能源'].append(round(Decimal(str(t)) / Decimal(str(sum_data)) * 100, 2))

        return data_dict


#  全国市场交易及投资建设
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
        return getattr(MarketInvestmentModel.objects.order_by('-year').first(), 'year')

    def get_name(self, obj):
        name_list = []
        field_name_list = MarketInvestmentModel._meta.get_fields()
        for field in field_name_list:
            if field.name == 'year' or field.name == 'created_at' or field.name == 'id':
                continue
            name_list.append(field.verbose_name)
        return name_list

    def get_number(self, obj):
        number_list = []
        data_obj = MarketInvestmentModel.objects.filter(year=self.get_year(obj)).first()
        field_list = MarketInvestmentModel._meta.get_fields()
        for field in field_list:
            if field.name == 'year' or field.name == 'created_at' or field.name == 'id':
                continue
            data = getattr(data_obj, field.name)
            if data:
                number_list.append(round(data, 0))
        return number_list

    def get_up(self, obj):
        up_list = []
        up_map = {
            'energy_investment': '亿元',
            'new_energy_storage_projects_power': '万千瓦',
            'new_energy_storage_projects': '万千瓦时',
            'electricity_trading': '百亿千瓦时',
            'coal_methane': '亿立方米'
        }
        field_list = MarketInvestmentModel._meta.get_fields()
        for field in field_list:
            if field.name == 'year' or field.name == 'created_at' or field.name == 'id':
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
            if field.name == 'year' or field.name == 'created_at' or field.name == 'id':
                continue
            data = getattr(data_obj, field.name)
            next_data = getattr(next_obj, field.name)
            num_list.append(round((data - next_data) / next_data * 100, 1))
        return num_list


#  全国能源开发与需求
class EnergyDevelopAndDemandSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyDevelopAndDemandModel
        fields = ['name', 'data']

    def get_name(self, obj):
        name_list = ['地区开发', '地区消耗']
        return name_list

    def get_data(self, obj):
        data_dict = {'地区开发': [], '地区消耗': []}

        data_obj = EnergyDevelopAndDemandModel.objects.order_by('-year').first()

        field_list = EnergyDevelopAndDemandModel._meta.get_fields()
        for field in field_list:
            if field.name != 'id' and field.name != 'created_at':
                data = getattr(data_obj, field.name)
                if '_dv' in field.name:
                    #  地区开发
                    data_dict['地区开发'].append({'value': data, 'name': field.verbose_name})
                elif '_dm' in field.name:
                    #  地区消耗
                    data_dict['地区消耗'].append({'value': data, 'name': field.verbose_name})
        return data_dict


#  全国能源储量统计
class EnergyReserveSerializer(serializers.ModelSerializer):
    indicator = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['indicator', 'data']

    def get_indicator(self, obj):
        name_list = []
        field_name_list = EnergyReserveModel._meta.get_fields()
        for field in field_name_list:
            data_dict = {}
            if field.name == 'year' or field.name == 'created_at' or field.name == 'id' or field.name == 'range':
                continue
            data_dict['name'] = field.verbose_name
            data_dict['max'] = round(max(EnergyReserveModel.objects.values_list(field.name, flat=True)) * Decimal(str(random.uniform(1.1, 1.2))), 2)
            name_list.append(data_dict)

        return name_list

    def get_data(self, obj):
        data_dict = {'国内总量': [], '世界平均': []}

        data_obj1 = EnergyReserveModel.objects.filter(range='全国').order_by('-year').first()
        data_obj2 = EnergyReserveModel.objects.filter(range='全球').order_by('-year').first()

        field_list = EnergyReserveModel._meta.get_fields()
        for field in field_list:
            if not (field.name == 'year' or field.name == 'created_at' or field.name == 'id' or field.name == 'range'):
                data = getattr(data_obj1, field.name)
                #  全国
                data_dict['国内总量'].append(data * Decimal(str(1.45)))
                #  世界
                data = getattr(data_obj2, field.name)
                data_dict['世界平均'].append(round(data / Decimal(str(1.43)), 2))
        return data_dict