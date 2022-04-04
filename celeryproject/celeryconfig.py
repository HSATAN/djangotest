# _*_ coding:utf-8 _*_
from kombu import Queue, Exchange
BROKER_URL='amqp://guest:guest@49.235.125.109:5672/'
BROKER_RESULT_BACKEND = 'redis://default:hkj957455@49.235.125.109:6379/1'

CELERY_DEFAULT_QUEUES='default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_ROUTING_KEY= 'default'



CELERY_QUEUES = (
    Queue('queue1', Exchange(name='queue1',type='direct'),routing_key='queue1'),
    Queue('queue2',Exchange('queue2',type='direct'),routing_key='queue2')
)

CELERY_ROUTES = {
    'tasks.queue1':{'queue':'queue1','routing_key':'queue1'},
    'tasks.queue2':{'queue':'queue2', 'routing_key':'queue2'}
}


# 某个程序中出现的队列，在broker中不存在，则立刻创建它
CELERY_CREATE_MISSING_QUEUES = True

#CELERY_IMPORTS = ("async_task.tasks", "async_task.notify")

CELERYD_CONCURRENCY = 20
# 并发worker数

CELERY_TIMEZONE = 'Asia/Shanghai'
#设置时区
CELERYBEAT_SCHEDULE = {
'queue1-per-1-minutes':{#任务名字可以随便取
    'task':'tasks.queue1',
    'schedule':10,
    'args':('huangkaijie',)#一个参数后面必须有逗号，不然会解析错误，会把字符串的每一位当成一个参数
},
    'queue2-per-1-minutes':{
        'task':'tasks.queue2',
        'schedule':5,
        'args':(5,6)
    }
}


CELERY_ENABLE_UTC = True
#启动时区设置

CELERYD_FORCE_EXECV = True
# 非常重要,有些情况下可以防止死锁

CELERY_MESSAGE_COMPRESSION = 'zlib'
#压缩方案选择，可以是zlib, bzip2，默认是发送没有压缩的数据

CELERYD_PREFETCH_MULTIPLIER = 1
#celery worker 每次去BROKER中预取任务的数量 默认值就是4

CELERYD_MAX_TASKS_PER_CHILD = 100
# 每个worker最多执行万100个任务就会被销毁，可防止内存泄露 默认无限的

# CELERYD_TASK_TIME_LIMIT = 60
#  单个任务的运行时间不超过此值，否则会被SIGKILL 信号杀死 任务移交给父进程

# BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 90}
# 任务发出后，经过一段时间还未收到acknowledge , 就将任务重新交给其他worker执行

CELERY_DISABLE_RATE_LIMITS = True
#关闭限速

CELERY_ACKS_LATE = True
#任务发送完成是否需要确认，对性能会稍有影响

CELERY_TASK_RESULT_EXPIRES = 24 * 60 * 60
#任务过期时间，celery任务执行结果的超时时间

# CELERY_TASK_SERIALIZER = 'msgpack'
# #指定任务序列化方式
#
# CELERY_RESULT_SERIALIZER = 'msgpack'
# #指定结果序列化方式
#
# CELERY_ACCEPT_CONTENT = ['msgpack']
# #指定任务接受的序列化类型.

# 限制任务的执行频率
# 下面这个就是限制tasks模块下的add函数，每秒钟只能执行10次
# CELERY_ANNOTATIONS = {'tasks.add':{'rate_limit':'10/s'}}