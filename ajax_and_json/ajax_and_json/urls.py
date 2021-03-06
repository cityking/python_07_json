"""ajax_and_json URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from ajax import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^add/$', views.add),
    url(r'^add2/((?:-|\d)+)/((?:-|\d)+)/$', views.add2),
    url(r'^ajax_list/$', views.ajax_list, name='list'),
    url(r'^ajax_dict/$', views.ajax_dict, name='dict'),
    url(r'^ajax_complex/$', views.ajax_complex, name='complex'),

    url(r'^more_poems/$', views.more_poems, name='more_poems'),
    url(r'^add_poems/$', views.add_poems, name='add_poems'),
]
