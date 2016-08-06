"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from user_info import views as userviews
from house import views as houseviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', userviews.index),
    url(r'^signup/', userviews.user_signup),
    url(r'^signin/', userviews.user_signin),
    url(r'^user/(?P<userid>[0-9]+)$', userviews.user_detail),
    url(r'^house/roompost$', houseviews.roompost),
    url(r'^logout', userviews.user_signout),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
