from django.conf.urls import patterns, url

from . import views

# url(r'<regex>', <views.name> [, {<kwargs>}, <name>] ),

urlpatterns = patterns('', 
	url(r'^$', views.IndexView.as_view(), name="index"),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name="detail"),
	url(r'^results/$', views.ResultsView.as_view(), name="results"),
	url(r'^create/$', views.GigCreate.as_view(), name="create"),
	url(r'^submit/$', views.GigCreate.as_view(), name="submit"),
	url(r'^(?P<pk>\d+)/update/$', views.GigUpdate.as_view(), name="update"),	
	url(r'^(?P<pk>\d+)/delete/$', views.GigDelete.as_view(), name="delete"),
	# SignUps
	url(r'^(?P<pk>\d+)/signup/', views.GigSignUp.as_view(), name="signup"),
)  
