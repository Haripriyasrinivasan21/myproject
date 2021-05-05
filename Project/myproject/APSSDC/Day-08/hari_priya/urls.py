from django.urls import path
from hari_priya import views
urlpatterns = [
    path('',views.home),
    path('demo/',views.chk),
    path('firsthtml/',views.homepage),
    path('login/',views.lgn),
    path('rg/',views.reg),
]