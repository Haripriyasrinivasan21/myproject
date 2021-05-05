from django.urls import path
from NoteApp import views #from . import views
from django.contrib.auth import views as ad

urlpatterns = [
    path('',views.home,name="hm"),
    path('pro/',views.profile,name="profile"),
    path('abt/',views.about,name="at"),
    path('cnt/',views.contact,name="ct"),
    path('lg/',ad.LoginView.as_view(template_name='html files/login.html'),name="log"),
    path('rg/',views.regi,name="rg"),
    path('ds/',views.dashboard,name="dsh"),
    path('lgo/',ad.LogoutView.as_view(template_name='html files/logout.html'),name="logo"),
    path('comp/',views.complaint,name="cp"),
    path('updf/',views.updpf,name="upf"),
    path('ch/',views.cgf,name="cg"),
    path('rst/',ad.PasswordResetView.as_view(template_name='html files/resetpassword.html'),name="reset_password"),
    path('rst_done/',ad.PasswordResetDoneView.as_view(template_name='html files/resetpassworddone.html'),name="password_reset_done"),
    path('rst_cf/<uidb64>/<token>/',ad.PasswordResetConfirmView.as_view(template_name='html files/reset_password_confirm.html'),name="password_reset_confirm"),
    path('rst_cmplt/',ad.PasswordResetCompleteView.as_view(template_name='html files/reset_password_complete.html'),name="password_reset_complete"),

]