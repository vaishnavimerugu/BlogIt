from django.conf.urls import url
from django.contrib.auth.views import logout
from . import views
urlpatterns=[
            url(r'^userhome/',views.userhome,name='userhome'),
            url(r'^newpost/', views.newpost, name='newpost'),
            url(r'^register/',views.register,name='register'),
            url(r'^login/',views.user_login,name='login'),
            url(r'^logout/$', 'django.contrib.auth.views.logout',{'next_page': '/blog/userhome'}),
            url(r'^post/$',views.post,name='post'),
            url(r'^all_blogs/',views.all_blogs,name='all_blogs')
            ]