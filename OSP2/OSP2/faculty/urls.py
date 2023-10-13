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
    path('header',views.header,name='header'),
    path('logout', views.logout,name='logout'),
    
    path('prof',views.prof,name='prof'),
    path('sub',views.sub,name='sub'),
    path('ass/<int:pk>',views.ass,name='ass'),
    path('checkass/<int:pk>',views.checkass,name='checkass'),
    path('update_ass/<int:pk>',views.update_ass,name='update-ass'),
    # path('editatt',views.editatt,name='editatt'),
    path('showstds',views.showstds,name='showstds'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)