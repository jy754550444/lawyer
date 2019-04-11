# coding=utf-8
__author__ = 'yy'

from django.db import models
from ckeditor.fields import RichTextField
import datetime
from django.contrib.auth.models import User
from lawyer.models import Law
# from lawyer.models import Users

ORG_CHOICES = (
    ("1", u"一审"),
    ("2", u"二审"),
    ("4", u"再审"),
    ("3", u"一审，二审"),
    ("5", u"二审，再审"),
)

SEX_CHOICES = (
    ("1", u"男"),
    ("2", u"女"),
)

PAY_CHOICES = (
    ("1", u"微信"),
    ("2", u"支付宝"),
    ("3", u"现金"),
    ("4", u"银行卡转账"),
    ("5", u"其它"),
)


STAGE_CHOICES = (
    ("1", u"咨询阶段"),
    ("2", u"侦查阶段"),
    ("3", u"审查起诉"),
    ("4", u"一审审判阶段"),
    ("5", u"二审审判阶段"),
    ("6", u"再审阶段"),
)



# import random
#
# ran = random.randint(0, 99)


# def defulfs():
#     now = datetime.datetime.now()
#     order_id ='主'now.strftime("%Y") + '刑初'
#     return order_id


# 刑事业务流程
class Business(models.Model):
    name = models.CharField(verbose_name='案件委托阶段', max_length=50)
    enter_date = models.DateField(verbose_name='创建时间', blank=True, null=True)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '刑事业务流程'
        verbose_name_plural = '刑事业务流程'

    def __str__(self):
        return self.name


# 刑事案件登记表
class Criminal(models.Model):
    subscribe = models.NullBooleanField(verbose_name='是否订阅', default=0)
    case_id = models.CharField(verbose_name='刑事案件编号', max_length=50, blank=True, null=True,)
    openid = models.CharField(verbose_name='唯一标识', max_length=120,blank=True)
    name = models.CharField(verbose_name='委托人', max_length=50,blank=True, null=True,)
    sex = models.CharField(verbose_name='性别', max_length=20, choices=SEX_CHOICES, default='1')
    age = models.CharField(verbose_name='年龄', max_length=10, blank=True, )
    nation = models.CharField(verbose_name='民族', max_length=10, blank=True, )
    occupation = models.CharField(verbose_name='职业', max_length=20, blank=True)
    idcard = models.CharField(verbose_name='身份证号', max_length=50, blank=True, )
    address = models.CharField(verbose_name='住址', max_length=200, blank=True, )
    tel = models.CharField(verbose_name='联系电话', max_length=50, blank=True, )
    nail_address = models.CharField(verbose_name='现住址', max_length=200, blank=True, )
    case = models.CharField(verbose_name='涉嫌罪名', max_length=1000, blank=True)
    defendant = models.CharField(verbose_name='犯罪嫌疑人或被告人', max_length=50, blank=True)
    defendants = models.CharField(verbose_name='共同犯罪嫌疑人或被告人', max_length=50, blank=True)
    stage = models.CharField(verbose_name='案件所处阶段', max_length=50, choices=STAGE_CHOICES, blank=True,default='1')
    case_office = models.CharField(verbose_name='办案机关', max_length=50, blank=True)
    Trial_level = models.CharField(verbose_name='审级', max_length=20, choices=ORG_CHOICES, default='1')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Criminals')
    enter_date = models.DateField(verbose_name='归档时间', blank=True, null=True)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '登记表'
        verbose_name_plural = '登记表'

    def __str__(self):
        return self.case


# 刑事案件辩护委托合同（一审阶段）
class CriminalAgent(models.Model):
    nail_name = models.CharField(verbose_name='甲方名称', max_length=50)
    civil = models.ForeignKey(Criminal, verbose_name=u'刑事案件编号', null=True, on_delete=models.CASCADE)
    nail_address = models.CharField(verbose_name='地址', max_length=500, blank=True, null=True)
    nail_tel = models.CharField(verbose_name='电话', max_length=50, blank=True, null=True)
    nail_code = models.CharField(verbose_name='身份证号', max_length=50, blank=True, null=True)
    law = models.ForeignKey(Law, verbose_name=u'乙方律师事务所', on_delete=models.CASCADE, blank=True, null=True,
                            related_name='agent')
    b_address = models.CharField(verbose_name='住址', max_length=500, blank=True, null=True)
    b_tel = models.CharField(verbose_name='电话', max_length=50, blank=True, null=True)
    case = models.CharField(verbose_name='涉嫌罪名', max_length=1000, blank=True)
    business = models.ForeignKey(Business, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='CriminalAgent')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='CriminalAgents')
    defence_fee = models.CharField(verbose_name='律师费(元)', max_length=50, blank=True, null=True)
    agency_fee = models.CharField(verbose_name='律师费(大写元)', max_length=50)
    total = models.CharField(verbose_name='共计(元)', max_length=50, blank=True, null=True)
    enter_date = models.DateField(verbose_name='签订日期',blank=True, null=True)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '委托代理协议'
        verbose_name_plural = '委托代理协议'

    def __str__(self):
        return self.nail_name


