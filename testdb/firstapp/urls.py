# _*_ coding:utf-8 _*_
from django.urls import path
from . import views
app_name = 'firstapp'
urlpatterns = [path('test',views.index, name='index'),
               path('index',views.index,name='index'),
               path('<int:month>/<int:year>', views.year),
               path('<int:month>',views.month, name='month'),
               path('insertuser',views.insertuser, name='insertuser')
               ]