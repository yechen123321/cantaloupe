import random
from decimal import Decimal

from .models import *
from rest_framework import serializers


#  能源发展热力图
class HeatMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeatMapModel
        fields = ['name', 'value']