# 刑事案件辩护委托合同（二审阶段）
class CriminalAgents(models.Model):
    nail_name = models.CharField(verbose_name='甲方名称', max_length=50)
    civil = models.ForeignKey(Criminal, verbose_name=u'刑事案件编号', null=True, on_delete=models.CASCADE)
    nail_address = models.CharField(verbose_name='地址', max_length=500, blank=True, null=True)
    nail_tel = models.CharField(verbose_name='电话', max_length=50, blank=True, null=True)
    nail_code = models.CharField(verbose_name='身份证号', max_length=50, blank=True, null=True)
    law = models.ForeignKey(Law, verbose_name=u'乙方律师事务所', on_delete=models.CASCADE, blank=True, null=True,
                            related_name='agents')
    b_address = models.CharField(verbose_name='住址', max_length=500, blank=True, null=True)
    b_tel = models.CharField(verbose_name='电话', max_length=50, blank=True, null=True)
    case = models.CharField(verbose_name='涉嫌罪名', max_length=1000, blank=True)
    business = models.ForeignKey(Business, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='CriminalAgents')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='CriminalAgentss')
    defence_fee = models.CharField(verbose_name='律师费(元)', max_length=50, blank=True, null=True)
    agency_fee = models.CharField(verbose_name='律师费(大写元)', max_length=50)
    total = models.CharField(verbose_name='共计(元)', max_length=50, blank=True, null=True)
    enter_date = models.DateField(verbose_name='签订日期',blank=True, null=True)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '委托代理协议(二审)'
        verbose_name_plural = '委托代理协议(二审)'

    def __str__(self):
        return self.nail_name


# 刑事案件授权委托书
class Proxy(models.Model):
    case = models.CharField(verbose_name='案由', max_length=1000, blank=True, null=True)
    civil = models.ForeignKey(Criminal, verbose_name=u'刑事案件编号', null=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='委托人/委托单位', max_length=50, blank=True, null=True)
    defendant = models.CharField(verbose_name='犯罪嫌疑人或被告人', max_length=50, blank=True, null=True)
    business = models.ForeignKey(Business, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Proxy')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Proxys')
    tel = models.CharField(verbose_name='律师电话', max_length=50, blank=True, null=True)
    Trial_level = models.CharField(verbose_name='审级', max_length=20, choices=ORG_CHOICES, default='1')
    enter_date = models.DateField(verbose_name='合同有效期', )
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '授权委托书'
        verbose_name_plural = '授权委托书'

    def __str__(self):
        return self.name


# 被告人专用介绍信
class Defendant_letter(models.Model):
    # enter_date = models.DateField(verbose_name='日期', blank=True, null=True)
    number = models.IntegerField(verbose_name='编号', blank=True, null=True)
    civil = models.ForeignKey(Criminal, verbose_name=u'刑事案件编号', null=True, on_delete=models.CASCADE)
    court = models.CharField(verbose_name='交付单位', max_length=20, blank=True, null=True)
    name = models.CharField(verbose_name='犯罪嫌疑人或被告人', max_length=50, blank=True, null=True)
    business = models.ForeignKey(Business, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Defendant_letter')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Defendant_letters')
    case = models.CharField(verbose_name='案由', max_length=1000, blank=True, null=True)
    court_picture = models.FileField(verbose_name=u'文件/图片', upload_to='Court_letter', blank=True)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '被告人专用介绍信'
        verbose_name_plural = '被告人专用介绍信'

    def __str__(self):
        return self.name


