from django.conf.urls import url
from booktest import views

urlpatterns = [
    # 分页显示地区的url
    url(r'^part_area(\d*)', views.part_area),
    # 省市县案例页面
    url(r'^show_area/$', views.show_area),
    # 查询省级地区
    url(r'^prov/$', views.prov),
    # 查询市级地区信息
    url(r'^city(\d+)/$', views.city),
]
