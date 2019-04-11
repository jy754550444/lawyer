# coding=utf-8
__author__ = 'yy'
import xadmin
from .models import *
from xadmin import views
from xadmin.plugins.actions import BaseActionView
# from mptt.admin import MPTTModelAdmin
from django.template import loader


# 基本的修改
class BaseSetting(object):
    enable_themes = True  # 打开主题功能
    use_bootswatch = True  # 可选主题




# 针对全局的
class GlobalSettings(object):
    # data_charts = {
    #      "user_count": {'title': u"律师注册数量", "x-field": "law_date", "y-field": ("law_count",), "order": ('law_date',)},
    #       "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    #  }
    site_title = "律师所后台管理系统"  # 系统名称
    site_footer = "律师后台"  # 底部版权栏
    menu_style = "accordion"  # 将菜单栏收起来

    # def block_top_toolbar(self, context, nodes):
    #     nodes.append(loader.render_to_string('xadmin/baseindex.html',))
# 注册，注意一个是BaseAdminView，一个是CommAdminView
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

from django.template import loader

from xadmin.sites import site
from xadmin.views import BaseAdminPlugin, ListAdminView

# class HelloWorldPlugin(BaseAdminPlugin):
#
#     # context 即为 TemplateContext， nodes 参数包含了其他插件的返回内容。
#     # 您可以直接返回 HTML 片段，或是将内容加入到 nodes 参数中
#     def block_results_top(self, context, nodes):
#         # return "<div class='info'>Hello %s</div>" % context['hello_target']
#         nodes.append(loader.render_to_string('xadmin/baseindex.html', ))
# site.register_plugin(HelloWorldPlugin, ListAdminView)
# class TestAdminPlugin(BaseAdminPlugin):
#
#     def get_context(self, context):
#         context['test'] = True
#         return context
#
# site.register_plugin(TestAdminPlugin, SomeAdminView)

#
#
# class MyAction(BaseActionView):
#     # 这里需要填写三个属性
#     action_name = "name"  #: 相当于这个 Action 的唯一标示, 尽量用比较针对性的名字
#     # description = _(u'Test selected %(verbose_name_plural)s') #: 描述, 出现在 Action 菜单中, 可以使用 ``%(verbose_name_plural)s`` 代替 Model 的名字.
#
#     # model_perm = 'change'    #: 该 Action 所需权限
#
#     # 而后实现 do_action 方法
#     # def do_action(self, queryset):
#     #     # queryset 是包含了已经选择的数据的 queryset
#     #     for obj in queryset:
#     #         # obj 的操作
#     #         ...
#     #     # 返回 HttpResponse
#     #     return HttpResponse(...)
#
# # class RecordAdmin(object):
#     # data_charts = {
#     #     "user_count": {'title': u"User Report", "x-field": "enter_date", "y-field": ("100", "200"), "order": ('enter_date',)},
#     #     # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
#     # }
#
# # xadmin.site.register(Lawyer, RecordAdmin)
#
# 律师事务所
class LawAdmin(object):
    list_display = ('name', 'tel', 'address', 'enter_date')
    # refresh_times = (3, 5, 10)
    # actions = ['name']
    list_filter = ('name', 'tel',)
    search_fields = ('name', 'tel',)
    show_detail_fields = ['name', 'tel', ...]
    list_per_page = 20
    list_editable = ['name', 'tel', ...]
    # list_export = ('xls', 'xml', 'json',)
    # data_charts = {
    #     "user_count": {'title': u"律师注册数量", "x-field": "law_date", "y-field": ("law_count",), "order": ('law_date',)},
    #     # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    # }


xadmin.site.register(Law, LawAdmin)

from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(object):
    list_display = ('user', 'tel', 'address',)


xadmin.site.register(UserProfile, UserProfileAdmin)
