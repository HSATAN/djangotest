# _*_ coding:utf-8 _*_
from celery import Celery
# broker='amqp://guest:guest@49.235.125.109:5672/'
# #broker = 'redis://127.0.0.1:6379/0'
# backend = 'redis://default:hkj957455@49.235.125.109:6379/1'
#

app = Celery()
app.config_from_object('celeryconfig')

@app.task
def queue1(message):
    return '这是队列1 %s '%message

@app.task
def queue2(x, y):
    return '这是队列2 计算两个数之和 %d' %(x + y)

# app.conf.task_routes = {
#     'tasks.add':{'queue':'add', 'routing_key':'add'},
#     'tasks.task1':{'queue':'task1', 'routing_key':'task1'},
# }