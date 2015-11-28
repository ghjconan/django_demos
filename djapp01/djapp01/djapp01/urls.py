"""
Definition of urls for djapp01.
"""

from datetime import datetime
from django.conf.urls import patterns, url, include
from webui.forms import BootstrapAuthenticationForm
from webui import views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^contact$', views.ContactView.as_view(), name='contact'),
    url(r'^about', views.AboutView.as_view(), name='about'),
    url(r'^people', views.PeopleView.as_view(), name='people'),
    url(r'^api/', include('api.urls')),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'webui/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
