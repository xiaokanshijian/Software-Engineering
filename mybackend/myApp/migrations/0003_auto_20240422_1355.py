# Generated by Django 3.0.3 on 2024-04-22 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0002_auto_20240422_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='FisherMan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '养殖户',
                'verbose_name_plural': '养殖户',
                'db_table': 'fisherman',
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
