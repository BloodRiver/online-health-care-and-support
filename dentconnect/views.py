from django.shortcuts import render


def index_view(request):
    return render(request, "dentconnect/index.html")


def patient_login_view(request):
    return render(request, "dentconnect/patient_login.html")


def doctor_login_view(request):
    return render(request, "dentconnect/doctor_login.html")


def staff_login_view(request):
    return render(request, "dentconnect/staff_login.html")


def admin_login_view(request):
    return render(request, "dentconnect/admin_login.html")


def register_view(request):
    return render(request, "dentconnect/register.html")


def admin_dashboard_view(request):
    return render(request, "dentconnect/admin/dashboard.html")


def admin_manage_users_view(request):
    return render(request, "dentconnect/admin/manage_users.html")


def admin_appointments_view(request):
    return render(request, "dentconnect/admin/appointments.html")


def admin_add_user_view(request):
    return render(request, "dentconnect/admin/add_user.html")


def profile_view(request):
    return render(request, "dentconnect/profile.html")


def settings_view(request):
    return render(request, "dentconnect/settings.html")


def booking_view(request):
    return render(request, "dentconnect/patient/booking.html")


def patient_history_view(request):
    return render(request, "dentconnect/patient/history.html")
