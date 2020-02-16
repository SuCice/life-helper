from django.http import JsonResponse
from user.models import User
import json
from utils.auth import get_open_id, already_authorized
# Create your views here.


# 登陆
def login_auth(request):
    response = {}
    post_data = request.body.decode('utf-8')
    post_data = json.loads(post_data)
    app_id = post_data.get('app_id').strip()
    nickname = post_data.get('nickname').strip()
    code = post_data.get('code').strip()
    print(app_id, nickname, code)
    if not (app_id and code):
        response['status'] = 0
        response['error_msg'] = 'authorized failed. need entire authorization data.'
        return JsonResponse(response, safe=False)
    try:
        open_id = get_open_id(app_id, code)
    except Exception as e:
        print(e)
        response['status'] = 0
        response['error_msg'] = 'authorized error'
        return JsonResponse(response, safe=False)
    if not open_id:
        response['status'] = 0
        response['error_msg'] = 'authorized error!'
        return JsonResponse(response, safe=False)
    request.session['open_id'] = open_id
    request.session['is_authorized'] = True

    # 如果用户不存在，则新建用户
    if not User.objects.filter(open_id=open_id):
        user = User(open_id=open_id, focus_cities=json.dumps(["北京"]))
        user.save()
    return JsonResponse(data={"status": 1}, safe=False)


# 判断是否已经登陆
def get_login_status(request):
    if already_authorized(request):
        data = {"is_authorized": 1}
    else:
        data = {"is_authorized": 0}
    return JsonResponse(data={"status": 1, "data": data}, safe=False)


# 注销
def logout(request):
    request.session.clear()
    return JsonResponse(data={"status": 1}, safe=False)
