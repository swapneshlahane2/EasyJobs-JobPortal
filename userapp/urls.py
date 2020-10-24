from django.urls import path
from userapp import views
from userapp.views import UserFormView


urlpatterns = [
    path('userregister/', UserFormView.as_view()),
    path('userlogin/', views.user_login),
    path('userlogout/', views.logout_view),
    path('user_login/', views.user_login_required),
    path('userloginregister/', views.user_login_register_view),
    #============= IT JOB URLS =======================#
    path('readit/', views.readuserit_view),
    path('it_apply/<int:id>/', views.it_apply),
    #============= MECHANICAL JOB URLS =======================#
    path('readmech/', views.readusermech_view),
    path('mech_apply/<int:id>/', views.mech_apply),
    #============= CIVIL JOB URLS =======================#
    path('readcivil/', views.readusercivil_view),
    path('civil_apply/<int:id>/', views.civil_apply),

]
