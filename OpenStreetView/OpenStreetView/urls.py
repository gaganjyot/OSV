from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OpenStreetView.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'openstreetview.views.home'),
    url(r'^signup/$', 'openstreetview.views.signup'),
    url(r'^signin/$', 'django.contrib.auth.views.login', {'template_name': 'login.html','redirect_field_name' : '/' }, name='signin'),
    url(r'^signout/$','django.contrib.auth.views.logout', {'next_page' : '/signin'}, name='signout'),
    url(r'^mapdata/$', 'openstreetview.views.mapdata'),
    url(r'^addimage/$', 'openstreetview.views.add_image'),
    url(r'uploadimage/$', 'openstreetview.views.upload_image', name='uploadimage'),
    url(r'approveimages/$', 'openstreetview.views.load_unapproved_images', name='approveimages'),
    url(r'approve/$', 'openstreetview.views.approve_image'),
)
