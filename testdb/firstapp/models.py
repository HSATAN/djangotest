from django.db import models

# Create your models here.

class First(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=10)
class test2(models.Model):
    name = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=10)
    class Meta:
        db_table = 'user' #设置表名