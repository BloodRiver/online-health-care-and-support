from django.urls import path
from . import views

app_name = 'medguide'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('selection', views.selection, name='selection'),
    path('details', views.details, name='details'),
    path('recommendation', views.recommendation, name='recommendation'),
    path('preview', views.preview, name='preview'),
    path('moderator', views.moderator_dashboard, name='moderator'),
]