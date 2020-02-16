from django.http import JsonResponse
from user.models import User
from django.views import View
from utils import auth
import json
# Create your views here.


# 添加用户关心的城市
class UserInfoView(View):

    # 添加关心的城市
    def post(self, request):
        if not auth.already_authorized(request):
            response = {"status": 0, "error_msg": "auth fail"}
            return JsonResponse(response, safe=False)
        open_id = request.session.get('open_id')
        user = User.objects.get(open_id=open_id)
        # got str object
        received_body = request.body.decode('utf-8')
        received_body = eval(received_body)

        citie = received_body.get('city')
        before_citys = json.loads(user.focus_cities)
        if citie is not None and citie not in before_citys:
            before_citys.append(citie)
        user.focus_cities = json.dumps(before_citys)
        user.save()
        response = {"status": 1}
        return JsonResponse(response, safe=False)

