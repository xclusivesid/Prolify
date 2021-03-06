from django.urls import path,re_path
from . import views

app_name='album'

urlpatterns = [

    path(r'', views.home, name='home'),

    re_path(r'^album/$', views.album, name='album'),

    re_path(r'^register/$',views.register, name='register'),

    re_path(r'^success/$',views.success, name='success'),

    re_path(r'^userprofile/edit/$',views.edituserprofile, name='edituserprofile'),

    re_path(r'^userprofile/$',views.userprofile, name='userprofile'),

    re_path(r'^userprofile/password/$',views.change_password, name='change_password'),
    
    #album/profile/2/detail
    re_path(r'^profile/(?P<pk>[0-9]+)/detail/$',views.contact_detail, name='contact_detail'),

    re_path(r'^contacts/$', views.contact, name='contact'),

    re_path(r'^results/$', views.search, name='search'),

    #/album/profile/add/
    re_path(r'^profile/add/$', views.contact_add, name='contact_add'),

    #/album/profile/2/update
    re_path(r'^profile/(?P<pk>[0-9]+)/edit/$', views.contact_edit, name='contact_edit'),

     #/album/profile/2/delete
    re_path(r'^profile/(?P<pk>[0-9]+)/delete/$', views. contact_delete, name='contact_delete'),

   
 
]