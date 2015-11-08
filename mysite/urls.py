from django.conf.urls.defaults import *
from views import hello
from books import views          #链接views导入函数
from django.conf import settings
#settings.configure()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.begin),    #welcome to the bookdb
    url(r'^search-form/$',views.search_form), #查询函数
    url(r'^search/$',views.search),#查询结果页面
    url(r'^show/$',views.show),#所有书的信息展示页面
    url(r'^delete/$',views.delete),#删除某一本书
    url(r'^book_author/$',views.book_author),#显示某本书的详细信息
    url(r'^welcome/$',views.begin), #welcome to the bookdb
    url(r'^add/$',views.bookinsert),#新增某本书
    url(r'^add_author/$',views.authorinsert),#新增作者
    url(r'^ask/$',views.add_ask),#超链接，用于询问新增的书是否需要新增作者
    url(r'^book_modify/$',views.bookmodify),#修改图书信息
    url(r'^showauthor/$',views.showauthor),#显示作者信息
    url(r'^author_modify/$',views.authormodify),#修改作者信息
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
