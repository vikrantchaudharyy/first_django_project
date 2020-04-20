"""first_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf.urls import include
from first_app import views
from basic_app import views as b_view


urlpatterns = [
    path('first_app/', include('first_app.urls')),
    path('basic_app/', include('basic_app.urls')),
    path('template_text/', views.template_text_render),
    path('template_image/', views.template_image_injection),
    path('strong/', views.strong),
    path('hello/',views.hello,name='hello'),
    path('table/', views.table),
    path('admin/', admin.site.urls),
    path('',b_view.index,name='index'),
    path('special/',b_view.special,name='special'),
    path('logout/', b_view.user_logout, name='logout'),
]
