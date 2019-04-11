# coding=utf-8
__author__ = 'yy'

import random, string, time, os,datetime,json,requests

from lawyer import settings
from wechatpy.oauth import WeChatOAuth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from wechatpy.replies import TextReply, ImageReply, VoiceReply, ArticlesReply, TransferCustomerServiceReply
from wechatpy import parse_message, create_reply, WeChatClient
from wechatpy.utils import check_signature, ObjectDict
from wxchat.models import WxLaw
from civil.models import Civil

from wechatpy.exceptions import InvalidSignatureException

WECHAT_TOKEN = settings.WECHAT_TOKEN
APP_URL = settings.APP_URL
APPID = settings.WECHAT_APPID
APPSECRET = settings.WECHAT_SECRET

client = WeChatClient(settings.WECHAT_APPID, settings.WECHAT_SECRET)
# wxPay = WeChatPay(appid=settings.WECHAT_APPID, api_key=settings.MCH_KEY, mch_id=settings.MCH_ID)


@csrf_exempt
def wechat(request):
    if request.method == 'GET':
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)


        try:
            check_signature(WECHAT_TOKEN, signature, timestamp, nonce)
        except InvalidSignatureException:
            echostr = 'error'

        return HttpResponse(echostr)

    elif request.method == 'POST':
        msg = parse_message(request.body)
        print(msg)
        # if msg.type == 'text':
        #     if msg.content == '民事案件':
        #         reply = getDogLossList(request, msg)
        #     elif msg.content == '刑事案件':
        #         reply = getDogOwnerList(request, msg)
        #     else:
        #         reply = TransferCustomerServiceReply(message=msg)
        # code = request.POST.get('code',None)
        # print(code,1111111111)
        if msg.type == 'image':
            reply = ImageReply(message=msg)
            reply.media_id = msg.media_id
        elif msg.type == 'voice':
            reply = VoiceReply(message=msg)
            reply.media_id = msg.media_id
            reply.content = '语音信息'
        elif msg.type == 'event':
            print('eventkey=', msg.event)
            if msg.event == 'subscribe':
                print(333333333333)
                saveWxLaw(msg.source)
                reply = create_reply('感谢您关注【辽宁大潮律师事务所】', msg)
            elif msg.event == 'unsubscribe':
                reply = create_reply('取消关注公众号', msg)
                unSubUserinfo(msg.source)
            elif msg.event == 'subscribe_scan':
                reply = create_reply('感谢您关注【辽宁大潮律师事务所】', msg)
                saveWxLaw(msg.source, msg.scene_id)
                print('scene_id=', msg.scene_id)
            elif msg.event == 'scan':
                print('scan====', msg.scene_id)
                # setUserToMember(msg.source, msg.scene_id)
                reply = create_reply('', msg)
            else:
                reply = create_reply('view', msg)

        response = HttpResponse(reply.render(), content_type="application/xml")
        return response

def unSubUserinfo(openid):
    try:
        user = WxLaw.objects.get(openid=openid)
        if user:
            user.delete()
        #     WxIntroduce.objects.filter(Q(openid=openid) | Q(introduce_id=openid)).delete()
    except WxLaw.DoesNotExist:
        pass


def saveWxLaw(openid, scene_id=None):
    user = client.user.get(openid)
    print(user,openid,222333333)
    if 'errcode' not in user:
        sub_time = user.pop('subscribe_time')
        sub_time = datetime.datetime.fromtimestamp(sub_time)
        user['subscribe_time'] = sub_time

        obj, created = WxLaw.objects.update_or_create(defaults=user, openid=openid)
        obj.save()
    else:
        print(user)

def createMenu(request):
    print('createMenu', client.access_token)
    resp = client.menu.create({
        "button": [
            {
                "type": "view",
                "name": "民事案件",
                "url": APP_URL + "/civil/index"
            },
            {
                "type": "view",
                "name": "刑事案件",
                "url": APP_URL + "/criminal/index",
                # "sub_button": [
                #     {
                #         "type": "view",
                #         "name": "我的推广码",
                #         "url": APP_URL + "/redirect/myqrcode"
                #     },
                #     {
                #         "type": "view",
                #         "name": "我的积分",
                #         "url": APP_URL + "/redirect/myscore"
                #     },
            }
        ]
    })
    return HttpResponse(json.dumps(resp))


# @login_required
def deleteMenu(request):
    print('deleteMenu', client.access_token)
    resp = client.menu.delete()
    return HttpResponse(json.dumps(resp))


