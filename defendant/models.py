# coding=utf-8
__author__ = 'yy'

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from civil.models import Civil,Civilbusiness
from ckeditor.fields import RichTextField


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



# 民事案件委托代理
class CivilAgent(models.Model):
    civil = models.ForeignKey(Civil, verbose_name=u'民事案件编号', null=True, on_delete=models.CASCADE)
    agency_fee = models.CharField(verbose_name='代理费(元)', max_length=50)
    agency_fees = models.CharField(verbose_name='代理费(大写)', max_length=50,blank=True)
    nail_contacts = models.CharField(verbose_name='指定乙方联系人', max_length=50, blank=True, null=True)
    nail_name = models.CharField(verbose_name='甲方名称', max_length=50)
    nail_legal = models.CharField(verbose_name='甲方法定代表人', max_length=50, blank=True, null=True)
    nail_address = models.CharField(verbose_name='地址', max_length=500, blank=True, null=True)
    nail_tel = models.CharField(verbose_name='电话', max_length=50, blank=True, null=True)
    law = models.CharField( verbose_name=u'乙方',max_length=50, blank=True, null=True )
    b_legal = models.CharField(verbose_name='乙方法定代表人', max_length=50, blank=True, null=True)
    b_address = models.CharField(verbose_name='地址', max_length=500, blank=True, null=True)
    b_tel = models.CharField(verbose_name='电话', max_length=50, blank=True, null=True)
    # business = models.ForeignKey(Civilbusiness, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
    #                              related_name='Civilbusiness')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='CivilAgents')
    name = models.CharField(verbose_name='对方当事人名称或者姓名', max_length=50, blank=True, null=True)
    court = models.CharField(verbose_name='审理机关', max_length=20, blank=True, null=True)
    Trial_level = models.CharField(verbose_name='审级', max_length=20,blank=True, null=True)
    case = models.CharField(verbose_name='案由', max_length=1000, blank=True)
    remarks = models.TextField(verbose_name='备注', blank=True, max_length=2000, null=True)

    class Meta:
        verbose_name = '委托代理协议'
        verbose_name_plural = '委托代理协议'

    def __str__(self):
        return self.nail_name


# 律师事务所民事出庭函
class Court_letter(models.Model):
    enter_date = models.DateField(verbose_name='日期', blank=True, null=True)
    number = models.IntegerField(verbose_name='编号', blank=True, null=True)
    civil = models.ForeignKey(Civil, verbose_name=u'民事案件编号', null=True, on_delete=models.CASCADE)
    court = models.CharField(verbose_name='支付单位', max_length=20, blank=True, null=True)
    name = models.CharField(verbose_name='委托人/委托单位', max_length=50, blank=True, null=True)
    business = models.ForeignKey(Civilbusiness, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Court_letter')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Court_letters')
    case = models.CharField(verbose_name='案由', max_length=1000, blank=True, null=True)
    case_name = models.CharField(verbose_name='案由名称', max_length=1000, blank=True, null=True)
    court_picture = models.FileField(verbose_name=u'文件/图片', upload_to='Court_letter', blank=True)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '律师事务所出庭函'
        verbose_name_plural = '律师事务所出庭函'

    def __str__(self):
        return self.name


