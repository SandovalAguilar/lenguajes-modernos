from django.urls import path
from principal_app import views

urlpatterns = [
 path("", views.home, name="home"),
]