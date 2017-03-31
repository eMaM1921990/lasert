"""lasert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from lasertApp import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^partners/', views.partner, name='partner'),
    url(r'^clients/', views.clients, name='client'),
    url(r'^solutions/', views.solution, name='solution'),
    url(r'^contactus/$', views.contact_us, name='contactUs'),
    url(r'^careers/$', views.careers, name='careers'),
    url(r'^about/$', views.about, name='about'),
    url(r'^subscribe/$', views.addToSubscriber, name='subscribe'),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', admin.site.urls),
    url(r'^froala_editor/', include('froala_editor.urls')),

    # serve media
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    # url(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
    # Localizations #
    url(r'^i18n/', include('django.conf.urls.i18n')),

]
