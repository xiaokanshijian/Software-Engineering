from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from myApp.models import FisherMan
from myApp.serializers import FisherSerializer, UserDetailSerializer
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from .utils.getData import getHydroData, getHydroDataList, getFishData, getScore
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
import json
import paddlex as pdx
from django.core.files.storage import FileSystemStorage
import os
import cv2

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


from django.http import JsonResponse
import base64

@csrf_exempt
def AICenter(request):
    if request.method == 'POST' and request.FILES.get('image'):
        # 确保mask和draw文件夹存在
        image_dir = './tmp/images'
        mask_dir = './tmp/mask'
        draw_dir = './tmp/draw'
        os.makedirs(mask_dir, exist_ok=True)
        os.makedirs(draw_dir, exist_ok=True)
        # 保存上传的图片
        image = request.FILES['image']
        fs = FileSystemStorage(location=image_dir)
        filename = fs.save(image.name, image)
        imgName = fs.path(filename)
        print(imgName)
        
        # 图片处理逻辑
        file_name = os.path.split(imgName)[1].split('.')[0]
        model = pdx.deploy.Predictor('./inference_model_seg')
        label = model.predict(imgName)['label_map']
        label = label * 255
        mask_path = os.path.join(mask_dir, f'{file_name}_mask.png')
        cv2.imwrite(mask_path, label, (cv2.IMWRITE_PNG_COMPRESSION, 0))
        image = cv2.imread(imgName)
        mask = cv2.imread(mask_path, 0)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
        result_image_path = os.path.join(draw_dir, f'{file_name}_draw.png')
        cv2.imwrite(result_image_path, image)

        model = pdx.load_model('./inference_model')
        result = model.predict(imgName)
        result_category = result[0]["category"]
        print(result_category)
        
        # 将图像转换为Base64编码
        with open(result_image_path, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        
        # 将图像数据和result_category封装成JSON对象返回
        response_data = {
            'image_data': encoded_string,
            'result_category': result_category
        }
        return JsonResponse(response_data)
    else:
        # 如果不是POST请求或没有文件被上传，则渲染默认页面
        return render(request, 'AICenter.html')
    