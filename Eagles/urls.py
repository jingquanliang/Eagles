#coding=utf-8
"""Eagles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from advertise import views as leran_advertise
from calc import views as calc_views

from calc.views import MyView
from calc.views import HomePageView
from calc.views import ArticleDetailView
from calc.views import ArticleListView
from chat import views

urlpatterns = [
    #url(r'^$', leran_advertise.home, name='home'),
    # url(r'^$', calc_views.index, name='home'),
    url(r'^$',  views.about, name='about'),
    url(r'^add/$', calc_views.add, name='add'),  # 注意修改了这一行
    url(r'^add/(\d+)/(\d+)/$', calc_views.add, name='add2'),
    url(r'^admin/', admin.site.urls),
    url(r'^mine/$', MyView.as_view(), name='my-view'),
    url(r'^templateView/$', HomePageView.as_view(), name='home'),
    # url(r'^(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
    url(r'^listview$', ArticleListView.as_view(), name='article-list'),
    url(r'^new/$', views.new_room, name='new_room'),
    url(r'^(?P<label>[\w-]{,50})/.*/$', views.chat_room, name='chat_room'),
]
