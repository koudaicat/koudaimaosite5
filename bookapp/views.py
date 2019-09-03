from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext
from bookapp.models import Bookinfo #加载图书类

# Create your views here.
def index(request):#request是http的返回值
    #进行处理，M和T的交互
    return HttpResponse("老铁，没毛病")


def my_render(request,tempate_path,context_dict={}):
    temp = loader.get_template(tempate_path)
    # 2、定义模板上下文，给模板文件传递数据
    context = RequestContext(request, context_dict)
    # 3、模板渲染，产生标准html内容
    res_html = temp.render()
    # 4、返回给游览器
    return HttpResponse(res_html)
def index2(request):#request是http的返回值
    #进行处理，M和T的交互
    return render(request, "bookapp/index.html",
                  {'content': 'hello world',
                   'list': list(range(1, 10))})

def show_books(request):
    """显示图书信息"""
    #1、通过M查图书表中的数据
    books = Bookinfo.objects.all()
    #2、使用模板
    return render(request,'bookapp/show_books.html',{'books':books})


def detail(request,bid):
    """查询图书关联英雄信息"""
    #1、根据bid查询图书信息
    book = Bookinfo.objects.get(id=bid)
    #查询预book关联的英雄信息
    heros = book.heroinfo_set.all()
    #使用模板
    return render(request,"bookapp/detail.html",{"book":book,"heros":heros})





