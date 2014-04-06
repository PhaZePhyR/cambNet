from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers

#from gigs import views

admin.autodiscover()

router = routers.DefaultRouter()
#router.register(r'gigs', views.GigViewSet)

urlpatterns = patterns('',
    #url(r'^', include(router.urls)),
    url(r'^', include('home.urls', namespace='home', app_name='home')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^gigs/', include('gigs.urls', namespace='gigs', app_name='gigs')),
    url(r'^admin/', include(admin.site.urls)),
)

"""
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cambnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('home.urls', namespace='home', app_name='home')),
    url(r'^gigs/', include('gigs.urls', namespace='gigs', app_name='gigs')),
    url(r'^admin/', include(admin.site.urls)),
)
"""