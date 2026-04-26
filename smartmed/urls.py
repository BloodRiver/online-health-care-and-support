from django.urls import path
from . import views

app_name = "smartmed"

urlpatterns = [
    path('', views.app_view, name="app")
]
