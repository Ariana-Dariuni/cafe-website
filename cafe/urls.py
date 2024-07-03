from django.urls import path # type:ignore
from . import views

urlpatterns = [
    # path('', views.home, name = "home"),
    path('login/', views.login_view, name = "login"),
    path('logout/', views.logout_view, name = "logout"),
    path('register/', views.Register, name = "register"),
    path('management/', views.Management, name = "management"),

    path('', views.home, name = "home"),



]