# 财产保全申请书
class Property(models.Model):
    applicant = models.CharField(verbose_name='申请人姓名', max_length=20, blank=True, null=True)
    sex = models.CharField(verbose_name='申请人性别', max_length=20, choices=SEX_CHOICES, default='1')
    nation = models.CharField(verbose_name='申请人民族', max_length=20, blank=True, null=True)
    posts = models.CharField(verbose_name='申请人职务', max_length=20, blank=True, null=True)
    address = models.CharField(verbose_name='申请人现住址', max_length=20, blank=True, null=True)
    one_applicant = models.CharField(verbose_name='第一被申请人姓名', max_length=20, blank=True, null=True)
    one_sex = models.CharField(verbose_name='第一被申请人性别', max_length=20, choices=SEX_CHOICES, default='1')
    one_nation = models.CharField(verbose_name='第一被申请人民族', max_length=20, blank=True, null=True)
    one_posts = models.CharField(verbose_name='第一被申请人职务', max_length=20, blank=True, null=True)
    one_address = models.CharField(verbose_name='第一被申请人现住址', max_length=20, blank=True, null=True)
    two_applicant = models.CharField(verbose_name='第二被申请人姓名', max_length=20, blank=True, null=True)
    two_sex = models.CharField(verbose_name='第二被申请人性别', max_length=20, choices=SEX_CHOICES, default='1')
    two_nation = models.CharField(verbose_name='第二被申请人民族', max_length=20, blank=True, null=True)
    two_posts = models.CharField(verbose_name='第二被申请人职务', max_length=20, blank=True, null=True)
    two_address = models.CharField(verbose_name='第二被申请人现住址', max_length=20, blank=True, null=True)
    court = models.CharField(verbose_name='法院', max_length=20, blank=True, null=True)
    civil = models.ForeignKey(Civil, verbose_name=u'民事案件编号', null=True, on_delete=models.CASCADE)
    business = models.ForeignKey(Civilbusiness, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Propertys')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Property')
    requests = models.TextField(verbose_name='请求事项', max_length=10000, blank=True, null=True)
    case = models.TextField(verbose_name='事实与理由', max_length=10000, blank=True, null=True)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '财产保全申请书'
        verbose_name_plural = '财产保全申请书'

    def __str__(self):
        return self.applicant


# 起诉状
class Indictment(models.Model):
    plaintiff = models.CharField(verbose_name='原告姓名', max_length=20, blank=True, null=True)
    sex = models.CharField(verbose_name='原告性别', max_length=20, choices=SEX_CHOICES, default='1')
    nation = models.CharField(verbose_name='原告民族', max_length=20, blank=True, null=True)
    posts = models.CharField(verbose_name='原告职务', max_length=20, blank=True, null=True)
    code = models.CharField(verbose_name='原告身份证号', max_length=50, blank=True, null=True)
    address = models.CharField(verbose_name='原告住址', max_length=20, blank=True, null=True)
    agent = models.CharField(verbose_name='法定代理人', max_length=20, blank=True, null=True)
    agent_sex = models.CharField(verbose_name='代理人性别', max_length=20, choices=SEX_CHOICES, default='1')
    agent_nation = models.CharField(verbose_name='代理人民族', max_length=20, blank=True, null=True)
    birthday = models.CharField(verbose_name='代理人出生日期', max_length=20, blank=True, null=True)
    agent_code = models.CharField(verbose_name='代理人身份证号', max_length=50, blank=True, null=True)
    agent_tel = models.CharField(verbose_name='代理人电话', max_length=20, blank=True, null=True)
    agent_address = models.CharField(verbose_name='代理人现住址', max_length=20, blank=True, null=True)
    defendant = models.CharField(verbose_name='被告人姓名', max_length=20, blank=True, null=True)
    defendant_sex = models.CharField(verbose_name='被告人性别', max_length=20, choices=SEX_CHOICES, default='1')
    defendant_nation = models.CharField(verbose_name='被告人民族', max_length=20, blank=True, null=True)
    defendant_birthday = models.CharField(verbose_name='被告人出生日期', max_length=20, blank=True, null=True)
    defendant_code = models.CharField(verbose_name='被告人身份证号', max_length=50, blank=True, null=True)
    defendant_tel = models.CharField(verbose_name='被告人电话', max_length=20, blank=True, null=True)
    defendant_address = models.CharField(verbose_name='被告人现住址', max_length=20, blank=True, null=True)
    court = models.CharField(verbose_name='法院', max_length=20, blank=True, null=True)
    civil = models.ForeignKey(Civil, verbose_name=u'民事案件编号', null=True, on_delete=models.CASCADE)
    business = models.ForeignKey(Civilbusiness, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Indictments')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Indictment')
    requests = RichTextField(verbose_name='诉讼请求', blank=True, null=True)
    case = RichTextField(verbose_name='事实与理由', blank=True, null=True)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '起诉状'
        verbose_name_plural = '起诉状'

    def __str__(self):
        return self.plaintiff


