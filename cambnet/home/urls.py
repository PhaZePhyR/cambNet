from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('', 
	url(r'^$', views.IndexView.as_view(), name="index"),
	url(r'^contacts/$', views.ContactsView.as_view(), name="contacts"),
	url(r'^login/$', views.LoginView.as_view(), name="login"),	
	url(r'^logout/$', views.LogoutView.as_view(), name="logout"),
)	