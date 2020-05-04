"""minor_p URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from face_detector import view
from dappx import auth_views
from django.conf.urls import url,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'<movie_name>', view.temp, name='movie_name'),
    path('',view.index,name='index'),
    #path('signup.html', view.signup),


    path(r'reg/',auth_views.index,name='reg_page'),
    path(r'special/',auth_views.special,name='special'),
    path(r'dappx/',include('dappx.urls')),
    path(r'logout/$', auth_views.user_logout, name='logout'),

]
