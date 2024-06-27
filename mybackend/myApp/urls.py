from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from myApp.views import RegisterViewSet, FiserViewSet
from rest_framework_jwt.views import obtain_jwt_token
from myApp import views

router = DefaultRouter()    
router.register(r'register', RegisterViewSet)

urlpatterns = [
    # path('login/', UserApi.as_view({'post': 'login'})),
    path('login/', obtain_jwt_token),
    re_path('^', include(router.urls)),
    path('main/', views.data, name='main'),
    path('dataCenter/', views.dataCenter, name='dataCenter'),
    path('underwaterSystem/', views.underwaterSystem, name='underwaterSystem'),
    path('users/', views.users, name='users'),
    path('AICenter/', views.AICenter, name='AICenter'),
]
