from django.urls import path,include
from . import views
urlpatterns=[
    path("",views.login,name="home"),
    path("login",views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("travel/logout",views.logout,name="logout"),
]