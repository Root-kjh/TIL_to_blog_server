from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def explorer(request):
    request = json.loads(request.body)
    return JsonResponse({
        'path': request['path']
    })

@csrf_exempt
def search(request):
    request = json.loads(request.body)
    ElasticSearch
    return JsonResponse({
        'keyword': request['keyword']
    })