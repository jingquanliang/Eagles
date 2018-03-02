#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

from django.views.generic import View

from django.views.generic.base import TemplateView

from calc.models import Article

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone



class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

class HomePageView(TemplateView):

    template_name = "calc/base.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context

class ArticleDetailView(DetailView):

    model = Article # 要显示详情内容的类

    template_name = 'calc/article_detail.html'
    # 模板名称，默认为 应用名/类名_detail.html（即 app/modelname_detail.html）

    # 在 get_context_data() 函数中可以用于传递一些额外的内容到网页
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['object'] = Article.objects.all()[:5]
        context['now'] = timezone.now()
        return context

class ArticleListView(ListView):

    model = Article

    template_name = 'calc/article_list.html'
    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

@cache_page(60 * 15) # 秒数，这里指缓存 15 分钟，不直接写900是为了提高可读性
def add(request,a,b):
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def index(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    return render(request, 'calc/home.html', {'string': string})
