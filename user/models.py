from django.db import models

# Create your models here.


# 入口功能清单描述
class App(models.Model):
    app_id = models.CharField(primary_key=True, max_length=32)  # 唯一ID
    name = models.CharField(max_length=128)  # 中文名字

    def to_dict(self):
        return {
            'app_id': self.app_id,
            'name': self.name
        }

    # def __str__(self):
    #     return '%s(%s)' % (self.name, self.application)
    #
    # def __repr__(self):
    #     return '%s(%s)' % (self.name, self.application)


# 用户信息表
class User(models.Model):
    # open_id
    open_id = models.CharField(max_length=64, unique=True)
    # 昵称
    nickname = models.CharField(max_length=256)
    # 关注的城市
    focus_cities = models.TextField(default='[]')

    class Meta:
        indexes = [
            models.Index(fields=['open_id'])
        ]

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return self.nickname
