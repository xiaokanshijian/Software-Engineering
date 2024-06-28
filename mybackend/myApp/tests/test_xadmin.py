from django.test import TestCase
import xadmin
from myApp.models import FisherMan, HydroData, Fish
from myApp.adminx import FisherManAdmin, HydroDataAdmin, FishAdmin

class AdminTest(TestCase):
    def setUp(self):
        # 创建测试数据
        HydroData.objects.create(date='2021-01-01', water_quality='I', temperature=20, ph=7.0, dissolved_oxygen=8.0, conductivity=300, turbidity=10, permanganate_index=5, ammonia_nitrogen=0.1, total_nitrogen=0.5, total_phosphorus=0.1, site_condition='good')
        Fish.objects.create(species='carp', weight=100, length=20, height=10, width=5)
        FisherMan.objects.create(name='张三', phone='12345678901', email='your_email@mail.com')

    def test_hydro_data_admin(self):
        model_admin = HydroDataAdmin(HydroData, xadmin.site)
        self.assertEqual(model_admin.list_display, ['id', 'date', 'water_quality', 'temperature', 'ph', 'dissolved_oxygen', 'conductivity', 'turbidity', 'permanganate_index', 'ammonia_nitrogen', 'total_nitrogen', 'total_phosphorus', 'site_condition'])
        self.assertEqual(model_admin.search_fields, ['date', 'water_quality', 'site_condition'])
        self.assertEqual(model_admin.list_filter, ['date', 'water_quality', 'site_condition'])
        self.assertEqual(model_admin.list_per_page, 10)
        self.assertEqual(model_admin.show_detail_fields, ['date'])
        self.assertEqual(model_admin.model_icon, 'fa fa-tint')

    def test_fish_admin(self):
        model_admin = FishAdmin(Fish, xadmin.site)
        self.assertEqual(model_admin.list_display, ['id', 'species', 'weight', 'length', 'height', 'width'])
        self.assertEqual(model_admin.search_fields, ['species'])
        self.assertEqual(model_admin.list_filter, ['species'])
        self.assertEqual(model_admin.list_per_page, 10)
        self.assertEqual(model_admin.show_detail_fields, ['species'])
        self.assertEqual(model_admin.model_icon, 'fa fa-fish')

    def test_fisherman_admin(self):
        model_admin = FisherManAdmin(FisherMan, xadmin.site)
        self.assertEqual(model_admin.list_display, ['id', 'user', 'name', 'phone', 'email', 'create_time'])
        self.assertEqual(model_admin.search_fields, ['name', 'phone', 'email'])
        self.assertEqual(model_admin.list_filter, ['name', 'phone', 'email'])
        self.assertEqual(model_admin.list_per_page, 10)
        self.assertEqual(model_admin.show_detail_fields, ['name'])
        self.assertEqual(model_admin.model_icon, 'fa fa-user')