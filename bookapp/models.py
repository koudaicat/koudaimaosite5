from django.db import models


# Create your models here.
class Bookinfo(models.Model):
    btitle = models.CharField(max_length=20)#图书名称，charfield是一个字符串
    bpub_date = models.DateField()


def __str__(self):
    return self.btitle

class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)#英雄名称
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=128)
    #建立和book类和英雄类一对多的关系
    #hbook = models.ForeignKey('BookInfo'）#报错
    hbook = models.ForeignKey('Bookinfo', on_delete=models.CASCADE)#on_delete是为了防止两个表数据不对应，是2.0版本后才有的参数

def __str__(self):
    return self.hname
