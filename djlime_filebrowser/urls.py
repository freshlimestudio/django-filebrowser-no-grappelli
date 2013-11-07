from django.conf.urls import *

urlpatterns = patterns(
    '',
    url(r'^browse/$', 'djlime_filebrowser.views.browse', name="fb_browse"),
    url(r'^mkdir/', 'djlime_filebrowser.views.mkdir', name="fb_mkdir"),
    url(r'^upload/', 'djlime_filebrowser.views.upload', name="fb_upload"),
    url(r'^rename/$', 'djlime_filebrowser.views.rename', name="fb_rename"),
    url(r'^delete/$', 'djlime_filebrowser.views.delete', name="fb_delete"),
    url(r'^versions/$', 'djlime_filebrowser.views.versions', name="fb_versions"),
    url(r'^check_file/$', 'djlime_filebrowser.views._check_file', name="fb_check"),
    url(r'^upload_file/$', 'djlime_filebrowser.views._upload_file', name="fb_do_upload"),
)
