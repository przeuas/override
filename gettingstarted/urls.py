from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views


# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    path('admin/', admin.site.urls),
    path('post/new/', hello.views.post_new, name='post_new'),
    path('post/<int:pk>/', hello.views.post_detail, name='post_detail'),
    path('post/ <int:pk>/edit/', hello.views.post_edit, name='post_edit'),
    path('post/(?P<pk>\d+)/publish/$', hello.views.post_publish, name='post_publish'),
    path('post/(?P<pk>\d+)/remove/$', hello.views.post_remove, name='post_remove'),

]
