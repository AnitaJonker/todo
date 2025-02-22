from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hero", views.hero, name="hero"),
    path("main", views.main, name="main"),
]