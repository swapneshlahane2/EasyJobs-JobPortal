from django.urls import path
from adminapp import views
from adminapp.views import AddITJobView, UpdateITJobView, DeleteITJobView
from adminapp.views import AddMechJobView, UpdateMechJobView, DeleteMechJobView
from adminapp.views import AddCivilJobView, UpdateCivilJobView, DeleteCivilJobView
from adminapp.views import AddAddressView
from adminapp import views

urlpatterns = [
    path('home/', views.Home,name="home"),
    path('register/', views.admin_register),
    path('choose/', views.choose_view),
    path('loginregister/', views.loginregister_view),
    path('contact/', views.contact),
    path('feedback/', views.feedback),
    path('address/', AddAddressView.as_view()),
    #============= IT JOB URLS ==========================#
    path('additjob/', AddITJobView.as_view(), name='additjob'),
    path('readitjob/<int:id>/', views.readit_view, name='readitjob'),
    path('updateitjob/<int:pk>/', UpdateITJobView.as_view(), name='updateitjob'),
    path('deleteitjob/<int:pk>/', DeleteITJobView.as_view(), name='deleteitjob'),
    path('resumeit/<int:id>/', views.resume_it, name='resumeit'),
    #============= MECHANICAL JOB URLS ==========================#
    path('addmechjob/', AddMechJobView.as_view(), name='addmechjob'),
    path('readmechjob/<int:id>/', views.readmech_view, name='readmechjob'),
    path('updatemechjob/<int:pk>/', UpdateMechJobView.as_view(), name='updatemechjob'),
    path('deletemechjob/<int:pk>/', DeleteMechJobView.as_view(), name='deletemechjob'),
    path('resumemech/<int:id>/', views.resume_mech, name='resumemech'),
    #============= CIVIL JOB URLS ==========================#
    path('addciviljob/', AddCivilJobView.as_view(), name='addciviljob'),
    path('readciviljob/<int:id>/', views.readciviljob_view, name='readciviljob'),
    path('updateciviljob/<int:pk>/', UpdateCivilJobView.as_view(), name='updateciviljob'),
    path('deleteciviljob/<int:pk>/', DeleteCivilJobView.as_view(), name='deleteciviljob'),
    path('resumecivil/<int:id>/', views.resume_civil, name='resumecivil'),

]
