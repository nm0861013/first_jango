from django.shortcuts import render

from django.http import HttpResponse
import json

# Create your views here.
def my_view(request):
    if request.method == 'POST':
        # 獲取json格式的data
        data = json.loads(request.body)

        # 做適當的處理
        result = {'message': 'Hello ' + data['name']}

        # 將處理好的data轉換成json格式
        json_result = json.dumps(result)

        # 回傳json格式的data
        return HttpResponse(json_result, content_type='application/json')

def my_view2(request):
    if request.method == 'POST':
        # 处理逻辑
        my_data = request.POST.get('my_data')
        # 返回HTTP响应
        return HttpResponse('Received data: {}'.format(my_data))
    else:
        return HttpResponse('Hello, world!')

def my_view3(request):
    name = request.GET.get('name')
    if name == 'joy':
        return HttpResponse('你的名字是 joy')
    return HttpResponse('請提交一個POST請求並包含名字為 joy 的數據')
#http://127.0.0.1:8000/project/my_view3/?name=joy