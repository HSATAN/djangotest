# _*_ coding:utf-8 _*_
from kombu import Queue, Exchange
BROKER_URL='amqp://guest:guest@49.235.125.109:5672/' #消息中间件的url
BROKER_RESULT_BACKEND = 'redis://default:hkj957455@49.235.125.109:6379/1'#中间结果的存储url
CELERY_TASK_SERIALIZER = 'json' #指定任务序列化方式
CELERY_RESULT_SERIALIZER = 'json'#指定结果序列化方式
CELERY_TASK_RESULT_EXPIRES =60 # 任务过期时间,celery任务执行结果的超时时间
CELERY_CREATE_MISSING_QUEUES = True # 某个程序中出现的队列，在broker中不存在，则立刻创建它
CELERYD_CONCURRENCY = 20  # 并发worker数
CELERY_TIMEZONE = 'Asia/Shanghai'

CELERYD_FORCE_EXECV = True    # 非常重要,有些情况下可以防止死锁

CELERYD_PREFETCH_MULTIPLIER = 1

CELERYD_MAX_TASKS_PER_CHILD = 100    # 每个worker最多执行万100个任务就会被销毁，可防止内存泄露
# CELERYD_TASK_TIME_LIMIT = 60    # 单个任务的运行时间不超过此值，否则会被SIGKILL 信号杀死
# BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 90}
# 任务发出后，经过一段时间还未收到acknowledge , 就将任务重新交给其他worker执行
CELERY_DISABLE_RATE_LIMITS = True

CELERY_DEFAULT_QUEUES='default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_ROUTING_KEY= 'default'



#设置队列列表
CELERY_QUEUES = (
    Queue('queue1', Exchange(name='queue1',type='direct'),routing_key='queue1'),
    Queue('queue2',Exchange('queue2',type='direct'),routing_key='queue2')
)


#该设置将每一个任务绑定到指定的队列中
CELERY_ROUTES = {
    'tasks.queue1':{'queue':'queue1','routing_key':'queue1'},
    'tasks.queue2':{'queue':'queue2', 'routing_key':'queue2'}
}