from django.conf.urls import url

from . import views

app_name = 'blogs'
urlpatterns = [

    url(
        r'^$',
        views.BlogsListView.as_view(),
        name='blogs'
    ),
    url(
        r'^(?P<pk>\d+)/create',
        views.PostCreateView.as_view(),
        name = 'create',
    ),

    url(
        r'^(?P<pk>\d+)/(?P<post_id>\d+)/update',
        views.PostUpdateView.as_view(),
        name = 'update',
    ),
    url(
        r'^(?P<pk>\d+)',
        views.PostsListView.as_view(),
        name = 'blog',
    ),


    url(
        r'^(?P<pk>\d+)/subscribe',
        views.SubscribeView.as_view(),
        name = 'subscribe',
    ),

    url(
        r'^unsubscribe/(?P<pk>\d+)',
        views.UnSubscribeView.as_view(),
        name='unsubscribe',
    ),





]