from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.oper_list, name='oper_list'),
    re_path(r'^oper/(?P<pk>\d+)/$', views.oper_detail, name='oper_detail'),
]

