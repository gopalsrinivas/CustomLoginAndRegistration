from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/',register_user,name="register"),
    path('login/', login_view, name="login"),
    path('home/', home, name="home"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
