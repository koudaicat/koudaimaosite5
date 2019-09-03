from django.contrib import admin
from bookapp.models import  Bookinfo
from bookapp.models import HeroInfo

'''class BookinfoAdmin(admin,ModelAdmin):
    #图书模型管理类
    list_display=["id","btitle","bpub_date"]'''


admin.site.register(Bookinfo)# Register your models here.
admin.site.register(HeroInfo)