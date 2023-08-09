from django.contrib import admin
from django.urls import path
from.views import home,register,login_user,logout_user,detail,new,form

urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login_user',login_user,name='login_user'),
    path('logout_user',logout_user,name='logout_user'),
    path('detail',detail,name='detail',),
    path('new/',new,name='new'),
    path('form/',form,name='form'),
]