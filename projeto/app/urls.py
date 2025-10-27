# projeto/urls.py
from django.contrib import admin
from django.urls import path
from . import views  # vamos criar as views já já


urlpatterns = [
    path("", views.login_view, name="login"),          # login primeiro
    path("upload/", views.upload_file, name="upload"), # <- aqui troca para upload_file
    path("logout/", views.logout_view, name="logout"),
]