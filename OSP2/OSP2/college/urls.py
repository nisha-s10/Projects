"""OSP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('logout', views.logout,name='logout'),
    path('prof', views.prof,name='prof'),
    path('fac', views.fac,name='fac'),
    path('sub/<int:pk>', views.sub,name='sub'),
    path('delete_sub/<int:pk>', views.delete_sub,name='delete_sub'),
    path('header',views.header,name='header'),
    path('brreg/<int:pk>',views.brreg,name='brreg'),
    path('delete_branch/<int:pk>',views.delete_branch,name="delete_branch"),
    path('stdprof/<int:pk>',views.stdprof,name='stdprof'),
    path('delete_std/<int:pk>',views.delete_std,name='delete-std'),
    path('coreg',views.coreg,name='coreg'),
    path('assign_sub',views.assign_sub,name='assign_sub'),
    path('delete_course/<int:pk>',views.delete_course,name="delete_course"),
    path('facreg',views.facreg,name='facreg'),
    path('showfac',views.showfac,name='showfac'),
    path('update_status1/<int:pk>',views.update_status1,name="update_status1"),
    path('showstd',views.showstd,name='showstd'),
    path('update_status/<int:pk>',views.update_status,name="update_status"),
    path('stdreg',views.stdreg,name='stdreg'), 
    path('subreg/<int:pk>',views.subreg,name='subreg'),
    path('delete_subject/<int:pk>',views.delete_subject,name="delete_subject"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)