# 答辩状
class Defence(models.Model):
    defence_name = models.CharField(verbose_name='答辩人姓名', max_length=20, blank=True, null=True)
    sex = models.CharField(verbose_name='答辩人性别', max_length=20, choices=SEX_CHOICES, default='1')
    nation = models.CharField(verbose_name='答辩人民族', max_length=20, blank=True, null=True)
    defence_birthday = models.CharField(verbose_name='答辩人出生日期', max_length=20, blank=True, null=True)
    defence_tel = models.CharField(verbose_name='答辩人电话', max_length=20, blank=True, null=True)
    address = models.CharField(verbose_name='答辩人住址', max_length=20, blank=True, null=True)
    the_defence = models.CharField(verbose_name='被答辩人姓名', max_length=20, blank=True, null=True)
    the_defence_sex = models.CharField(verbose_name='被答辩人性别', max_length=20, choices=SEX_CHOICES, default='1')
    the_defence_nation = models.CharField(verbose_name='被答辩人民族', max_length=20, blank=True, null=True)
    the_defence_birthday = models.CharField(verbose_name='被答辩人出生日期', max_length=20, blank=True, null=True)
    the_defence_post = models.CharField(verbose_name='被答辩人职务', max_length=20, blank=True, null=True)
    the_defence_tel = models.CharField(verbose_name='被答辩人电话', max_length=20, blank=True, null=True)
    the_defence_address = models.CharField(verbose_name='被答辩人现住址', max_length=20, blank=True, null=True)
    court = models.CharField(verbose_name='法院', max_length=20, blank=True, null=True)
    civil = models.ForeignKey(Civil, verbose_name=u'民事案件编号', null=True, on_delete=models.CASCADE)
    business = models.ForeignKey(Civilbusiness, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Defences')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Defence')
    requests = RichTextField(verbose_name='诉讼请求', blank=True, null=True)
    case = models.CharField(verbose_name='案由', max_length=1000, blank=True, null=True)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '答辩状'
        verbose_name_plural = '答辩状'

    def __str__(self):
        return self.defence_name


# 撤诉申请
class Revoke(models.Model):
    plaintiff = models.CharField(verbose_name='申请人姓名', max_length=20, blank=True, null=True)
    tel = models.CharField(verbose_name='申请人电话', max_length=20, blank=True, null=True)
    address = models.CharField(verbose_name='申请人住址', max_length=20, blank=True, null=True)
    agent = models.CharField(verbose_name='法定代表人', max_length=20, blank=True, null=True)
    claimant = models.CharField(verbose_name='被申请人姓名', max_length=20, blank=True, null=True)
    the_defence_sex = models.CharField(verbose_name='被申请人性别', max_length=20, choices=SEX_CHOICES, default='1')
    the_defence_nation = models.CharField(verbose_name='被申请人民族', max_length=20, blank=True, null=True)
    the_defence_code = models.CharField(verbose_name='被申请人身份证号', max_length=50, blank=True, null=True)
    the_defence_birthday = models.CharField(verbose_name='被申请人出生日期', max_length=20, blank=True, null=True)
    the_defence_tel = models.CharField(verbose_name='被申请人电话', max_length=20, blank=True, null=True)
    the_defence_address = models.CharField(verbose_name='被申请人现住址', max_length=20, blank=True, null=True)
    court = models.CharField(verbose_name='法院', max_length=20, blank=True, null=True)
    civil = models.ForeignKey(Civil, verbose_name=u'民事案件编号', null=True, on_delete=models.CASCADE)
    business = models.ForeignKey(Civilbusiness, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Revokes')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Revoke')
    requests = RichTextField(verbose_name='申请事项', blank=True, null=True)
    case = RichTextField(verbose_name='事实与理由', blank=True, null=True)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '撤诉申请'
        verbose_name_plural = '撤诉申请'

    def __str__(self):
        return self.plaintiff


