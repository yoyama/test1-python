from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo1.views.home', name='home'),
    # url(r'^demo1/', include('demo1.foo.urls')),
    url(r'^download/.*$', 'test1.views.download', name='download'),
    url(r'^top/.*$', 'test1.views.index', name='index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
