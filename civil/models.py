# coding=utf-8
__author__ = 'yy'

from django.db import models
from ckeditor.fields import RichTextField
import datetime
from lawyer.models import Law
from django.contrib.auth.models import User

# from lawyer.models import Users

ORG_CHOICES = (
    ("1", u"一审"),
    ("2", u"二审"),
    ("4", u"再审"),
    ("3", u"一审，二审"),
    ("5", u"二审，再审"),
)

AGENT_CHOICES = (
    ("1", u"一般代理"),
    ("2", u"特别代理"),

)

Name_CHOICES = (
    ("1", u"委托人"),
    ("2", u"相对人"),
    ("3", u"当事人"),
    ("4", u"第三人"),
)

Method_CHOICES =(
    ("1", u"法人"),
    ("2", u"自然人"),
)

SEX_CHOICES = (
    ("1", u"男"),
    ("2", u"女"),
)

Proxy_CHOICES = (
    ("1", u"代为申请"),
    ("2", u"代为诉讼"),
    ("3", u"代为立案"),
    ("4", u"代为承认变更诉讼请求"),
    ("5", u"代收法律文书"),
    ("6", u"代为上诉"),
    ("7", u"代为查封保全"),
    ("8", u"代为申请再审"),
)


# import random
#
# ran = random.randint(0, 99)


# def defulfs():
#     now = datetime.datetime.now()
#     order_id ="主" now.strftime("%Y") + str(ran)
#     return order_id


# 民事业务流程
class Civilbusiness(models.Model):
    name = models.CharField(verbose_name='阶段名称', max_length=50)
    enter_date = models.DateField(verbose_name='创建时间', blank=True, null=True)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '民事业务流程'
        verbose_name_plural = '民事业务流程'

    def __str__(self):
        return self.name


# 案件信息登记表
class Civil(models.Model):
    subscribe = models.NullBooleanField(verbose_name='是否订阅', default=0)
    case_id = models.CharField(verbose_name='民事案件编号', max_length=50, blank=True, null=True)
    consultation = models.BooleanField(verbose_name='咨询', blank=True, default=False)
    openid = models.CharField(verbose_name='唯一标识', max_length=120,blank=True)
    case = models.CharField(verbose_name='案由', max_length=1000,)
    agency_fee = models.CharField(verbose_name='委托费', max_length=50,blank=True)
    case_office = models.CharField(verbose_name='审理机关', max_length=50, blank=True)
    court_picture = models.FileField(verbose_name=u'身份证复印件', upload_to='civil', blank=True)
    trial_level = models.CharField(verbose_name='审级', max_length=20, choices=ORG_CHOICES, default='1')
    agent = models.CharField(verbose_name='代理权限', max_length=20, choices=AGENT_CHOICES, default='1')
    pto = models.ImageField(verbose_name=u'二维码', upload_to='civil', blank=True)
    situation = models.TextField(verbose_name='案件基本情况', blank=True)
    remark = models.TextField(verbose_name='证据目录', blank=True)
    user = models.ForeignKey(User, verbose_name=u'承办律师', blank=True, on_delete=models.CASCADE,
                             related_name='Civils')
    # enter_date = models.DateField(verbose_name='归档时间', blank=True, null=True)

    class Meta:
        verbose_name = '案件信息登记表'
        verbose_name_plural = '案件信息登记表'

    def __str__(self):
        if self.consultation == False:
            return '3333'
        else:
            return '222'


