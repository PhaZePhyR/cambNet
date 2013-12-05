from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cambnet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('home.urls', namespace='home', app_name='home')),
    url(r'^gigs/', include('gigs.urls', namespace='gigs', app_name='gigs')),
    url(r'^admin/', include(admin.site.urls)),
)