from money.models import Money, MoneyPrice
# Create your views here.

from django.http import JsonResponse
from django.views import View
from user.models import User
# 获取货币信息


# 获取用户的自定义的货币提醒
def get_money_price_log(request):
    open_id = request.session.get('open_id')
    user = User.objects.get(open_id=open_id)
    data = []
    money = MoneyPrice.objects.filter(user=user)
    for money_data in money:
        data.append({
            "id": money_data.id,
            "name": money_data.money.name,
            "price_type": money_data.price_type,
            "price": money_data.price
        })
    res = {"status": 1, "data": data}
    return JsonResponse(data=res, safe=False)


def delete_data(request):
    price_id = request.GET.get("id")
    print("删除，，，，，，，", price_id)
    money_price = MoneyPrice.objects.get(id=price_id)
    money_price.delete()
    response = {"status": 1}
    return JsonResponse(response, safe=False)


# 获取货币价格、添加、删除点位提醒
class MoneyView(View):
    def get(self, request):
        data = []
        money = Money.objects.all()
        for money_data in money:
            if money_data.name == "eth":
                data.append({
                    "name": '以太坊',
                    "price": money_data.price
                })
            if money_data.name == "btc":
                data.append({
                    "name": '比特币',
                    "price": money_data.price
                })
        res = {"status": 1, "data": data}
        return JsonResponse(data=res, safe=False)

    def post(self, request):
        print("ssssssssssss")
        open_id = request.session.get('open_id')
        user = User.objects.get(open_id=open_id)

        received_body = request.body.decode('utf-8')
        print(received_body)

        received_body = eval(received_body)
        print(received_body)

        money_name = received_body.get('money_name')
        price_type = received_body.get('price_type')
        price = float(received_body.get('price'))

        money = Money.objects.get(name=money_name)
        money_price = MoneyPrice(
            user=user,
            money=money,
            price_type=price_type,
            price=price
        )
        money_price.save()
        response = {"status": 1}
        return JsonResponse(response, safe=False)