# 上述状
class Appeal(models.Model):
    name = models.CharField(verbose_name='上述人姓名', max_length=20, blank=True, null=True)
    tel = models.CharField(verbose_name='上述人电话', max_length=20, blank=True, null=True)
    post = models.CharField(verbose_name='上述人职务', max_length=20, blank=True, null=True)
    address = models.CharField(verbose_name='上述人住址', max_length=20, blank=True, null=True)
    sex = models.CharField(verbose_name='上述人性别', max_length=20, choices=SEX_CHOICES, default='1')
    nation = models.CharField(verbose_name='上述人民族', max_length=20, blank=True, null=True)
    code = models.CharField(verbose_name='上述人身份证号', max_length=50, blank=True, null=True)
    birthday = models.DateField(verbose_name='上述人出生日期', blank=True, null=True)
    court = models.CharField(verbose_name='法院', max_length=20, blank=True, null=True)
    civil = models.ForeignKey(Civil, verbose_name=u'民事案件编号', null=True, on_delete=models.CASCADE)
    business = models.ForeignKey(Civilbusiness, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Appeals')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Appeal')
    requests = RichTextField(verbose_name='上述请求', blank=True, null=True)
    case = RichTextField(verbose_name='事实与理由', blank=True, null=True)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '上述状'
        verbose_name_plural = '上述状'

    def __str__(self):
        return self.name


