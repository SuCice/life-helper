from django.urls import path
from .views import menu, auth, user_info

urlpatterns = [
    path('menu', menu.get_menu, name='menu'),
    path('login_auth', auth.login_auth, name='login_auth'),
    path('login_status', auth.get_login_status, name='get_login_status'),
    path('logout', auth.logout, name='logout'),
    path('user_city', user_info.UserInfoView.as_view(), name='user_city'),
]