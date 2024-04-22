import random

from .models import *
from rest_framework import serializers


class my_methods:
    @staticmethod
    def province_dict():
        s = {
            '北京': [
                '石景山', '房山', '通州', '顺义', '昌平', '大兴', '怀柔', '平谷', '延庆', '密云', '西城', '海淀',
                '朝阳', '丰台', '门头沟'
            ],
            '浙江': [
                '杭州', '宁波', '温州', '绍兴', '湖州', '嘉兴', '金华', '衢州', '台州', '丽水', '舟山'
            ],
            '重庆': [
                '渝中', '大渡口', '江北', '南岸', '北碚', '巴南', '九龙坡', '南川', '江津', '永川', '合川', '綦江',
                '潼南', '铜梁', '万盛'
            ],
            '西藏': [
                '拉萨', '昌都', '日喀则'],
            '四川': [
                '成都', '绵阳', '自贡', '攀枝花', '泸州', '德阳', '广元', '遂宁', '内江', '乐山', '资阳', '宜宾',
                '南充', '达州', '雅安', '广安', '巴中', '眉山'
            ],
            '山东': [
                '济南', '青岛', '淄博', '枣庄', '东营', '烟台', '潍坊', '济宁', '泰安', '威海', '日照', '滨州', '德州',
                '聊城', '临沂', '菏泽'
            ],
            '上海': [
                '黄浦', '徐汇', '长宁', '静安', '普陀', '虹口', '杨浦', '闵行', '宝山', '嘉定', '浦东新区', '金山',
                '松江', '青浦', '奉贤', '崇明'
            ],
            '广东': [
                '深圳', '广州', '珠海', '东莞', '佛山', '中山', '惠州', '汕头', '江门', '湛江', '肇庆', '梅州', '茂名',
                '阳江', '清远', '韶关', '揭阳', '汕尾', '潮州', '河源', '云浮'
            ],
            '广西': [
                '南宁', '柳州', '桂林', '梧州', '北海', '崇左', '来宾', '贺州', '玉林', '百色', '河池', '钦州',
                '防城港', '贵港'
            ],
            '安徽': [
                '合肥', '芜湖', '蚌埠', '淮北', '亳州', '宿州', '阜阳', '淮南', '滁州', '六安', '马鞍山', '宣城',
                '铜陵', '池州', '安庆', '黄山'
            ]
        }
        return s


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


#  地区基地分布
class BaseDistributionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = BaseDistributionModel
        fields = ['name', 'value', 'thing']

    def get_name(self, obj):
        return obj.electric_field.city


#  地区电场运行状况
class OperationStatusSerializer(serializers.ModelSerializer):
    data = serializers.SerializerMethodField()

    class Meta:
        fields = ['data']
        model = BaseDistributionModel

    def get_data(self, obj):
        province = obj.electric_field.province
        name_list = list(
            BaseDistributionModel.objects.filter(electric_field__city__in=my_methods.province_dict()[province]).values_list('electric_field__station_name', flat=True))
        data_dict = {'name': random.sample(name_list, min(4, len(name_list))), 'thing': []}
        for i in range(len(data_dict['name'])):
            data = BaseDistributionModel.objects.filter(electric_field__station_name=data_dict['name'][i]).values_list('electric_field__state').first()
            if data[0]:
                data_dict['thing'].append('正常运行')
            else:
                data_dict['thing'].append('运行异常')
        return data_dict


#  地区基地设备运行相关信息
class BaseEquipmentWorkingInformationSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    manage = serializers.SerializerMethodField()

    class Meta:
        model = BaseEquipmentWorkingInformationModel
        fields = ['name', 'type', 'state', 'manage', 'when']

    def get_name(self, obj):
        return obj.device_name

    def get_type(self, obj):
        return obj.device_type

    def get_state(self, obj):
        return obj.device_state

    def get_manage(self, obj):
        return obj.device_information
