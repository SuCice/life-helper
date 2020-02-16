from user.models import User

from utils.wx.session import wx_get_open_id


# 判断是否已经授权
def already_authorized(request):
    print(request.session.get('is_authorized'))
    is_authorized = True if request.session.get('is_authorized') else False
    return is_authorized


# 根据open_id 获取user用户对象
def get_user(request):
    if not already_authorized(request):
        raise Exception('not authorized request')
    open_id = request.session.get('open_id')
    user = User.objects.get(open_id=open_id)
    return user


def get_open_id(app_id, code):
    return wx_get_open_id(app_id, code)
