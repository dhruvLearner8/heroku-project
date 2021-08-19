from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name='home'),
    path("explore",views.explore,name="explore"),
    path("index",views.index, name="index"),
    path("register",views.register, name="register"),
    path("login",views.login,name="login"),
    path('logout',views.logout,name='logout'),
    path('forget_pass',views.forget_pass,name='forget_pass'),
    path('OTP_check',views.OTP_check,name='OTP_check'),
    path('new_pass',views.new_pass,name='new_pass'),
    path('add',views.add,name='add'),
    path('Delete_Product/<int:id>',views.Delete_Product,name='Delete_Product'),
    path('history',views.history,name='history'),
    path('new_pass',views.new_pass,name='new_pass'),

]