from django.conf.urls import url

from . import views

app_name = 'pollApp'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='indexName'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detailName'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='resultsName'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='voteName'),
]