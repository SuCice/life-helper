import json
import requests

'''
return data 的格式
{
  "session_key": "JmRNs6uPEpFzlMRmg4NqJQ==",
  "expires_in": 7200,
  "openid": "oXSML0ZH05BItFTFILfgCGxXxxik"
}
'''


# 获取open_id
def wx_get_open_id(appid, code):
    host = 'https://api.weixin.qq.com/sns/jscode2session'
    params = 'appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % \
             (appid, 'f61d140c8394cad4681b2a5afc46c8d3', code)
    url = host + '?' + params
    response = requests.get(url=url, proxies={})
    data = json.loads(response.text)
    open_id = data.get('openid')
    return open_id
