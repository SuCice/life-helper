from django.urls import path
from .views import views

urlpatterns = [
    path('', views.MoneyView.as_view(), name='index'),
    path('price_log', views.get_money_price_log, name='price_log'),
    path('delete', views.delete_data, name='delete_data'),
]
