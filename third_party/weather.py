# {
#     "reason": "查询成功!",
#     "result": {
#         "city": "北京",
#         "realtime": {
#             "temperature": "10",
#             "humidity": "37",
#             "info": "晴",
#             "wid": "00",
#             "direct": "南风",
#             "power": "2级",
#             "aqi": "141"
#         },
#         "future": [
#             {
#                 "date": "2020-02-10",
#                 "temperature": "-5/12℃",
#                 "weather": "晴",
#                 "wid": {
#                     "day": "00",
#                     "night": "00"
#                 },
#                 "direct": "南风转东北风"
#             },
#             {
#                 "date": "2020-02-11",
#                 "temperature": "-3/11℃",
#                 "weather": "晴",
#                 "wid": {
#                     "day": "00",
#                     "night": "00"
#                 },
#                 "direct": "南风转北风"
#             },
#             {
#                 "date": "2020-02-12",
#                 "temperature": "-2/11℃",
#                 "weather": "晴",
#                 "wid": {
#                     "day": "00",
#                     "night": "00"
#                 },
#                 "direct": "北风"
#             },
#             {
#                 "date": "2020-02-13",
#                 "temperature": "-2/9℃",
#                 "weather": "多云转雨夹雪",
#                 "wid": {
#                     "day": "01",
#                     "night": "06"
#                 },
#                 "direct": "北风转东风"
#             },
#             {
#                 "date": "2020-02-14",
#                 "temperature": "-3/5℃",
#                 "weather": "小雪",
#                 "wid": {
#                     "day": "14",
#                     "night": "14"
#                 },
#                 "direct": "东北风"
#             }
#         ]
#     },
#     "error_code": 0
# }
import json
import requests


def get_weather_data(city_name):
    app_key = "c40e7aea7f550e5e24cc4af8ae5678df"
    api_url = "http://apis.juhe.cn/simpleWeather/query"
    params = {
        "city": city_name,
        "key": app_key
    }
    response = requests.get(api_url, params=params)
    result = json.loads(response.text)
    print(result)

    if int(result.get("error_code")) == 0:
        return {"status": 1, "data": result.get("result").get("future")}
    else:
        return {"status": 0, "error_msg": "请求失败！"}


if __name__ == '__main__':
    data = get_weather_data("北京")
