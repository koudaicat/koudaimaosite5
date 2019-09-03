from django.conf.urls import url
from bookapp import views

urlpatterns=[
    #通过url函数设置url路由配置项
    url(r"^index$",views.index),
    url(r"^index2$",views.index2),
    url(r"^books$",views.show_books),#显示图书信息
    url(r"^books/(\d+)$",views.detail),#显示英雄信息
]
