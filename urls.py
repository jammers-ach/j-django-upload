from django.conf.urls import patterns,include,url
from . import views

urlpatterns = patterns('',
    url(r'upload$', views.uploader_conf, name="default_upload"),
)
