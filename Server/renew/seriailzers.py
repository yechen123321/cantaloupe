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
        return obj.province

    def get_data(self, obj):
        data_dict = {'水生电能': 0, '光生电能': 0, '风生电能': 0}
        field_names_map = {
            'water_power': '水生电能',
            'sun_power': '光生电能',
            'wind_power': '风生电能'
        }

        data_obj = MainEnergyProductionModel.objects.filter(province=obj.province).order_by('-year').first()
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

    type = ['风能', '水利', '光伏', '质能', '其他']
    field_map = {
        '风能': 'wind_res',
        '水利': 'water_res',
        '光伏': 'light_res',
        '质能': 'biomass_energy_res'
    }

    def get_name(self, obj):
        year = list(
            EnergyReserveModel.objects.filter(province=obj.province).order_by('year').values_list('year', flat=True))
        name_list = [year, self.type]
        return name_list

    def get_data(self, obj):
        year = list(
            EnergyReserveModel.objects.filter(province=obj.province).order_by('year').values_list('year', flat=True))
        data_dict = {}
        for it in self.type:
            data_dict[it] = []
        for year_i in year:
            data_obj = EnergyReserveModel.objects.filter(province=obj.province, year=year_i).first()
            if data_obj:
                for field_name, field in self.field_map.items():
                    value = getattr(data_obj, field)
                    data_dict[field_name].append(value)
            data_obj_other = EnergyReserveModel.objects.filter(province=obj.province, year=year_i).first()
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

        data_obj = EnergyReserveModel.objects.filter(province=obj.province).order_by('-year').first()
        if data_obj:
            for x, y in self.field_map.items():
                t_dict = {'value': getattr(data_obj, y + '_pro'), 'name': x}
                data_dict['地区开发'].append(t_dict)
            other_data = 0
            for x, y in self.other_map.items():
                other_data += getattr(data_obj, y + '_pro')
            data_dict['地区开发'].append({'value': other_data, 'name': '其他'})

            for x, y in self.field_map.items():
                t_dict = {'value': getattr(data_obj, y + '_res'), 'name': x}
                data_dict['地区消耗'].append(t_dict)
            other_data = 0
            for x, y in self.other_map.items():
                other_data += getattr(data_obj, y + '_res')
            data_dict['地区消耗'].append({'value': other_data, 'name': '其他'})
        return data_dict


#  地区再生能源产能
class EnergyCapacitySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['name', 'data']

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
        year = list(
            EnergyReserveModel.objects.filter(province=obj.province).order_by('year').values_list('year', flat=True))
        data_dict = {'年份': year}
        for x, y in self.field_map.items():
            data_dict[x] = []
            for year_i in year:
                data_obj = getattr(EnergyReserveModel.objects.filter(province=obj.province, year=year_i).first(), y)
                data_dict[x].append(data_obj)
        return data_dict


#  地区再生能源排行
class EnergyRankingSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['data']

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
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['data']

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
        data_dict['发展占比'] = str(random.randint(60, 85)) + '%'
        return data_dict


#  地区再生能源装机容量
class RenewableEnergyInstallationSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()
    data2 = serializers.SerializerMethodField()

    class Meta:
        model = RenewableEnergyInstallationModel
        fields = ['name', 'data', 'data2']

    field_names_map = {
        'water': '水电装机',
        'wind': '风电装机',
        'sun': '光伏发电',
        'biomass': '生物质发电',
    }

    def get_name(self, obj):
        year = list(
            RenewableEnergyInstallationModel.objects.filter(province=obj.province).order_by('year').values_list('year',
                                                                                                                flat=True))
        return year

    def get_data(self, obj):
        # data_dict = {'水电装机': [], '风电装机': [], '光伏发电': [], '生物质发电': []}
        data_dict = {'现有量': [], '新增量': [], '增长率': []}

        year = list(
            RenewableEnergyInstallationModel.objects.filter(province=obj.province).order_by('year').values_list('year',
                                                                                                                flat=True))
        for year_i in year:
            data = RenewableEnergyInstallationModel.objects.filter(province=obj.province, year=year_i).first()
            if data:
                now_sum = 0
                for field_name, verbose_name in self.field_names_map.items():
                    value = getattr(data, field_name)
                    now_sum += value
                data_dict['现有量'] = now_sum
            t = round(random.uniform(float(now_sum / 2), float(now_sum) * 0.8), 2)
            data_dict['新增量'] = t
            data_dict['增长率'] = round(t / float(now_sum) * 100, 2)
        return data_dict

    def get_data2(self, obj):
        data_list = []
        data_obj = RenewableEnergyInstallationModel.objects.filter(province=obj.province).order_by('-year').first()
        for field_name, verbose_name in self.field_names_map.items():
            value = getattr(data_obj, field_name)
            dic = {'value': value, 'name': verbose_name}
            data_list.append(dic)
        return data_list


