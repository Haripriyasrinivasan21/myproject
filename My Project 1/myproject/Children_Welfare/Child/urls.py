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
    path('lgo/',ad.LogoutView.as_view(template_name='html files/logout.html'),name="logo"),
    path('ch/',views.cgf,name="cg"),
    path('pro/',views.profile,name="profile"),
    path('don/',views.donate,name="donate"),
    path('oca/',views.occasion,name="occasion"),
 ]