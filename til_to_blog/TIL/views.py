from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from lib.ElasticSearch import ElasticSearch
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
    result = ElasticSearch.find_by_keyword(request['keyword'])
    print(result)
    file_list = list()
    for file in result['hits']['hits']:
        temp_file = {"file_name": file['_source']['name'], "file_path": file['_source']['path']}
        file_list.append(temp_file)
    return JsonResponse({
        "file_list":file_list
    })