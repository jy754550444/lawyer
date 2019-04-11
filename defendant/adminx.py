# coding=utf-8
__author__ = 'yy'
import xadmin
from .models import *
from xadmin import views
from xadmin.plugins.actions import BaseActionView
# from mptt.admin import MPTTModelAdmin
from django.utils.safestring import mark_safe


# 民事案件委托代理
class CivilAgentAdmin(object):
    # 除了空的
    def formfield_for_dbfield(self, db_field, **kwargs):
        # if not self.request.user.is_superuser:
        if db_field.name == "civil":
            kwargs["queryset"] = Civil.objects.exclude(case_id=None)
        return super(CivilAgentAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    def save_models(self):
        obj = self.new_obj
        request = self.request
        obj.user_id = str(request.user.id)
        obj.save()




    list_display = ('nail_name', 'agency_fees', 'nail_legal', 'nail_address', 'user', 'ui_operate')
    # fields = ('civil', 'agency_fee', )
    # list_display_links = ('',)
    exclude = ('user', 'agency_fees',)
    model_icon = 'fa fa-shield fa-flip-vertical'

    # 加载js文件
    def get_media(self):
        media = super(CivilAgentAdmin, self).get_media()
        path = self.request.get_full_path()
        if "add" in path or 'update' in path:
            media.add_js([self.static('js/civil.js')])
        return media

    def queryset(self):
        qs = super(CivilAgentAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)

    def ui_operate(self, obj):
        # edit = reverse('xadmin:lawyer_civilagent_update', args=(obj.id,))
        # url_name="{}/{}/update".format( self.app_name, self.model_name)
        # v = reverse(url_name, args=(obj.pk,))
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)

    ui_operate.short_description = ''


xadmin.site.register(CivilAgent, CivilAgentAdmin)

# 律师事务所民事出庭函
class Court_letterAdmin(object):
    list_display = ('name', 'case', 'court', 'case_name', 'user', 'ui_operate')
    # list_display_links = ('',)
    exclude = ('user', 'number')
    model_icon = 'fa fa-shield fa-rotate-270'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)

    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(Court_letterAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(Court_letter, Court_letterAdmin)


# 财产保全申请书
class PropertyAdmin(object):
    list_display = ('applicant', 'nation', 'address', 'posts', 'case', 'user', 'ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    # model_icon = 'fa fa-square-o fa-stack-2x'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)

    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(PropertyAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(Property, PropertyAdmin)


# 起诉状
class IndictmentAdmin(object):
    list_display = ('plaintiff', 'case', 'nation', 'court', 'code', 'user', 'ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    model_icon = 'fa fa-shield fa-rotate-90'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)

    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(IndictmentAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(Indictment, IndictmentAdmin)


# 答辩状
class DefenceAdmin(object):
    list_display = ('defence_name', 'case', 'nation', 'court', 'defence_tel', 'user', 'ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    model_icon = 'fa fa-shield fa-rotate-90'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)

    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(DefenceAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(Defence, DefenceAdmin)


# 撤诉申请
class RevokeAdmin(object):
    list_display = ('plaintiff', 'tel', 'address', 'agent', 'claimant', 'user', 'ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    model_icon = 'fa fa-shield fa-rotate-90'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)

    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(RevokeAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(Revoke, RevokeAdmin)


# 上述状
class AppealAdmin(object):
    list_display = ('name', 'tel', 'address', 'nation', 'post', 'user', 'ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    model_icon = 'fa fa-shield fa-rotate-90'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)

    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(AppealAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(Appeal, AppealAdmin)


# 被上述人
class AppellantAdmin(object):
    list_display = ('name', 'tel', 'address', 'nation', 'post',)


xadmin.site.register(Appellant, AppellantAdmin)


# 证据目录
class EvidenceAdmin(object):
    list_display = ('remarks', 'ui_operate')
    # list_display_links = ('',)
    model_icon = 'fa fa-shield fa-rotate-90'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)

    ui_operate.short_description = ''


xadmin.site.register(Evidence, EvidenceAdmin)


# 强制执行申请书
class ForceAdmin(object):
    list_display = ('name', 'tel', 'address', 'nation', 'post', 'user', 'ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    model_icon = 'fa fa-shield fa-rotate-90'

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)

    ui_operate.short_description = ''

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(ForceAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)


xadmin.site.register(Force, ForceAdmin)


# 被申请人
class CoverAdmin(object):
    list_display = ('name', 'tel', 'address', 'nation', 'post',)


xadmin.site.register(Cover, CoverAdmin)


# 代理词
class AgentwordAdmin(object):
    list_display = ('name', 'law', 'user', 'ui_operate')
    # list_display_links = ('',)
    exclude = ('user',)
    model_icon = 'fa fa-shield fa-rotate-90'

    def save_models(self):
        self.new_obj.user = self.request.user
        super().save_models()

    def queryset(self):
        qs = super(AgentwordAdmin, self).queryset()
        if self.request.user.is_superuser:
            return qs
        else:
            return qs.filter(user=self.request.user)

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)

    ui_operate.short_description = ''


xadmin.site.register(Agentword, AgentwordAdmin)


# 民事业务流程
class CivilbusinessAdmin(object):
    list_display = ('name',)
    # list_display_links = ('',)


xadmin.site.register(Civilbusiness, CivilbusinessAdmin)


# 法定代表人身份证明书
class ProveAdmin(object):
    list_display = ('name', 'post', 'ui_operate')
    # list_display_links = ('',)

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)

    ui_operate.short_description = ''


xadmin.site.register(Prove, ProveAdmin)


# 风险告知书
class RiskAdmin(object):
    list_display = ('name', 'ui_operate')
    # list_display_links = ('',)

    def ui_operate(self, obj):
        return mark_safe("<a href=change?req_id=%s target=_blank>打印</a>" % obj.pk)

    ui_operate.short_description = ''


xadmin.site.register(Risk, RiskAdmin)


