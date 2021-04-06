from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from lib.ElasticSearch import ElasticSearch
import json
import os

TIL_DIR = "/git/til"

@csrf_exempt
def explorer(request):
    request = json.loads(request.body)
    path = os.path.realpath(TIL_DIR+request['path'])
    if os.path.commonprefix((path,TIL_DIR)) != TIL_DIR:
        return JsonResponse({
            "message": "fail"
        })
    if os.path.isdir(path):
        file_type = "folder"
        file_context = list()
        for file in os.listdir(path):
            file_dict = dict()
                file_dict['file_name'] = file
                file_dict['file_path'] = path+file
            if os.path.isdir(path+file):
                file_dict['file_type'] = "folder"
            else:
                file_dict['file_type'] = "file"
            file_context.append(file_dict)
    else:
        file_type = "file"
        file = open(path,'r')
        file_context = file.read()
        file.close()

    return JsonResponse({
        "file_type": file_type,
        "file_context": file_context
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