from django.urls import path

from . import views

    
urlpatterns = [path("login_user", views.login_user, name="login_user"),
               path("register", views.registerPage, name="register"),
               path("logout", views.logout_view, name="logout")]