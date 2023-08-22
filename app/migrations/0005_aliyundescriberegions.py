# Generated by Django 3.2.19 on 2023-08-22 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_aliyunecsassets_securitygroupids'),
    ]

    operations = [
        migrations.CreateModel(
            name='AliyunDescribeRegions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regionId', models.CharField(max_length=50, verbose_name='实例区域id')),
                ('regionEndpoint', models.CharField(max_length=50, verbose_name='实例端点')),
                ('localName', models.CharField(max_length=50, verbose_name='本地名称')),
            ],
            options={
                'db_table': 'aliyun_describe_Regions',
            },
        ),
    ]
