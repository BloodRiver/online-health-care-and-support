from django.urls import path
from . import views

app_name = "ehr"

urlpatterns = [
    path('', views.index_view, name="index"),
    path('past-diagnosis', views.past_diagnosis_view, name="past_diagnosis"),
    path('surgery', views.surgery_view, name="surgery"),
    path('treatments', views.treatments_view, name="treatments")
    
]
