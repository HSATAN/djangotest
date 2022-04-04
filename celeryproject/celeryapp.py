# _*_ coding:utf-8 _*_
from celery import Celery
app = Celery('celeryproject', include=['celeryproject.tasks'])
app.config_from_object('celeryproject.celeryconfig')
if __name__ == '__main__':
    app.start()