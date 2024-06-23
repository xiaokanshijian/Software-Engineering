from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from myApp.models import FisherMan
from myApp.serializers import FisherSerializer, UserDetailSerializer
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseBadRequest
from .utils.getData import getHydroData, getHydroDataList, getFishData, getScore
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
import json


def jwt_response_payload_handler(token, user=None, request=None):
    """
    设置jwt登录之后返回token和user信息
    """
    fisherman = FisherMan.objects.get(user=user)
    return {
        'token': token,
        'user': UserDetailSerializer(user, context={'request': request}).data,
        'fisherman': FisherSerializer(fisherman, context={'request': request}).data
    }

# class UserApi(viewsets.ViewSet):
#     """
#     用户注册
#     """
class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    用户注册
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    # def login(self, request):
    #     user = FisherMan.objects.filter(username=request.data['username'])
    #     if user and check_password(request.data['password'], user.password):
    #         # 生成token
    #         token, created = Token.objects.get_or_create(user=user)
    #         return Response({
    #             'msg': '登录成功', 
    #             'user': FisherSerializer(user, context={'request': request}).data, 
    #             'token': token.key
    #             })

    def create(self, request, *args, **kwargs):
        user = User.objects.filter(username=request.data['username'])
        if user:
            return Response({'msg': '用户名已存在'}, status=status.HTTP_201_CREATED)
        user_detail = UserDetailSerializer(data=request.data)
        if user_detail.is_valid():
            user_detail.save()
        user = User.objects.get(username=request.data['username'])
        # 密码转成密文存储
        user.password = make_password(user.password)
        user.save()
        fisherMan = FisherMan(user=user, name=request.data['name'], phone=request.data['phone'], email=request.data['email'])
        if fisherMan:
            fisherMan.save()
            return Response({'msg': '注册成功'}, status=status.HTTP_200_OK)
        return Response(user_detail.errors)

# Create your views here.
class FiserViewSet(ModelViewSet):
    queryset = FisherMan.objects.all
    serializer_class = FisherSerializer

def data(request):
    if request.method == 'GET':
        April_data, May_data, records = getHydroData()
        return JsonResponse({
            'April': April_data,
            'May': May_data,
            'records': records
        })
    
def dataCenter(request):
    if request.method == 'GET':
        hydro_data = getHydroDataList()
        species_stats = getFishData()
        return JsonResponse({
            'hydro_data': hydro_data,
            'species_stats': species_stats
        })

def underwaterSystem(request):
    if request.method == 'GET':
        species_stats = getFishData()
        scores = getScore()
        return JsonResponse({
            'species_stats': species_stats,
            'scores': scores
        })

@require_http_methods(["PATCH"])
@csrf_exempt
def users(request):
    if request.method == 'PATCH':
        # 解析请求体中的JSON数据
        try:
            data = json.loads(request.body)
            user_id = data.get('id')
            name = data.get('name')
            phone = data.get('phone')
            email = data.get('email')
            # 假设 'user' 字段是用来更新其他用户信息的
            # user_info = data.get('user')
        except (ValueError, KeyError):
            return HttpResponseBadRequest("无效的请求数据")

        # 更新用户信息
        try:
            user = FisherMan.objects.get(id=user_id)
            if name:
                user.name = name
            if phone:
                user.phone = phone
            if email:
                user.email = email
            # 根据需要更新其他字段
            user.save()
            return JsonResponse({"message": "更新个人信息成功"}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "用户不存在"}, status=404)

    # 如果请求方法不是PATCH，返回不支持的请求方法
    return HttpResponseBadRequest("不支持的请求方法")
