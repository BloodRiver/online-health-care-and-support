from django.shortcuts import render, redirect
from django.views.generic import View

def index_view(request):
    return render(request, "bloodconnect/layouts/index.html")


class FindDonorView(View):
    template_name = "bloodconnect/layouts/find_donor.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
    
class LoginView(View):
    template_name = "bloodconnect/layouts/login.html"
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("bloodconnect:index")
        return render(request, self.template_name)
    
    
def logout_view(request):
    return redirect("bloodconnect:login")
    
    
class RegisterView(View):
    template_name = "bloodconnect/layouts/register.html"
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("bloodconnect:index")
        
        return render(request, self.template_name)
    
    
class DemoUserDashboardView(View):
    template_name = "bloodconnect/layouts/demo_user_dashboard.html"
    mockCurrentUser = {
        'name': 'Alex Thompson',
        'email': 'alex.thompson@email.com',
        'bloodGroup': 'A+',
        'phone': '+880 01xxx-xxxxxx',
        'location': 'Dhaka, Bangladesh',
        'userType': 'Donor',
        }
    
    def get(self, request):
        return render(request, self.template_name, context={'mockCurrentUser': self.mockCurrentUser})
    
    
class DemoAdminDashboardView(View):
    template_name = "bloodconnect/layouts/admin_dashboard.html"
    stats = {
        'months': ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar'],
        'donations': [120, 145, 165, 180, 170, 195],
        'blood_groups': ['A+', 'O-', 'O+', 'AB-', 'AB+', 'B-', 'B+', 'A-'],
        'blood_group_counts': [22, 7, 26, 3, 9, 6, 20, 8],
        'blood_group_labels': ['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-'],
        'blood_group_stat_counts': [320, 85, 280, 95, 245, 72, 110, 40],
        'skipNavbar': True
    }
    
    def get(self, request):
        return render(request, self.template_name, context=self.stats)
