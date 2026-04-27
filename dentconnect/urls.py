from django.urls import path
from . import views

app_name = "dentconnect"

urlpatterns = [
    path('', views.index_view, name="index"),
    path('patient/login', views.patient_login_view, name="patient_login"),
    path('doctor/login', views.doctor_login_view, name="doctor_login"),
    path('staff/login', views.staff_login_view, name="staff_login"),
    path('admin/login', views.admin_login_view, name="admin_login"),
    path('register', views.register_view, name="register"),
    path('admin/dashboard', views.admin_dashboard_view, name="admin_dashboard"),
    path('admin/manage-users', views.admin_manage_users_view, name="admin_manage_users"),
    path('admin/appointments', views.admin_appointments_view, name="admin_appointments"),
    path('admin/add-user', views.admin_add_user_view, name="admin_add_user"),
    path("profile", views.profile_view, name="profile"),
    path("settings", views.settings_view, name="settings"),
    path("patient/booking", views.booking_view, name="booking"),
    path("patient/history", views.patient_history_view, name="patient_history")
]
