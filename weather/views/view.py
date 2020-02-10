# from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from third_party import weather


# 获取天气信息
# @params = {"city_name": "xxx"}
def get_weather(request):
    if request.method == "GET":
        city_name = request.GET.get("city_name")
        result = weather.get_weather_data(city_name)
        if result.get("status") == 0:
            data = {"status": 0, "error_msg": "请求错误"}
        else:
            data = {
                "status": 1,
                "data": {
                    "city_name": city_name,
                    "weather_list": result.get("data")
                }
            }
        return JsonResponse(data=data, status=200)
    else:
        return JsonResponse(data={"status": 0, "error_msg": "请求错误"}, status=200)
