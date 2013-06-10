from django.conf.urls import patterns, include, url
from django.views.generic import UpdateView
from django.conf import settings

from t5_editform.views import CustomProfileUpdateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', include('t1_contact.urls')),
    url(r'^requests/$', include('t3_httprequests.urls')),
    url(r'^update/(?P<pk>\d+)/$',  CustomProfileUpdateView.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT, }),
    
)
