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
