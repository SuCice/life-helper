# 获取火币网货币信息插入数据库
import os
import json
import requests

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "life_helper.settings")
import django
django.setup()
from money.models import Money


def get_huobi_data():
    api_url = "https://www.huobi.io/-/x/pro/market/overview5?r=ri4a6"
    response = requests.get(api_url)
    result = json.loads(response.text)
    print(result)
    if result.get("status") == 'ok':
        for x in result.get("data"):
            if x.get("symbol") == "ethusdt":
                eth_data = x.get("close")
            if x.get("symbol") == "btcusdt":
                btc_data = x.get("close")
    btc_money = Money.objects.get(name="btc")
    btc_money.price = btc_data
    btc_money.save()
    eth_money = Money.objects.get(name="eth")
    eth_money.price = eth_data
    eth_money.save()
    #
    # money_pirce_highs = MoneyPrice.objects.filter(price_type="高位", money=btc_money)
    # for x in money_pirce_highs:
    #     if btc_data > x.price:
    #         pass
    #     pass


if __name__ == '__main__':
    data = get_huobi_data()