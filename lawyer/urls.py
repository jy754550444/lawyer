# coding=utf-8
"""lawyer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
import xadmin
from civil.view import civilAgent,court_letter,property,indictment,defence,revoke,appeal,force,evidence,agentword,prove,risk,civiliagent,BathQrCodeAckView
from django.conf import settings
from django.conf.urls.static import static
from criminal.view import criminal_letter,defendant_letter,proxy,criminalagent,criminalagents,proposal,appraisal,bail,nonprosecution,defensewords,risks
from lawyer.view import list,finish,userDemo


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    #民事
    url(r'^xadmin/civil/civilagent/change/$',civilAgent),
    # url(r'^xadmin/civil/proxy_legal/change/$',proxy_legal),
    # url(r'^xadmin/civil/proxy_nature/change/$',proxy_nature),
    url(r'^xadmin/civil/court_letter/change/$',court_letter),
    url(r'^xadmin/civil/property/change/$',property),
    url(r'^xadmin/civil/indictment/change/$',indictment),
    url(r'^xadmin/civil/defence/change/$',defence),
    url(r'^xadmin/civil/revoke/change/$',revoke),
    url(r'^xadmin/civil/appeal/change/$',appeal),
    url(r'^xadmin/civil/force/change/$',force),
    url(r'^xadmin/civil/evidence/change/$',evidence),
    url(r'^xadmin/civil/agentword/change/$',agentword),
    url(r'^xadmin/civil/prove/change/$',prove),
    url(r'^xadmin/civil/risk/change/$',risk),
    #刑事
    url(r'^xadmin/criminal/criminal_letter/change/$',criminal_letter),
    url(r'^xadmin/criminal/defendant_letter/change/$',defendant_letter),
    url(r'^xadmin/criminal/proxy/change/$',proxy),
    url(r'^xadmin/criminal/criminalagent/change/$',criminalagent),
    url(r'^xadmin/criminal/criminalagents/change/$',criminalagents),
    url(r'^xadmin/criminal/proposal/change/$',proposal),
    url(r'^xadmin/criminal/appraisal/change/$',appraisal),
    url(r'^xadmin/criminal/bail/change/$',bail),
    url(r'^xadmin/criminal/nonprosecution/change/$',nonprosecution),
    url(r'^xadmin/criminal/defensewords/change/$',defensewords),
    url(r'^xadmin/criminal/risks/change/$',risks),
    #手机版列表页
    url(r'^list/$',list),
    url(r'^finish/$', finish,name='finish'),
    #律师所
    url(r'^profile/$', userDemo),
    #获取json数据
    url(r'^civiliagent/$', civiliagent),

    #自动生成二维码

    # url(r'^bath-qrcode-ack/$', civiliagent),
    url(r'^qrcodeack/$', BathQrCodeAckView.as_view(), name='bath-qrcode-ack'), # 确认二维码

    #微信公众号入口
    url(r'^wechat/', include('wxchat.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


