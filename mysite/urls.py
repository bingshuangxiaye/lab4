from django.conf.urls.defaults import *
from views import hello
from books import views          #����views���뺯��
from django.conf import settings
#settings.configure()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.begin),    #welcome to the bookdb
    url(r'^search-form/$',views.search_form), #��ѯ����
    url(r'^search/$',views.search),#��ѯ���ҳ��
    url(r'^show/$',views.show),#���������Ϣչʾҳ��
    url(r'^delete/$',views.delete),#ɾ��ĳһ����
    url(r'^book_author/$',views.book_author),#��ʾĳ�������ϸ��Ϣ
    url(r'^welcome/$',views.begin), #welcome to the bookdb
    url(r'^add/$',views.bookinsert),#����ĳ����
    url(r'^add_author/$',views.authorinsert),#��������
    url(r'^ask/$',views.add_ask),#�����ӣ�����ѯ�����������Ƿ���Ҫ��������
    url(r'^book_modify/$',views.bookmodify),#�޸�ͼ����Ϣ
    url(r'^showauthor/$',views.showauthor),#��ʾ������Ϣ
    url(r'^author_modify/$',views.authormodify),#�޸�������Ϣ
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
