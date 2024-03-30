from .models import *
from rest_framework import serializers


#  电场故障信息GET
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


#  电场故障信息PUT
class ElectricFieldFaultSerializerPUT(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    reason = serializers.SerializerMethodField()

    class Meta:
        model = ElectricFieldFaultModel
        fields = ['name', 'reason']

    def get_name(self, obj):
        return obj.electric_field.station_name

    def get_reason(self, obj):
        return obj.malfunction_reason
