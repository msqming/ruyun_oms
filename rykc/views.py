from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from django.core import serializers

import json


from rykc import models

def index(request):


    return render(request,'index.html')

def api_index(request):

    data_list = models.CommInfo.objects.filter(id__lt=21)
    res = {
        'code':0,
        'msg':'',
        'data':[]
    }
    for data in data_list:
        res['data'].append({
            'id': data.id,
            'xinghao': data.xinghao,
            'pinlei': data.pinglei,
            'new_old': data.new_old,
            'dingwei': data.dingwei,
            'pinming': data.pingming,
            'cpu': data.cpu,
            'xianka': data.xianka,
            'neicun': data.neicun,
            'ssd': data.ssd,
            'hhd': data.hhd,
            'model_name': data.model_name,
            'config': data.config,
            'pn': data.pn
        })

    # s = serializers.serialize('json', res)
    s = json.dumps(res)

    return HttpResponse(s)

def data_upload(request):

    return render(request, 'data_upload.html')
