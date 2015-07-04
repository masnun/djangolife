from django.conf.urls import include, url
from django.contrib import admin

from video.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
