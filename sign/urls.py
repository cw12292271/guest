from django.urls import path
from sign import views_if
app_name = "sign"
urlpatterns = [
    path('add_event/', views_if.add_event, name='add_event'),
    path('add_guest/', views_if.add_guest, name='add_guest'),
    path('get_event_list/', views_if.get_event_list, name='get_event_list'),
    path('get_guest_list/', views_if.get_guest_list, name='get_guest_list'),
    path('user_sign/', views_if.user_sign, name='user_sign'),
]