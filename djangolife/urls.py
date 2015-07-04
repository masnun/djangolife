from django.conf.urls import include, url
from django.contrib import admin

from video.views import home, login, register

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^admin/', include(admin.site.urls)),
]
