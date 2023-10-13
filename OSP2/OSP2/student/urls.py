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
    path('checkass',views.checkass,name='checkass'),
    path('showatt',views.showatt,name='showatt'),
    path('subj',views.subj,name='subj'),
    path('prof',views.prof,name='prof'),
    path('stdsec',views.stdsec,name='stdsec'),
    path('notes',views.notes,name='notes'),
    path('delete_note/<int:pk>',views.delete_note,name="delete_note"),
    path('notes_detail/<int:pk>',views.notes_detail,name="notes_detail"),
    path('homework',views.homework,name='homework'),
    path('update_homework/<int:pk>',views.update_homework,name='update-homework'),
    path('delete_homework/<int:pk>',views.delete_homework,name='delete-homework'),
    path('youtube',views.youtube,name='youtube'),
    path('todo',views.todo,name='todo'),
    path('update_todo/<int:pk>',views.update_todo,name='update-todo'),
    path('delete_todo/<int:pk>',views.delete_todo,name='delete-todo'),
    path('subass/<int:pk>',views.subass,name='subass'),
    path('showass/<int:pk>',views.showass,name='showass'),
    path('books',views.books,name='books'),
    path('dictionary',views.dictionary,name='dictionary'),
    path('wiki',views.wiki,name='wiki'),
    path('conversion',views.conversion,name='conversion'),
    path('profile',views.profile,name='profile')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)