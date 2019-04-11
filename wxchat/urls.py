# coding=utf-8
__author__ = 'yy'

from django.conf.urls import url
from wxchat.views import wechat,createMenu,getMenu,deleteMenu,redirectUrl

urlpatterns = [

    url(r'^$', wechat),  # 微信入口
    url(r'^createmenu/$', createMenu),
    url(r'^getmenu/$', getMenu),
    url(r'^delmenu/$', deleteMenu),

    url(r'^redirect/(?P<item>[\w-]+)$', redirectUrl),
]