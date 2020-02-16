# from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from third_party import weather
from django.views import View
import utils
import json
from user.models import User
# 获取天气信息


class WeatherView(View):
    def get(self, request):
        if not utils.auth.already_authorized(request):
            res = {"status": 0, "error_msg": "auth fail"}
        else:
            data = []
            open_id = request.session.get('open_id')
            user = User.objects.filter(open_id=open_id)[0]
            cities = json.loads(user.focus_cities)
            for city in cities:
                result = weather.get_weather_data(city)
                data.append({
                    "city_name": city,
                    "weather_list": result.get("data")[0]
                })
            res = {"status": 1, "data": data}
        return JsonResponse(data=res, safe=False)

