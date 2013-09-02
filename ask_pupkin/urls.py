from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_pupkin.views.home', name='home'),
    # url(r'^ask_pupkin/', include('ask_pupkin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'askPupkinApp.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
	url( r'^login/$', 'askPupkinApp.views.log_in', name='log_in'),
	url(r'^questions/(?P<question_id>\d+)$', 'askPupkinApp.views.questions', name='questions'),
	url( r'^logout/$', 'askPupkinApp.views.log_out', name='log_out'),
	url(r'^users/(?P<user_id>\d+)$', 'askPupkinApp.views.users', name='users'),
)