#人员信息登记表
class Civils(models.Model):
    case_id = models.ForeignKey(Civil, verbose_name='案件信息登记表', null=True,blank=True, on_delete=models.CASCADE,
                                related_name='civils_civil')
    choice_name = models.CharField(verbose_name='人员性质', max_length=20, choices=Name_CHOICES, default='1')
    method_name = models.CharField(verbose_name='性质', max_length=20, choices=Method_CHOICES, default='2')
    name = models.CharField(verbose_name='委托人姓名', max_length=50, blank=True, )
    sex = models.CharField(verbose_name='性别', max_length=20, choices=SEX_CHOICES, default='1')
    age = models.CharField(verbose_name='年龄', max_length=10, blank=True, )
    nation = models.CharField(verbose_name='民族', max_length=10, blank=True, )
    occupation = models.CharField(verbose_name='职业', max_length=20, blank=True)
    idcard = models.CharField(verbose_name='身份证号', max_length=50, blank=True, )
    address = models.CharField(verbose_name='住址', max_length=200, blank=True, )
    tel = models.CharField(verbose_name='联系电话', max_length=50, blank=True, )
    nail_address = models.CharField(verbose_name='现住址', max_length=200, blank=True, )
    party = models.CharField(verbose_name='当事人(原告/被告)', max_length=50, blank=True)
    d_sex = models.CharField(verbose_name='当事人性别', max_length=20, choices=SEX_CHOICES, default='1')
    d_age = models.CharField(verbose_name='当事人年龄', max_length=10, blank=True, )
    d_nation = models.CharField(verbose_name='当事人民族', max_length=10, blank=True, )
    d_occupation = models.CharField(verbose_name='当事人职业', max_length=20, blank=True)
    d_code = models.CharField(verbose_name='当事人身份证号', max_length=50, blank=True)
    d_address = models.CharField(verbose_name='当事人住址', max_length=200, blank=True)
    d_tel = models.CharField(verbose_name='当事人联系电话', max_length=50, blank=True)
    d_nail_address = models.CharField(verbose_name='当事人现住址', max_length=200, blank=True)
    xd_name = models.CharField(verbose_name='相对人姓名', max_length=50,blank=True)
    xd_sex = models.CharField(verbose_name='性别', max_length=20, choices=SEX_CHOICES, default='1')
    xd_age = models.CharField(verbose_name='年龄', max_length=10, blank=True, null=True)
    xd_nation = models.CharField(verbose_name='民族', max_length=10, blank=True, null=True)
    xd_occupation = models.CharField(verbose_name='职业', max_length=20, blank=True, null=True)
    xd_idcard = models.CharField(verbose_name='身份证号', max_length=50, blank=True, null=True)
    xd_address = models.CharField(verbose_name='住址', max_length=200, blank=True, null=True)
    xd_tel = models.CharField(verbose_name='联系电话', max_length=50, blank=True, null=True)
    xd_nail_address = models.CharField(verbose_name='现住址', max_length=200, blank=True, null=True)
    company = models.CharField(verbose_name='公司名称', max_length=50, blank=True, null=True)
    code = models.CharField(verbose_name='统一社会信用代码', max_length=30, blank=True, null=True)
    legal = models.CharField(verbose_name='法定代表人', max_length=10, blank=True, null=True)
    id_card = models.CharField(verbose_name='法定代表人身份证号', max_length=10, blank=True, null=True)
    telephone = models.CharField(verbose_name='法定代表人电话', max_length=20, blank=True, null=True)
    company_tel = models.CharField(verbose_name='公司电话', max_length=20, blank=True, null=True)
    c_address = models.CharField(verbose_name='住所地', max_length=200, blank=True, null=True)
    place = models.CharField(verbose_name='注册地', max_length=100, blank=True, null=True)
    business= models.CharField(verbose_name='营业地', max_length=100, blank=True, null=True)
    tak = models.CharField(verbose_name='税号', max_length=50, blank=True, null=True)
    bank = models.CharField(verbose_name='开户行', max_length=50, blank=True, null=True)
    posts = models.CharField(verbose_name='职务', max_length=50, blank=True, null=True)
    court_picture = models.FileField(verbose_name=u'文件/图片', upload_to='civil', blank=True)
    legal_status= models.CharField(verbose_name='所处法律地位', max_length=20, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='civils_civil')
    # enter_date = models.DateField(verbose_name='归档时间', blank=True, null=True)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '人员信息登记表'
        verbose_name_plural = '人员信息登记表'

    def __str__(self):
        if self.name:
            return self.name
        elif self.party:
            return self.party
        else:
            return self.xd_name
