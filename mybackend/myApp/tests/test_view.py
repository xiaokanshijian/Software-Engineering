from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client

class AICenterViewTest(TestCase):
    def test_aicenter_view_with_image(self):
        # 创建一个模拟的图像文件
        image = SimpleUploadedFile(name='test_image.jpg', content=open('"E:\Grade3\fish_recognition2\tmp\image\fish_000021830001_01842.png"', 'rb').read(), content_type='image/png')
        
        # 构造POST请求
        client = Client()
        response = client.post(reverse('aicenter'), {'image': image})
        
        # 检查响应状态码
        self.assertEqual(response.status_code, 200)
        
        # 进一步的响应内容检查可以根据实际情况添加
        # 例如，检查返回的JSON中是否包含特定的键
        # self.assertIn('result_category', response.json())

from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.hashers import make_password

class UserRegistrationAndLoginTest(APITestCase):
    def setUp(self):
        # 创建一个用户用于登录测试
        self.test_user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        self.test_user.password = make_password('testpassword')
        self.test_user.save()

    def test_registration(self):
        """
        测试用户注册
        """
        url = reverse('register')  # 确保你的URL名称是'register'
        data = {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'newpassword'}
        response = self.client.post(url, data, format='json')
        # 检查是否成功创建用户
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # 检查返回的数据中是否有用户信息
        self.assertTrue('user' in response.data)

    def test_login(self):
        """
        测试用户登录
        """
        url = reverse('login')  # 确保你的URL名称是'login'
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(url, data, format='json')
        # 检查是否成功返回token
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # 检查返回的数据中是否有token
        self.assertTrue('token' in response.data)