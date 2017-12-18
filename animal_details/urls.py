from django.conf.urls import url
from . import views

app_name='animal_details'
urlpatterns = [

    url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^$', views.index,name='index'),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    url(r'animal/add/$',views.AnimalCreate.as_view(),name='animal-add'),

    url(r'animal/(?P<pk>[0-9]+)/$', views.AnimalUpdate.as_view(), name='animal-update'),

    url(r'animal/(?P<pk>[0-9]+)/delete/$', views.AnimalDelete.as_view(), name='animal-delete'),

    url(r'medicines/$',views.med_detail,name='med-detail'),
    url(r'medicines/add/$',views.MedicineCreate.as_view(),name='medicine-add'),
    url(r'medicines/(?P<pk>[0-9]+)/$',views.MedicineUpdate.as_view(),name='medicine-update'),

   
    #/Staff/
    url(r'Staff/$',views.StaffDetail.as_view(),name='Staff-detail'),
    #/Staff/add/
    url(r'Staff/add/$', views.StaffCreate.as_view(),name='Staff-add'),
    #/Staff/pk/
    url(r'Staff/(?P<pk>[0-9]+)/$', views.StaffUpdate.as_view(), name='Staff-update'),
     url(r'Staff/(?P<pk>[0-9]+)/delete/$', views.StaffDelete.as_view(), name='Staff-delete'),

    #/Tourist/
    url(r'Tourist/$',views.TouristDetail.as_view(),name='Tourist-detail'),
    #/Tourist/add/
    url(r'Tourist/add/$', views.TouristCreate.as_view(),name='Tourist-add'),
    #/Tourist/pk/
    url(r'Tourist/(?P<pk>[0-9]+)/$', views.TouristUpdate.as_view(), name='Tourist-update'),


    url(r'account/$',views.AccountDetail.as_view(),name='acc-detail'),
    url(r'account/add/$', views.add_account, name='account-add'),
    url(r'account/(?P<pk>[0-9]+)/$',views.AccountUpdate.as_view(),name='account-update'),
    url(r'account/(?P<pk>[0-9]+)/delete/$', views.AccountDelete.as_view(), name='account-delete'),

    url(r'Organisation_grants/$',views.GrantsDetail.as_view(),name='grant-detail'),
    url(r'Organisation_grants/add/$',views.GrantsCreate.as_view(),name='Org-grant-add'),
    url(r'Organisation_grants/(?P<pk>[0-9]+)/$',views.GrantsUpdate.as_view(),name='grant-Update'),
    url(r'Organisation_grants/(?P<pk>[0-9]+)/delete/$', views.GrantsDelete.as_view(), name='grant-delete'),


     ]