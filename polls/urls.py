from django.conf.urls import url

from . import views

#TODO: This is an individual per-app basis URL file.


#views.<name of function in view>



urlpatterns = [
    # ex: /polls/
    #name is used to as reference from template
   # url(r'^$', views.index, name='index'),


    # ex: /polls/5/
    # question_id is picked up as a query string and sent over to the View method
    # # The question_id='34' part comes from (?P<question_id>[0-9]+).
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),


]

