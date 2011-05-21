from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    ('^_ah/warmup$', 'djangoappengine.views.warmup'),

    ('^intro$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    #static assets (should be local-only)                   
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': 'media'}),

    (r'^time/add/$', 'timetracker.views.add'),
    (r'^time/start_timer/$', 'timetracker.views.start_task_timer'),
    (r'^time/clear_timer/$', 'timetracker.views.clear_task_timer'),

    (r'', 'timetracker.views.dashboard'),
)
