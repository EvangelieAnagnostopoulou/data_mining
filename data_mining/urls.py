from django.conf.urls import patterns, include, url
from django.contrib import admin
from data_mining import views
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'data_mining.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='home'),
    url(r'', include('social_auth.urls')),
    url(r'^getdata', login_required(views.get_facebook_data)),
    url(r'^thanks', login_required(views.thanks)),
    # Authentication module
    url(r'^accounts/', include('allauth.urls')),

)
