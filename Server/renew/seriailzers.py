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