# 刑事律师事务所出庭函
class Criminal_letter(models.Model):
    enter_date = models.DateField(verbose_name='日期', blank=True, null=True)
    number = models.IntegerField(verbose_name='编号', blank=True, null=True)
    civil = models.ForeignKey(Criminal, verbose_name=u'刑事案件编号', null=True, on_delete=models.CASCADE)
    court = models.CharField(verbose_name='交付单位', max_length=20, blank=True, null=True)
    name = models.CharField(verbose_name='犯罪嫌疑人或被告人', max_length=50, blank=True, null=True)
    business = models.ForeignKey(Business, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Criminal_letter')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Criminal_letters')
    case = models.CharField(verbose_name='案由', max_length=1000, blank=True, null=True)
    court_picture = models.FileField(verbose_name=u'文件/图片', upload_to='Court_letter', blank=True)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '律师事务所出庭函'
        verbose_name_plural = '律师事务所出庭函'

    def __str__(self):
        return self.name


# 法律意见书
class Proposal(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=50, blank=True, null=True)
    court = models.CharField(verbose_name='办案机关', max_length=20, blank=True, null=True)
    law = models.CharField(verbose_name='律师事务所', max_length=20, blank=True, null=True)
    civil = models.ForeignKey(Criminal, verbose_name=u'刑事案件编号', null=True, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Proposals')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Proposal')
    remarks = RichTextField(verbose_name='意见', blank=True, )

    class Meta:
        verbose_name = '法律意见书'
        verbose_name_plural = '法律意见书'

    def __str__(self):
        return self.name


# 重新司法鉴定申请
class Appraisal(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=50, blank=True, null=True)
    court = models.CharField(verbose_name='交付单位', max_length=20, blank=True, null=True)
    civil = models.ForeignKey(Criminal, verbose_name=u'刑事案件编号', null=True, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Appraisals')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Appraisal')
    remarks = RichTextField(verbose_name='理由', blank=True, )

    class Meta:
        verbose_name = '重新司法鉴定申请'
        verbose_name_plural = '重新司法鉴定申请'

    def __str__(self):
        return self.name


# 取保候审申请书
class Bail(models.Model):
    name = models.CharField(verbose_name='申请人姓名', max_length=50, blank=True, null=True)
    address = models.CharField(verbose_name='地址', max_length=50, blank=True, null=True)
    tel = models.CharField(verbose_name='电话', max_length=50, blank=True, null=True)
    requests = RichTextField(verbose_name='申请事项', blank=True, null=True)
    case = RichTextField(verbose_name='事实与理由', blank=True, null=True)
    court = models.CharField(verbose_name='交付单位', max_length=20, blank=True, null=True)
    civil = models.ForeignKey(Criminal, verbose_name=u'刑事案件编号', null=True, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Bails')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Bail')
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '取保候审申请书'
        verbose_name_plural = '取保候审申请书'

    def __str__(self):
        return self.name


# 不起诉意见书
class Nonprosecution(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=50, blank=True, null=True)
    law = models.CharField(verbose_name='律师事务所', max_length=50, blank=True, null=True)
    court = models.CharField(verbose_name='办案机关', max_length=20, blank=True, null=True)
    civil = models.ForeignKey(Criminal, verbose_name=u'刑事案件编号', null=True, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Nonprosecutions')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Nonprosecution')
    remarks = RichTextField(verbose_name='意见', blank=True, )

    class Meta:
        verbose_name = '不起诉意见书'
        verbose_name_plural = '不起诉意见书'

    def __str__(self):
        return self.name


# 辩护词
class Defensewords(models.Model):
    name = models.CharField(verbose_name=u'姓名', max_length=50, blank=True, null=True)
    law = models.CharField(verbose_name=u'律师事务所', max_length=50, blank=True, null=True)
    civil = models.ForeignKey(Criminal, verbose_name=u'刑事案件编号', null=True, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Defenseword')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Defensewords')
    remarks = RichTextField(verbose_name='意见', blank=True, )

    class Meta:
        verbose_name = '辩护词'
        verbose_name_plural = '辩护词'

    def __str__(self):
        return self.name


# 风险告知书
class Risks(models.Model):
    name = models.CharField(verbose_name='委托人姓名', max_length=20, blank=True, null=True)
    remarks = RichTextField(verbose_name='风险告知书内容', blank=True, )

    class Meta:
        verbose_name = '风险告知书'
        verbose_name_plural = '风险告知书'

    def __str__(self):
        return self.name
