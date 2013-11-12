from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # index page at /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # details of specific poll ex: /polls/5
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name="detail"),
    # results of specific poll ex: /polls/5/results
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name="results"),
    # votes of specific poll ex: /polls/5/votes
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name="vote"),
)