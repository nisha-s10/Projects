from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('empdetails/',views.empdetails, name='empdetails'),
    path('regemp/', views.regemp, name='regemp'),
    path('logout', views.logout, name='logout')
]