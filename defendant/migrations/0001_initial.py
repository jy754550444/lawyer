# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-04-04 11:31
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('civil', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agentword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='当事人姓名')),
                ('law', models.CharField(blank=True, max_length=20, null=True, verbose_name='律师事务所')),
                ('case', models.TextField(blank=True, max_length=1000, null=True, verbose_name='案由')),
                ('remarks', ckeditor.fields.RichTextField(blank=True, verbose_name='意见')),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Agentwords', to='civil.Civilbusiness', verbose_name='案件委托阶段')),
                ('civil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='civil.Civil', verbose_name='民事案件编号')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Agentword', to=settings.AUTH_USER_MODEL, verbose_name='律师')),
            ],
            options={
                'verbose_name': '代理词',
                'verbose_name_plural': '代理词',
            },
        ),
        migrations.CreateModel(
            name='Appeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='上述人姓名')),
                ('tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='上述人电话')),
                ('post', models.CharField(blank=True, max_length=20, null=True, verbose_name='上述人职务')),
                ('address', models.CharField(blank=True, max_length=20, null=True, verbose_name='上述人住址')),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='上述人性别')),
                ('nation', models.CharField(blank=True, max_length=20, null=True, verbose_name='上述人民族')),
                ('code', models.CharField(blank=True, max_length=50, null=True, verbose_name='上述人身份证号')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='上述人出生日期')),
                ('court', models.CharField(blank=True, max_length=20, null=True, verbose_name='法院')),
                ('requests', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='上述请求')),
                ('case', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='事实与理由')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Appeals', to='civil.Civilbusiness', verbose_name='案件委托阶段')),
                ('civil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='civil.Civil', verbose_name='民事案件编号')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Appeal', to=settings.AUTH_USER_MODEL, verbose_name='承办律师')),
            ],
            options={
                'verbose_name': '上述状',
                'verbose_name_plural': '上述状',
            },
        ),
        migrations.CreateModel(
            name='Appellant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='被上述人姓名')),
                ('tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='被上述人电话')),
                ('post', models.CharField(blank=True, max_length=20, null=True, verbose_name='被上述人职务')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='被上述人住址')),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='被上述人性别')),
                ('nation', models.CharField(blank=True, max_length=20, null=True, verbose_name='被上述人民族')),
                ('code', models.CharField(blank=True, max_length=50, null=True, verbose_name='被上述人身份证号')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='被上述人出生日期')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('appeal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Appellant', to='defendant.Appeal', verbose_name='上诉人')),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Appellants', to='civil.Civilbusiness', verbose_name='案件委托阶段')),
                ('civil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='civil.Civil', verbose_name='民事案件编号')),
            ],
            options={
                'verbose_name': '被上述人',
                'verbose_name_plural': '被上述人',
            },
        ),
        migrations.CreateModel(
            name='CivilAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_fee', models.CharField(max_length=50, verbose_name='代理费(元)')),
                ('agency_fees', models.CharField(blank=True, max_length=50, verbose_name='代理费(大写)')),
                ('nail_contacts', models.CharField(blank=True, max_length=50, null=True, verbose_name='指定乙方联系人')),
                ('nail_name', models.CharField(max_length=50, verbose_name='甲方名称')),
                ('nail_legal', models.CharField(blank=True, max_length=50, null=True, verbose_name='甲方法定代表人')),
                ('nail_address', models.CharField(blank=True, max_length=500, null=True, verbose_name='地址')),
                ('nail_tel', models.CharField(blank=True, max_length=50, null=True, verbose_name='电话')),
                ('law', models.CharField(blank=True, max_length=50, null=True, verbose_name='乙方')),
                ('b_legal', models.CharField(blank=True, max_length=50, null=True, verbose_name='乙方法定代表人')),
                ('b_address', models.CharField(blank=True, max_length=500, null=True, verbose_name='地址')),
                ('b_tel', models.CharField(blank=True, max_length=50, null=True, verbose_name='电话')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='对方当事人名称或者姓名')),
                ('court', models.CharField(blank=True, max_length=20, null=True, verbose_name='审理机关')),
                ('Trial_level', models.CharField(blank=True, max_length=20, null=True, verbose_name='审级')),
                ('case', models.CharField(blank=True, max_length=1000, verbose_name='案由')),
                ('remarks', models.TextField(blank=True, max_length=2000, null=True, verbose_name='备注')),
                ('civil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='civil.Civil', verbose_name='民事案件编号')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='CivilAgents', to=settings.AUTH_USER_MODEL, verbose_name='承办律师')),
            ],
            options={
                'verbose_name': '委托代理协议',
                'verbose_name_plural': '委托代理协议',
            },
        ),
        migrations.CreateModel(
            name='Court_letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enter_date', models.DateField(blank=True, null=True, verbose_name='日期')),
                ('number', models.IntegerField(blank=True, null=True, verbose_name='编号')),
                ('court', models.CharField(blank=True, max_length=20, null=True, verbose_name='支付单位')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='委托人/委托单位')),
                ('case', models.CharField(blank=True, max_length=1000, null=True, verbose_name='案由')),
                ('case_name', models.CharField(blank=True, max_length=1000, null=True, verbose_name='案由名称')),
                ('court_picture', models.FileField(blank=True, upload_to='Court_letter', verbose_name='文件/图片')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Court_letter', to='civil.Civilbusiness', verbose_name='案件委托阶段')),
                ('civil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='civil.Civil', verbose_name='民事案件编号')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Court_letters', to=settings.AUTH_USER_MODEL, verbose_name='承办律师')),
            ],
            options={
                'verbose_name': '律师事务所出庭函',
                'verbose_name_plural': '律师事务所出庭函',
            },
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='被申请人(或法定代理人)姓名')),
                ('bool', models.BooleanField(default=True, verbose_name='是否是申请人')),
                ('tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='被申请人电话')),
                ('post', models.CharField(blank=True, max_length=20, null=True, verbose_name='被申请人职务')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='被申请人住址')),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='被申请人性别')),
                ('nation', models.CharField(blank=True, max_length=20, null=True, verbose_name='被申请人民族')),
                ('code', models.CharField(blank=True, max_length=50, null=True, verbose_name='被申请人身份证号')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='被申请人出生日期')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Covers', to='civil.Civilbusiness', verbose_name='案件委托阶段')),
                ('civil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='civil.Civil', verbose_name='民事案件编号')),
            ],
            options={
                'verbose_name': '被申请人',
                'verbose_name_plural': '被申请人',
            },
        ),
        migrations.CreateModel(
            name='Defence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defence_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='答辩人姓名')),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='答辩人性别')),
                ('nation', models.CharField(blank=True, max_length=20, null=True, verbose_name='答辩人民族')),
                ('defence_birthday', models.CharField(blank=True, max_length=20, null=True, verbose_name='答辩人出生日期')),
                ('defence_tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='答辩人电话')),
                ('address', models.CharField(blank=True, max_length=20, null=True, verbose_name='答辩人住址')),
                ('the_defence', models.CharField(blank=True, max_length=20, null=True, verbose_name='被答辩人姓名')),
                ('the_defence_sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='被答辩人性别')),
                ('the_defence_nation', models.CharField(blank=True, max_length=20, null=True, verbose_name='被答辩人民族')),
                ('the_defence_birthday', models.CharField(blank=True, max_length=20, null=True, verbose_name='被答辩人出生日期')),
                ('the_defence_post', models.CharField(blank=True, max_length=20, null=True, verbose_name='被答辩人职务')),
                ('the_defence_tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='被答辩人电话')),
                ('the_defence_address', models.CharField(blank=True, max_length=20, null=True, verbose_name='被答辩人现住址')),
                ('court', models.CharField(blank=True, max_length=20, null=True, verbose_name='法院')),
                ('requests', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='诉讼请求')),
                ('case', models.CharField(blank=True, max_length=1000, null=True, verbose_name='案由')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Defences', to='civil.Civilbusiness', verbose_name='案件委托阶段')),
                ('civil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='civil.Civil', verbose_name='民事案件编号')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Defence', to=settings.AUTH_USER_MODEL, verbose_name='承办律师')),
            ],
            options={
                'verbose_name': '答辩状',
                'verbose_name_plural': '答辩状',
            },
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', ckeditor.fields.RichTextField(blank=True, verbose_name='证明内容')),
            ],
            options={
                'verbose_name': '证据目录',
                'verbose_name_plural': '证据目录',
            },
        ),
        migrations.CreateModel(
            name='Force',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='申请人姓名')),
                ('tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='申请人电话')),
                ('post', models.CharField(blank=True, max_length=20, null=True, verbose_name='申请人职务')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='申请人住址')),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='申请人性别')),
                ('nation', models.CharField(blank=True, max_length=20, null=True, verbose_name='申请人民族')),
                ('code', models.CharField(blank=True, max_length=50, null=True, verbose_name='申请人身份证号')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='申请人出生日期')),
                ('court', models.CharField(blank=True, max_length=20, null=True, verbose_name='法院')),
                ('requests', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='请求事项')),
                ('case', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='申请理由')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Forces', to='civil.Civilbusiness', verbose_name='案件委托阶段')),
                ('civil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='civil.Civil', verbose_name='民事案件编号')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Force', to=settings.AUTH_USER_MODEL, verbose_name='承办律师')),
            ],
            options={
                'verbose_name': '强制执行申请书',
                'verbose_name_plural': '强制执行申请书',
            },
        ),
        migrations.CreateModel(
            name='Indictment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plaintiff', models.CharField(blank=True, max_length=20, null=True, verbose_name='原告姓名')),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='原告性别')),
                ('nation', models.CharField(blank=True, max_length=20, null=True, verbose_name='原告民族')),
                ('posts', models.CharField(blank=True, max_length=20, null=True, verbose_name='原告职务')),
                ('code', models.CharField(blank=True, max_length=50, null=True, verbose_name='原告身份证号')),
                ('address', models.CharField(blank=True, max_length=20, null=True, verbose_name='原告住址')),
                ('agent', models.CharField(blank=True, max_length=20, null=True, verbose_name='法定代理人')),
                ('agent_sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='代理人性别')),
                ('agent_nation', models.CharField(blank=True, max_length=20, null=True, verbose_name='代理人民族')),
                ('birthday', models.CharField(blank=True, max_length=20, null=True, verbose_name='代理人出生日期')),
                ('agent_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='代理人身份证号')),
                ('agent_tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='代理人电话')),
                ('agent_address', models.CharField(blank=True, max_length=20, null=True, verbose_name='代理人现住址')),
                ('defendant', models.CharField(blank=True, max_length=20, null=True, verbose_name='被告人姓名')),
                ('defendant_sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='被告人性别')),
                ('defendant_nation', models.CharField(blank=True, max_length=20, null=True, verbose_name='被告人民族')),
                ('defendant_birthday', models.CharField(blank=True, max_length=20, null=True, verbose_name='被告人出生日期')),
                ('defendant_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='被告人身份证号')),
                ('defendant_tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='被告人电话')),
                ('defendant_address', models.CharField(blank=True, max_length=20, null=True, verbose_name='被告人现住址')),
                ('court', models.CharField(blank=True, max_length=20, null=True, verbose_name='法院')),
                ('requests', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='诉讼请求')),
                ('case', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='事实与理由')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Indictments', to='civil.Civilbusiness', verbose_name='案件委托阶段')),
                ('civil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='civil.Civil', verbose_name='民事案件编号')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Indictment', to=settings.AUTH_USER_MODEL, verbose_name='承办律师')),
            ],
            options={
                'verbose_name': '起诉状',
                'verbose_name_plural': '起诉状',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.CharField(blank=True, max_length=20, null=True, verbose_name='申请人姓名')),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='申请人性别')),
                ('nation', models.CharField(blank=True, max_length=20, null=True, verbose_name='申请人民族')),
                ('posts', models.CharField(blank=True, max_length=20, null=True, verbose_name='申请人职务')),
                ('address', models.CharField(blank=True, max_length=20, null=True, verbose_name='申请人现住址')),
                ('one_applicant', models.CharField(blank=True, max_length=20, null=True, verbose_name='第一被申请人姓名')),
                ('one_sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='第一被申请人性别')),
                ('one_nation', models.CharField(blank=True, max_length=20, null=True, verbose_name='第一被申请人民族')),
                ('one_posts', models.CharField(blank=True, max_length=20, null=True, verbose_name='第一被申请人职务')),
                ('one_address', models.CharField(blank=True, max_length=20, null=True, verbose_name='第一被申请人现住址')),
                ('two_applicant', models.CharField(blank=True, max_length=20, null=True, verbose_name='第二被申请人姓名')),
                ('two_sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='第二被申请人性别')),
                ('two_nation', models.CharField(blank=True, max_length=20, null=True, verbose_name='第二被申请人民族')),
                ('two_posts', models.CharField(blank=True, max_length=20, null=True, verbose_name='第二被申请人职务')),
                ('two_address', models.CharField(blank=True, max_length=20, null=True, verbose_name='第二被申请人现住址')),
                ('court', models.CharField(blank=True, max_length=20, null=True, verbose_name='法院')),
                ('requests', models.TextField(blank=True, max_length=10000, null=True, verbose_name='请求事项')),
                ('case', models.TextField(blank=True, max_length=10000, null=True, verbose_name='事实与理由')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Propertys', to='civil.Civilbusiness', verbose_name='案件委托阶段')),
                ('civil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='civil.Civil', verbose_name='民事案件编号')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Property', to=settings.AUTH_USER_MODEL, verbose_name='承办律师')),
            ],
            options={
                'verbose_name': '财产保全申请书',
                'verbose_name_plural': '财产保全申请书',
            },
        ),
        migrations.CreateModel(
            name='Prove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='姓名')),
                ('post', models.CharField(blank=True, max_length=20, null=True, verbose_name='职务')),
                ('tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='电话')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='住址')),
                ('enter_date', models.DateField(auto_now_add=True, verbose_name='日期')),
                ('remarks', models.TextField(blank=True, max_length=200, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '法定代表人身份证明书',
                'verbose_name_plural': '法定代表人身份证明书',
            },
        ),
        migrations.CreateModel(
            name='Revoke',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plaintiff', models.CharField(blank=True, max_length=20, null=True, verbose_name='申请人姓名')),
                ('tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='申请人电话')),
                ('address', models.CharField(blank=True, max_length=20, null=True, verbose_name='申请人住址')),
                ('agent', models.CharField(blank=True, max_length=20, null=True, verbose_name='法定代表人')),
                ('claimant', models.CharField(blank=True, max_length=20, null=True, verbose_name='被申请人姓名')),
                ('the_defence_sex', models.CharField(choices=[('1', '男'), ('2', '女')], default='1', max_length=20, verbose_name='被申请人性别')),
                ('the_defence_nation', models.CharField(blank=True, max_length=20, null=True, verbose_name='被申请人民族')),
                ('the_defence_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='被申请人身份证号')),
                ('the_defence_birthday', models.CharField(blank=True, max_length=20, null=True, verbose_name='被申请人出生日期')),
                ('the_defence_tel', models.CharField(blank=True, max_length=20, null=True, verbose_name='被申请人电话')),
                ('the_defence_address', models.CharField(blank=True, max_length=20, null=True, verbose_name='被申请人现住址')),
                ('court', models.CharField(blank=True, max_length=20, null=True, verbose_name='法院')),
                ('requests', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='申请事项')),
                ('case', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='事实与理由')),
                ('remarks', models.TextField(blank=True, verbose_name='备注')),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Revokes', to='civil.Civilbusiness', verbose_name='案件委托阶段')),
                ('civil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='civil.Civil', verbose_name='民事案件编号')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Revoke', to=settings.AUTH_USER_MODEL, verbose_name='承办律师')),
            ],
            options={
                'verbose_name': '撤诉申请',
                'verbose_name_plural': '撤诉申请',
            },
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='委托人姓名')),
                ('remarks', ckeditor.fields.RichTextField(blank=True, verbose_name='风险告知书内容')),
            ],
            options={
                'verbose_name': '风险告知书',
                'verbose_name_plural': '风险告知书',
            },
        ),
        migrations.AddField(
            model_name='cover',
            name='covers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Cover', to='defendant.Force', verbose_name='申请人'),
        ),
    ]
