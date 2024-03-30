from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt  # 取消 csrf 限制的装饰器
from django.utils.decorators import method_decorator
from datetime import datetime, timedelta

from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize

from django.apps import apps
from django.db.models import Count
from rest_framework.views import APIView

from .seriailzers import *
from .models import *


#  主要能源品种产量
@api_view(['GET', ])
@permission_classes(())
def get_region_energy_production(request, id=12):
    if request.method == 'GET':
        data_objects = MainEnergyProductionModel.objects.first()
        data = MainEnergyProductionSerializer(instance=data_objects, many=False)
        return Response(data=data.data, status=status.HTTP_200_OK)


#  电场故障信息
@method_decorator(csrf_exempt, name='dispatch')
@permission_classes(())
class ElectricFieldFault(APIView):

    def get(self, request):
        #  提供故障信息数据接口
        data_objects = ElectricFieldFaultModel.objects.first()

        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        #  获取用户提交的故障信息请求
        return None
