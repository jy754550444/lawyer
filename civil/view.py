# coding=utf-8
__author__ = 'yy'
from django.shortcuts import render, render_to_response, HttpResponse
from defendant.models import CivilAgent, Court_letter, Property, Indictment, Defence, Revoke, Appeal, Agentword, Evidence, \
    Force, Risk, Prove, Civil
import json
from lawyer.models import User, UserProfile
from django.views.generic import ListView, View, DetailView

class BathQrCodeAckView(View):
    def get(self, request, *args, **kwargs):
        try:
            code = request.GET.get("code", None)
            order = Civil.objects.get(case_id=code)
            # role = request.session.get("role", None)
            # if role == 1 or role ==2:
            # order.qr_status = True
            order.save()
        except Civil.DoesNotExist as ex :
            print(ex)
            order = None

        return render(request,'static/login.html', context={"object": order, "code": code})

# 民事代理表
def civilAgent(request):
    get_req = request.GET.get('req_id')
    all_data = CivilAgent.objects.get(id=get_req)
    return render_to_response('static/batch_change_form.html', {'all_data': all_data})


# 获取民事案件委托代理json数据
def civiliagent(request):
    case_id = request.GET.get('case_id')
    all_data = Civil.objects.get(case_id=case_id)
    law_name = request.GET.get('law_name')
    if law_name:
        laws = law_name[3:]
        name = laws.strip()
        all_names = UserProfile.objects.get(user__username=name)
        retValue = {'tel': all_data.tel, 'name': all_data.name, 'address': all_data.address, 'party': all_data.party,
                    'case_office': all_data.case_office, 'trial_level': all_data.trial_level, 'case': all_data.case,
                    'law_name': all_names.law.name, 'f_name': all_names.law.f_name, 'law_tel': all_names.tel,
                    'law_address': all_names.address,'b_name':all_data.b_name}
        return HttpResponse(json.dumps(retValue), content_type="application/json")


# 律师事务所民事出庭函
def court_letter(request):
    get_req = request.GET.get('req_id')
    all_data = Court_letter.objects.get(id=get_req)
    return render_to_response('static/court_letter.html', {'all_data': all_data})


# 财产保全申请书
def property(request):
    get_req = request.GET.get('req_id')
    all_data = Property.objects.get(id=get_req)
    return render_to_response('static/property.html', {'all_data': all_data})


# 起诉状
def indictment(request):
    get_req = request.GET.get('req_id')
    all_data = Indictment.objects.get(id=get_req)
    return render_to_response('static/indictment.html', {'all_data': all_data})


# 答辩状
def defence(request):
    get_req = request.GET.get('req_id')
    all_data = Defence.objects.get(id=get_req)
    return render_to_response('static/defence.html', {'all_data': all_data})


# 撤诉申请
def revoke(request):
    get_req = request.GET.get('req_id')
    all_data = Revoke.objects.get(id=get_req)
    return render_to_response('static/revoke.html', {'all_data': all_data})


# 上述状
def appeal(request):
    get_req = request.GET.get('req_id')
    all_data = Appeal.objects.get(id=get_req)
    return render_to_response('static/appeal.html', {'all_data': all_data})


# 强制执行申请书
def force(request):
    get_req = request.GET.get('req_id')
    all_data = Force.objects.get(id=get_req)
    return render_to_response('static/force.html', {'all_data': all_data})


# 证据目录
def evidence(request):
    get_req = request.GET.get('req_id')
    all_data = Evidence.objects.get(id=get_req)
    return render_to_response('static/evidence.html', {'all_data': all_data})


# 代理词
def agentword(request):
    get_req = request.GET.get('req_id')
    all_data = Agentword.objects.get(id=get_req)
    return render_to_response('static/agentword.html', {'all_data': all_data})


# 风险告知书
def risk(request):
    get_req = request.GET.get('req_id')
    all_data = Risk.objects.get(id=get_req)
    return render_to_response('static/risk.html', {'all_data': all_data})


# 法定代表人身份证明书
def prove(request):
    get_req = request.GET.get('req_id')
    all_data = Prove.objects.get(id=get_req)
    return render_to_response('static/prove.html', {'all_data': all_data})
