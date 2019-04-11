# coding=utf-8
__author__ = 'yy'
from django.shortcuts import render, render_to_response, HttpResponse
from criminal.models import Defendant_letter,Criminal_letter,CriminalAgent,CriminalAgents,Proxy,Proposal,Risks,Appraisal,Bail,Nonprosecution,Defensewords


#刑事案件辩护委托合同（一审阶段）
def criminalagent(request):
    get_req = request.GET.get('req_id')
    all_data = CriminalAgent.objects.get(id=get_req)
    return render_to_response('static/criminalagent.html',{'all_data':all_data})


#刑事案件授权委托书
def proxy(request):
    get_req = request.GET.get('req_id')
    all_data = Proxy.objects.get(id=get_req)
    context = {'all_data':all_data}
    return render(request,template_name='static/proxy.html',context=context )



#刑事案件辩护委托合同（二审阶段）
def criminalagents(request):
    get_req = request.GET.get('req_id')
    all_data = CriminalAgents.objects.get(id=get_req)
    return render_to_response('static/criminalagents.html',{'all_data':all_data})


#被告人专用介绍信
def defendant_letter(request):
    get_req = request.GET.get('req_id')
    all_data = Defendant_letter.objects.get(id=get_req)
    return render_to_response('static/defendant_letter.html',{'all_data':all_data})


#律师事务所出庭函
def criminal_letter(request):
    get_req = request.GET.get('req_id')
    all_data = Criminal_letter.objects.get(id=get_req)
    return render_to_response('static/criminal_letter.html',{'all_data':all_data})


#法律意见书
def proposal(request):
    get_req = request.GET.get('req_id')
    all_data = Proposal.objects.get(id=get_req)
    return render_to_response('static/proposal.html',{'all_data':all_data})


#重新司法鉴定申请
def appraisal(request):
    get_req = request.GET.get('req_id')
    all_data = Appraisal.objects.get(id=get_req)
    return render_to_response('static/appraisal.html',{'all_data':all_data})


#取保候审申请书
def bail(request):
    get_req = request.GET.get('req_id')
    all_data = Bail.objects.get(id=get_req)
    return render_to_response('static/bail.html',{'all_data':all_data})


#不起诉意见书
def nonprosecution(request):
    get_req = request.GET.get('req_id')
    all_data = Nonprosecution.objects.get(id=get_req)
    return render_to_response('static/nonprosecution.html',{'all_data':all_data})


#辩护词
def defensewords(request):
    get_req = request.GET.get('req_id')
    all_data = Defensewords.objects.get(id=get_req)
    return render_to_response('static/defensewords.html',{'all_data':all_data})


#风险告知书
def risks(request):
    get_req = request.GET.get('req_id')
    all_data = Risks.objects.get(id=get_req)
    return render_to_response('static/risks.html',{'all_data':all_data})