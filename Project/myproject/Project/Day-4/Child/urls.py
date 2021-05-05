from django.urls import path
from Child import views
from django.contrib.auth import views as ad


urlpatterns=[
    path('',views.home,name="hm"),
    path('abt/',views.about,name="at"),
    path('cnt/',views.contact,name="ct"),
    path('fed/',views.feedback,name="fb"),
    path('join/',views.joinus,name="ju"),
    path('lg/',ad.LoginView.as_view(template_name='html/login.html'),name="log"),
    path('lgo/',ad.LogoutView.as_view(template_name='html/logout.html'),name="logo"),
    path('ch/',views.cgf,name="cg"),
    path('pro/',views.profile,name="profile"),
    path('don/',views.donate,name="donate"),
    path('oca/',views.occasion,name="occasion"),
    path('rg/',views.regi,name="rg"),
    path('comp/',views.complaint,name="cp"),
    path('nu/',views.Newone,name="nu"),
    path('th/',views.thankyou,name="th"),
    path('cr/',views.crud,name="cd"),
    path('show/',views.showinfo,name="show"),
    path('ui/<str:uname>/',views.userinfo,name="uif"),
    path('delt/<str:st>/',views.deletedata,name="infodelete"),
    path('e/<int:si>/',views.userupdate,name="ue"),
    path('rol/',views.roles,name="rol"),
    path('rst/',ad.PasswordResetView.as_view(template_name='html/resetpassword.html'),name="reset_password"),
    path('rst_done/',ad.PasswordResetDoneView.as_view(template_name='html/resetdone.html'),name="password_reset_done"),
    path('rst_cf/<uidb64>/<token>/',ad.PasswordResetConfirmView.as_view(template_name='html/resetconfirm.html'),name="password_reset_confirm"),
    path('rst_cmplt/',ad.PasswordResetCompleteView.as_view(template_name='html/resetcomplete.html'),name="password_reset_complete"),
    path('dd/',views.donatedetails,name="dd"),
    path('updf/',views.updpf,name="upf"),
 ]