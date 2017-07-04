from django.conf.urls import url

from . import views

app_name = 'blogs'
urlpatterns = [

    url(
        r'^$',
        views.BlogListView.as_view(),
        name='blogs'
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