#  地区再生能源建设投资
class EnergyConstructionInvestmentSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['name', 'data']

    def get_name(self, obj):
        year = list(
            EnergyReserveModel.objects.filter(province=obj.province).order_by('year').values_list('year', flat=True))
        return year

    def get_data(self, obj):
        data_dict = {'产量': [], '存量': [], '产量增长率': []}

        year = list(
            EnergyReserveModel.objects.filter(province=obj.province).order_by('year').values_list('year', flat=True))
        for i in range(len(year)):
            t = round(random.uniform(float(80.00), float(210.00)), 1)
            data_dict['存量'].append(t)
            data_dict['产量增长率'].append(round(random.uniform(10.0, 25.0), 1))
        data_dict['产量'].append(round(random.uniform(50.0, 120.0), 1))
        for i in range(len(year) - 1):
            value = round(data_dict['产量'][i] * (data_dict['产量增长率'][i] / 100 + 1), 1)
            data_dict['产量'].append(value)

        return data_dict


#  地区分种类发电储能
class ClassificationCapacitySerializer(serializers.ModelSerializer):
    year = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['year', 'data']

    def get_year(self, obj):
        year = list(
            EnergyReserveModel.objects.filter(province=obj.province).order_by('year').values_list('year', flat=True))
        return year

    def get_data(self, obj):
        data_dict = {'水力发电量': {}, '太阳能发电量': {}, '风力发电量': {}}
        fields = [field.name for field in EnergyReserveModel._meta.fields if not field.auto_created]
        for x in data_dict:
            data_dict[x] = {'增长量': [], '现有量': [], '增长率': []}
            for i in range(len(self.get_year(obj))):
                year_i = self.get_year(obj)[i]
                data_obj = EnergyReserveModel.objects.filter(province=obj.province, year=year_i).first()
                pro_sum = res_sum = 0.0
                for y in fields:
                    if '_pro' in y:
                        pro_sum += float(getattr(data_obj, y))
                    elif '_res' in y:
                        res_sum += float(getattr(data_obj, y))
                data_dict[x]['增长量'].append(round(pro_sum, 2))
                data_dict[x]['现有量'].append(round(res_sum, 2))
                if i == 0:
                    data_dict[x]['增长率'].append(round(random.uniform(15.0, 22.0), 2))
                else:
                    now = data_dict[x]['现有量'][i]
                    last = data_dict[x]['现有量'][i - 1]
                    data = (now - last) / last * 100
                    if data < 10:
                        data += 10
                    data_dict[x]['增长率'].append(round(data, 2))

        return data_dict


#  地区分种类能源结构
class ClassificationStructureSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['data']

    def get_data(self, obj):
        data_dict = {'水力发电量': {}, '太阳能发电量': {}, '风力发电量': {}}
        data_obj = EnergyReserveModel.objects.filter(province=obj.province).order_by('-year').first()
        if data_obj:
            for x in data_dict:
                data_dict[x] = {'地区开发': [], '地区消耗': []}
                city_list = random.sample(my_methods.province_dict()[obj.province], 4)
                for y in city_list:
                    data_dict[x]['地区开发'].append({'value': round(random.uniform(10.0, 25.0), 2), 'name': y})
                data_dict[x]['地区开发'].append({'value': round(random.uniform(10.0, 25.0), 2), 'name': '其他'})
                city_list = random.sample(my_methods.province_dict()[obj.province], 4)
                for y in city_list:
                    data_dict[x]['地区消耗'].append({'value': round(random.uniform(10.0, 25.0), 2), 'name': y})
                data_dict[x]['地区消耗'].append({'value': round(random.uniform(10.0, 25.0), 2), 'name': '其他'})
        return data_dict


#  地区分种类发电装机容量
class ClassificationInstallationSerializer(serializers.ModelSerializer):
    year = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['year', 'data']

    def get_year(self, obj):
        year = list(
            EnergyReserveModel.objects.filter(province=obj.province).order_by('year').values_list('year', flat=True))
        return year

    def get_data(self, obj):
        data_dict = {key: [] for key in random.sample(my_methods.province_dict()[obj.province], 4)}

        for city in data_dict:
            tt = random.randint(0, 100)
            if tt > 75:
                m = 3000
            else:
                m = 1500
            s = random.uniform(0, m)
            for year in self.get_year(obj):
                c = random.uniform(0, 100)
                data_dict[city].append(round(s + c, 2))
        return data_dict


#  地区分种类储量概况
class ClassificationReserveGeneralSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        model = EnergyReserveModel
        fields = ['data']

    def get_data(self, obj):
        data_dict = {'全省平均': [], '市内总量': [], '发展占比': None}

        data_obj = EnergyReserveModel.objects.filter(province=obj.province).order_by('-year').first()
        field_list = EnergyReserveModel._meta.get_fields()
        for field in field_list:
            if '_res' in field.name:
                data = getattr(data_obj, field.name)
                data_dict['全省平均'].append(data * Decimal(str(1.45)))
                data = getattr(data_obj, field.name)
                data_dict['市内总量'].append(round(data / Decimal(str(1.43)), 2))
        data_dict['发展占比'] = str(random.randint(60, 85)) + '%'
        return data_dict