# 被上述人
class Appellant(models.Model):
    name = models.CharField(verbose_name='被上述人姓名', max_length=20, blank=True, null=True)
    tel = models.CharField(verbose_name='被上述人电话', max_length=20, blank=True, null=True)
    post = models.CharField(verbose_name='被上述人职务', max_length=20, blank=True, null=True)
    address = models.CharField(verbose_name='被上述人住址', max_length=50, blank=True, null=True)
    sex = models.CharField(verbose_name='被上述人性别', max_length=20, choices=SEX_CHOICES, default='1')
    nation = models.CharField(verbose_name='被上述人民族', max_length=20, blank=True, null=True)
    code = models.CharField(verbose_name='被上述人身份证号', max_length=50, blank=True, null=True)
    birthday = models.DateField(verbose_name='被上述人出生日期', blank=True, null=True)
    civil = models.ForeignKey(Civil, verbose_name=u'民事案件编号', null=True, on_delete=models.CASCADE)
    business = models.ForeignKey(Civilbusiness, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Appellants')
    appeal = models.ForeignKey(Appeal, verbose_name=u'上诉人', null=True, blank=True, on_delete=models.CASCADE,
                               related_name='Appellant')
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '被上述人'
        verbose_name_plural = '被上述人'

    def __str__(self):
        return self.name


# 证据目录
class Evidence(models.Model):
    remarks = RichTextField(verbose_name='证明内容', blank=True, )

    class Meta:
        verbose_name = '证据目录'
        verbose_name_plural = '证据目录'

    def __str__(self):
        return 'ssss'


# 强制执行申请书
class Force(models.Model):
    name = models.CharField(verbose_name='申请人姓名', max_length=20, blank=True, null=True)
    tel = models.CharField(verbose_name='申请人电话', max_length=20, blank=True, null=True)
    post = models.CharField(verbose_name='申请人职务', max_length=20, blank=True, null=True)
    address = models.CharField(verbose_name='申请人住址', max_length=50, blank=True, null=True)
    sex = models.CharField(verbose_name='申请人性别', max_length=20, choices=SEX_CHOICES, default='1')
    nation = models.CharField(verbose_name='申请人民族', max_length=20, blank=True, null=True)
    code = models.CharField(verbose_name='申请人身份证号', max_length=50, blank=True, null=True)
    birthday = models.DateField(verbose_name='申请人出生日期', blank=True, null=True)
    court = models.CharField(verbose_name='法院', max_length=20, blank=True, null=True)
    civil = models.ForeignKey(Civil, verbose_name=u'民事案件编号', null=True, on_delete=models.CASCADE)
    business = models.ForeignKey(Civilbusiness, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Forces')
    user = models.ForeignKey(User, verbose_name=u'承办律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Force')
    requests = RichTextField(verbose_name='请求事项', blank=True, null=True)
    case = RichTextField(verbose_name='申请理由', blank=True, null=True)
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '强制执行申请书'
        verbose_name_plural = '强制执行申请书'

    def __str__(self):
        return self.name


# 被申请人
class Cover(models.Model):
    name = models.CharField(verbose_name='被申请人(或法定代理人)姓名', max_length=20, blank=True, null=True)
    bool = models.BooleanField(verbose_name='是否是申请人', default=True)
    tel = models.CharField(verbose_name='被申请人电话', max_length=20, blank=True, null=True)
    post = models.CharField(verbose_name='被申请人职务', max_length=20, blank=True, null=True)
    address = models.CharField(verbose_name='被申请人住址', max_length=50, blank=True, null=True)
    sex = models.CharField(verbose_name='被申请人性别', max_length=20, choices=SEX_CHOICES, default='1')
    nation = models.CharField(verbose_name='被申请人民族', max_length=20, blank=True, null=True)
    code = models.CharField(verbose_name='被申请人身份证号', max_length=50, blank=True, null=True)
    birthday = models.DateField(verbose_name='被申请人出生日期', blank=True, null=True)
    civil = models.ForeignKey(Civil, verbose_name=u'民事案件编号', null=True, on_delete=models.CASCADE)
    business = models.ForeignKey(Civilbusiness, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Covers')
    covers = models.ForeignKey(Force, verbose_name=u'申请人', null=True, blank=True, on_delete=models.CASCADE,
                               related_name='Cover')
    remarks = models.TextField(verbose_name='备注', blank=True, )

    class Meta:
        verbose_name = '被申请人'
        verbose_name_plural = '被申请人'

    def __str__(self):
        return self.name


# 代理词
class Agentword(models.Model):
    name = models.CharField(verbose_name='当事人姓名', max_length=20, blank=True, null=True)
    law = models.CharField(verbose_name='律师事务所', max_length=20, blank=True, null=True)
    case = models.TextField(verbose_name='案由', max_length=1000, blank=True, null=True)
    civil = models.ForeignKey(Civil, verbose_name=u'民事案件编号', null=True, on_delete=models.CASCADE)
    business = models.ForeignKey(Civilbusiness, verbose_name=u'案件委托阶段', null=True, blank=True, on_delete=models.CASCADE,
                                 related_name='Agentwords')
    user = models.ForeignKey(User, verbose_name=u'律师', null=True, blank=True, on_delete=models.CASCADE,
                             related_name='Agentword')
    remarks = RichTextField(verbose_name='意见', blank=True, )

    class Meta:
        verbose_name = '代理词'
        verbose_name_plural = '代理词'

    def __str__(self):
        return self.name


# 风险告知书
class Risk(models.Model):
    name = models.CharField(verbose_name='委托人姓名', max_length=20, blank=True, null=True)
    remarks = RichTextField(verbose_name='风险告知书内容', blank=True, )

    class Meta:
        verbose_name = '风险告知书'
        verbose_name_plural = '风险告知书'

    def __str__(self):
        return self.name


# 法定代表人身份证明书
class Prove(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=20, blank=True, null=True)
    post = models.CharField(verbose_name='职务', max_length=20, blank=True, null=True)
    tel = models.CharField(verbose_name='电话', max_length=20, blank=True, null=True)
    address = models.CharField(verbose_name='住址', max_length=50, blank=True, null=True)
    enter_date = models.DateField(verbose_name='日期', auto_now_add=True, auto_now=False)
    remarks = models.TextField(verbose_name='备注', blank=True, max_length=200, null=True)

    class Meta:
        verbose_name = '法定代表人身份证明书'
        verbose_name_plural = '法定代表人身份证明书'

    def __str__(self):
        return self.name