# @login_required
def getMenu(request):
    # client = WeChatClient(settings.WECHAT_APPID, settings.WECHAT_SECRET)
    print('getMenu', client.access_token)
    resp = client.menu.get()
    # print(resp)
    return HttpResponse(json.dumps(resp, ensure_ascii=False))


def getUrl(item):
    if item is None:
        return APP_URL + '/index'
    else:
        return APP_URL + '/' + item


@csrf_exempt
def redirectUrl(request, item):
    case_id = request.GET.get('case_id', None)
    code = request.GET.get('code', None)
    openid = request.session.get('openid', None)
    print('code=', code)
    print('openid=', openid)
    print('case_id=', case_id)
    if openid is None:
        if code is None:  # 获取授权码code
            redirect_url = '%s/redirect/%s' % (APP_URL, item)
            webchatOAuth = WeChatOAuth(APPID, APPSECRET, redirect_url, 'snsapi_userinfo')
            authorize_url = webchatOAuth.authorize_url
            print(authorize_url)
            return HttpResponseRedirect(authorize_url)
        else:  # 同意授权，通过授权码获取ticket,根据ticket拉取用户信息
            webchatOAuth = WeChatOAuth(APPID, APPSECRET, '', 'snsapi_userinfo')
            res = webchatOAuth.fetch_access_token(code)
            if 'errcode' in res:
                return HttpResponse(json.dumps(res))
            else:

                open_id = webchatOAuth.open_id
                print(openid,'openid')
                count = Civil.objects.filter(openid=open_id, subscribe=1).count()
                if count == 0:
                    userinfo = webchatOAuth.get_user_info()
                    print(userinfo)
                    userinfo.pop('privilege')
                    Civil.objects.create(**userinfo)

                request.session['openid'] = open_id
                userinf = get_object_or_404(Civil, openid=open_id)
                request.session['nickname'] = userinf.nickname
                request.session['headimgurl'] = userinf.headimgurl
                redirect_url = getUrl(item)
                return HttpResponseRedirect(redirect_url)
    else:
        userinf = get_object_or_404(Civil, openid=openid)
        request.session['headimgurl'] = userinf.headimgurl

        redirect_url = getUrl(item)
        return HttpResponseRedirect(redirect_url)

#获取用户信息
@csrf_exempt
def getUserinfo(request):
    print('code=', '----------')
    appid = settings.WECHAT_APPID
    appsecret = settings.WECHAT_SECRET
    code = request.GET.get('code', None)
    print('code=', code)
    access_token_url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid={0}&secret={1}&code={2}&grant_type=authorization_code'
    access_token_url = access_token_url.format(appid, appsecret, code)
    res = requests.get(access_token_url)
    json_data = res.json()
    print(json_data,5666666)
    access_token = json_data['access_token']
    open_id = json_data['openid']

    userinfo_url = 'https://api.weixin.qq.com/sns/userinfo?access_token={0}&openid={1}&lang=zh_CN'
    userinfo_url = userinfo_url.format(access_token, open_id)
    resp = requests.get(userinfo_url)
    result = json.loads(resp.content.decode('utf-8', 'ignore'), strict=False)
    print(type(result))
    return HttpResponse("sucess")

# 网页授权
def authlist(request):
    appid = settings.WECHAT_APPID
    appsecret = settings.WECHAT_SECRET
    code = request.GET.get('code', None)
    print('code=', code)
    access_token_url = 'https://api.weixin.qq.com/sns/oauth2/access_token?appid={0}&secret={1}&code={2}&grant_type=authorization_code'
    access_token_url = access_token_url.format(appid, appsecret, code)
    res = requests.get(access_token_url)
    json_data = res.json()
    print(json_data)
    access_token = json_data['access_token']
    open_id = json_data['openid']

    count = WxLaw.objects.filter(openid=open_id, subscribe=1).count()
    if count == 0:
        userinfo_url = 'https://api.weixin.qq.com/sns/userinfo?access_token={0}&openid={1}&lang=zh_CN'
        userinfo_url = userinfo_url.format(access_token, open_id)
        resp_user = requests.get(userinfo_url)
        resp_userinfo = json.loads(resp_user.content.decode('utf-8', 'ignore'), strict=False)
        print(resp_userinfo)
        resp_userinfo.pop('privilege')
        WxLaw.objects.create(**resp_userinfo)

    return HttpResponse("success.....")