from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/ <int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    path('post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    #url(r'^$', hello.views.index, name='index'),
    path(r'^db', views.db, name='db'),
]
