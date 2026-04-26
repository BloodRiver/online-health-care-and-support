from django.urls import path
from . import views

app_name = "bloodconnect"

urlpatterns = [
    path('', views.index_view, name="index"),
    path('login', views.LoginView.as_view(), name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.RegisterView.as_view(), name="register"),
    path('demo-user', views.DemoUserDashboardView.as_view(), name="demo_user"),
    path('demo-admin', views.DemoAdminDashboardView.as_view(), name="demo_admin"),
    path('find-donor', views.FindDonorView.as_view(), name="find_donor")
]