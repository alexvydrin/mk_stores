from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.oper_list, name='oper_list'),
    re_path(r'^oper/(?P<pk>\d+)/$', views.oper_detail, name='oper_detail'),
    re_path(r'^oper/new/$', views.oper_new, name='oper_new'),
    re_path(r'^oper/(?P<pk>\d+)/edit/$', views.oper_edit, name='oper_edit'),
]

