"""Seminar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib.auth.views import LoginView, LogoutView
from app1 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^welcome/', views.welcome,name='welcome'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^search/', views.search,name='search'),

    url(r'^Autoproiz/', views.AutoProiz,name='unos_marka'),
    url(r'^Automod/', views.AutoMod,name='unos_model'),

    url(r'^login/', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    url(r'^password/', views.change_password, name='change_password'),

    url(r'^ispisi_modele/(\d+)', views.ispisi_modele, name='modeli'),
    url(r'^ispisi/', views.ispisi_proizvodjace,name='ispisi'),

    url(r'^update_proiz/(\d+)', views.update_proizvodjac, name='update_proiz'),
    url(r'^update_mod/(\d+)', views.update_model, name='update_mod'),

    url(r'^delete_pro/(\d+)', views.del_proizvodjac, name = 'delete_pro'),
    url(r'^delete_mod/(\d+)', views.del_model, name = 'delete_mod'),
    
    
]