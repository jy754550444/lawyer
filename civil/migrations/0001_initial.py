# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-04-04 11:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Civil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribe', models.NullBooleanField(default=0, verbose_name='是否订阅')),
                ('case_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='民事案件编号')),
                ('consultation', models.BooleanField(default=False, verbose_name='咨询')),
                ('openid', models.CharField(blank=True, max_length=120, verbose_name='唯一标识')),
                ('case', models.CharField(max_length=1000, verbose_name='案由')),
                ('agency_fee', models.CharField(blank=True, max_length=50, verbose_name='委托费')),
                ('case_office', models.CharField(blank=True, max_length=50, verbose_name='审理机关')),
                ('court_picture', models.FileField(blank=True, upload_to='civil', verbose_name='身份证复印件')),
                ('trial_level', models.CharField(choices=[('1', '一审'), ('2', '二审'), ('4', '再审'), ('3', '一审，二审'), ('5', '二审，再审')], default='1', max_length=20, verbose_name='审级')),
                ('agent', models.CharField(choices=[('1', '一般代理'), ('2', '特别代理')], default='1', max_length=20, verbose_name='代理权限')),
                ('pto', models.ImageField(blank=True, upload_to='civil', verbose_name='二维码')),
                ('situation', models.TextField(blank=True, verbose_name='案件基本情况')),
                ('remark', models.TextField(blank=True, verbose_name='证据目录')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Civils', to=settings.AUTH_USER_MODEL, verbose_name='承办律师')),
            ],
            options={
                'verbose_name': '案件信息登记表',
                'verbose_name_plural': '案件信息登记表',
            },
        ),
        migrations.CreateModel(
            name='Civilbusiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='阶段名称')),
                ('enter_date', models.DateField(blank=True, null=True, verbose_name='创建时间')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '民事业务流程',
                'verbose_name_plural': '民事业务流程',
            },
        ),
        migrations.CreateModel(
            name='Civils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_name', models.CharField(choices=[('1', '委托人'), ('2', '相对人'), ('3', '当事人'), ('4', '第三人')], default='1', max_length=20, verbose_name='人员性质')),
                ('method_name', models.CharField(choices=[('1', '法人'), ('2', '自然人')], default='2', max_length=20, verbose_name='性质')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='委托人姓名')),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='性别')),
                ('age', models.CharField(blank=True, max_length=10, verbose_name='年龄')),
                ('nation', models.CharField(blank=True, max_length=10, verbose_name='民族')),
                ('occupation', models.CharField(blank=True, max_length=20, verbose_name='职业')),
                ('idcard', models.CharField(blank=True, max_length=50, verbose_name='身份证号')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='住址')),
                ('tel', models.CharField(blank=True, max_length=50, verbose_name='联系电话')),
                ('nail_address', models.CharField(blank=True, max_length=200, verbose_name='现住址')),
                ('party', models.CharField(blank=True, max_length=50, verbose_name='当事人(原告/被告)')),
                ('d_sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='当事人性别')),
                ('d_age', models.CharField(blank=True, max_length=10, verbose_name='当事人年龄')),
                ('d_nation', models.CharField(blank=True, max_length=10, verbose_name='当事人民族')),
                ('d_occupation', models.CharField(blank=True, max_length=20, verbose_name='当事人职业')),
                ('d_code', models.CharField(blank=True, max_length=50, verbose_name='当事人身份证号')),
                ('d_address', models.CharField(blank=True, max_length=200, verbose_name='当事人住址')),
                ('d_tel', models.CharField(blank=True, max_length=50, verbose_name='当事人联系电话')),
                ('d_nail_address', models.CharField(blank=True, max_length=200, verbose_name='当事人现住址')),
                ('xd_name', models.CharField(blank=True, max_length=50, verbose_name='相对人姓名')),
                ('xd_sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='性别')),
                ('xd_age', models.CharField(blank=True, max_length=10, null=True, verbose_name='年龄')),
                ('xd_nation', models.CharField(blank=True, max_length=10, null=True, verbose_name='民族')),
                ('xd_occupation', models.CharField(blank=True, max_length=20, null=True, verbose_name='职业')),
                ('xd_idcard', models.CharField(blank=True, max_length=50, null=True, verbose_name='身份证号')),
                ('xd_address', models.CharField(blank=True, max_length=200, null=True, verbose_name='住址')),
                ('xd_tel', models.CharField(blank=True, max_length=50, null=True, verbose_name='联系电话')),
                ('xd_nail_address', models.CharField(blank=True, max_length=200, null=True, verbose_name='现住址')),
                ('company', models.CharField(blank=True, max_length=50, null=True, verbose_name='公司名称')),
                ('code', models.CharField(blank=True, max_length=30, null=True, verbose_name='统一社会信用代码')),
                ('legal', models.CharField(blank=True, max_length=10, null=True, verbose_name='法定代表人')),
                ('telephone', models.CharField(blank=True, max_length=20, null=True, verbose_name='电话')),
                ('c_address', models.CharField(blank=True, max_length=200, null=True, verbose_name='住所地')),
                ('court_picture', models.FileField(blank=True, upload_to='civil', verbose_name='文件/图片')),
                ('legal_status', models.CharField(blank=True, max_length=20, null=True, verbose_name='所处法律地位')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('case_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='civils_civil', to='civil.Civil', verbose_name='案件信息登记表')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='civils_civil', to=settings.AUTH_USER_MODEL, verbose_name='承办律师')),
            ],
            options={
                'verbose_name': '人员信息登记表',
                'verbose_name_plural': '人员信息登记表',
            },
        ),
    ]