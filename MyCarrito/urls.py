"""MyCarrito URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.conf import settings
dajaxice_autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    	url(r'^$', 'app.views.home'),
    #(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')), #DAJAXICE
	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^(bikes|books|music)/$', 'app.views.category', \
			name="category"),
	url(r'^(?P<category>(bikes|books|music))/(?P<p_id>\d{1,})-(.*)/$',\
		 'app.views.product', name="product"),
	url(r'^checkout/$', 'app.views.checkOut',\
	 	name="checkOut"),
	url(r'^logout/$', 'userprofiles.views.userLogOut', name="userLogOut"),
	url(r'^search$', 'app.views.search'),
	url(r'^sign/$', 'userprofiles.views.signDispatcher', name="sign"),
	url(r'^upload/(?P<path>.*)$', 'django.views.static.serve',
					{'document_root':settings.MEDIA_ROOT}),
]

urlpatterns += staticfiles_urlpatterns()