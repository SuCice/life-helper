from django.shortcuts import render
from django.http import JsonResponse
from user.models import App
# Create your views here.


# 获取可支持的应用列表
def get_menu(request):
    query_set = App.objects.all()
    all_app = []
    for app in query_set:
        all_app.append(app.to_dict())
    print(all_app)
    res = {
        "status": 1,
        "data": {"app_list": all_app}
    }
    return JsonResponse(data=res, safe=False)
