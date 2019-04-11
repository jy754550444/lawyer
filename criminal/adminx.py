# coding=utf-8
__author__ = 'yy'

import xadmin
from .models import *
from django.utils.safestring import mark_safe
from django.db.models import Max


# 刑事案件登记表
class CriminalAdmin(object):
    list_display = ('case_id','name','case', 'enter_date','user','Trial_level')
    exclude = ['case_id',]
    model_icon = 'fa fa-comments'

    def save_models(self):
        # def get_max_sn(self):
        yearmon = datetime.datetime.now().strftime('%Y')
        maxVal = Criminal.objects.filter().aggregate(sn_max=Max("case_id"))
        max_value = maxVal['sn_max']
        if max_value is None:
            num = '001'
            order_id ='主'+yearmon + '刑初'+num
            self.new_obj.case_id = order_id
            super().save_models()
        else:
            num = str(int(max_value[-3:]) + 1).rjust(3,'0')
            order_id ='主'+yearmon + '刑初'+num
            self.new_obj.case_id = order_id
            super().save_models()
        # return '{0}{1}'.format(yearmon, num)

xadmin.site.register(Criminal, CriminalAdmin)


# 刑事案件委托代理(一审)
class CriminalAgentAdmin(object):
    list_display = ('nail_name','nail_address','nail_code','user','ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    model_icon = 'fa fa-comments'


    def ui_operate(self, obj):
        # edit = reverse('xadmin:lawyer_civilagent_update', args=(obj.id,))
        # url_name="{}/{}/update".format( self.app_name, self.model_name)
        # v = reverse(url_name, args=(obj.pk,))
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)
    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(CriminalAgentAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(CriminalAgent, CriminalAgentAdmin)


# 刑事案件委托代理(二审)
class CriminalAgentsAdmin(object):
    list_display = ('nail_name','nail_address','nail_code','user','ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    model_icon = 'fa fa-cog fa-fw'

    def ui_operate(self, obj):
        # edit = reverse('xadmin:lawyer_civilagent_update', args=(obj.id,))
        # url_name="{}/{}/update".format( self.app_name, self.model_name)
        # v = reverse(url_name, args=(obj.pk,))
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)
    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(CriminalAgentsAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)

xadmin.site.register(CriminalAgents, CriminalAgentsAdmin)


#被告人专用介绍信
class Defendant_letterAdmin(object):
    list_display = ('name','case','number','court','user','ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    model_icon = 'fa fa-align-right'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)
    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(Defendant_letterAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)

xadmin.site.register(Defendant_letter, Defendant_letterAdmin)



#民事诉讼授权委托书(自然人用）
class ProxyAdmin(object):
    list_display = ('name','case','defendant','user','ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    model_icon = 'fa fa-align-center'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)
    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(ProxyAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)

xadmin.site.register(Proxy, ProxyAdmin)


#律师事务所出庭函
class Criminal_letterAdmin(object):
    list_display = ('name','case','court','user','ui_operate')
    # list_display_links = ('',)
    exclude = ('user','number')
    model_icon = 'fa fa-align-left'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)
    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(Criminal_letterAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)

xadmin.site.register(Criminal_letter, Criminal_letterAdmin)



#法律意见书
class ProposalAdmin(object):
    list_display = ('name','court','user','ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    model_icon = 'fa fa-align-left'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)
    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(ProposalAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)

xadmin.site.register(Proposal, ProposalAdmin)



#重新司法鉴定申请
class AppraisalAdmin(object):
    list_display = ('name','court','user','ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    model_icon = 'fa fa-align-left'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)
    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(AppraisalAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)

xadmin.site.register(Appraisal, AppraisalAdmin)



#取保候审申请书
class BailAdmin(object):
    list_display = ('name','court','address','tel','user','ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    model_icon = 'fa fa-align-left'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)
    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(BailAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)

xadmin.site.register(Bail, BailAdmin)


#辩护词
class DefensewordsAdmin(object):
    list_display = ('name','user','ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    model_icon = 'fa fa-align-left'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)
    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(DefensewordsAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)

xadmin.site.register(Defensewords, DefensewordsAdmin)



#不起诉意见书
class NonprosecutionAdmin(object):
    list_display = ('name','user','ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    # model_icon = 'fa fa-envira'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)
    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(NonprosecutionAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)

xadmin.site.register(Nonprosecution, NonprosecutionAdmin)


#刑事业务流程
class BusinessAdmin(object):
    list_display = ('name',)
    # list_display_links = ('',)
xadmin.site.register(Business, BusinessAdmin)


#风险告知书
class RisksAdmin(object):
    list_display = ('name','ui_operate')
    # list_display_links = ('',)

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)
    ui_operate.short_description = ''
xadmin.site.register(Risks, RisksAdmin)