from django.conf.urls import url
from. import views
from django.conf import settings
from django.conf.urls.static import static

urlpattern=[
    url("^$",views.welcome,name='welcome'),
    url('^today/$',views.news_of_day,name='newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^article/(\d+)',views.article,name ='article')

]
if setting.DEBUG:
    urlpatterns+=static(setting.MEDIA_URL,document_root = setting.MEDIA_ROOT)