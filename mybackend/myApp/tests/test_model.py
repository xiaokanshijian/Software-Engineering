from django.test import TestCase
from myApp.models import FisherMan
from django.contrib.auth.models import User

class FisherManModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 创建一个用户和FisherMan实例用于测试
        test_user = User.objects.create_user(username='testuser', password='12345')
        FisherMan.objects.create(user=test_user, name='张三', phone='12345678901', email='zhangsan@example.com')

    def test_field_labels(self):
        fisherman = FisherMan.objects.get(id=1)
        field_label_name = fisherman._meta.get_field('name').verbose_name
        field_label_phone = fisherman._meta.get_field('phone').verbose_name
        self.assertEquals(field_label_name, '姓名')
        self.assertEquals(field_label_phone, '电话')

    def test_field_max_length(self):
        fisherman = FisherMan.objects.get(id=1)
        max_length_name = fisherman._meta.get_field('name').max_length
        max_length_phone = fisherman._meta.get_field('phone').max_length
        self.assertEquals(max_length_name, 20)
        self.assertEquals(max_length_phone, 11)

    def test_object_name_is_name(self):
        fisherman = FisherMan.objects.get(id=1)
        expected_object_name = fisherman.name
        self.assertEquals(expected_object_name, str(fisherman))

    def test_ordering(self):
        first_fisherman = FisherMan.objects.all()[0]
        self.assertEquals(first_fisherman.name, '张三')

    def test_db_table_name(self):
        self.assertEquals(FisherMan._meta.db_table, 'fisherman')