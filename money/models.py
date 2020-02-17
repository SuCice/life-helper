from django.db import models
from user.models import User
# Create your models here.


# 虚拟货币表
class Money(models.Model):
    # 货币的名字
    name = models.CharField(max_length=256)
    # 价格点位
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


# 虚拟货币价格提醒表
class MoneyPrice(models.Model):
    # 点位类型
    price_type = models.CharField(max_length=256)
    # 价格点位
    price = models.FloatField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    money = models.ForeignKey(Money, on_delete=models.CASCADE)

    def __str__(self):
        return self.price_type

    def __repr__(self):
        return self.price_type