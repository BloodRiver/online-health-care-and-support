from django.db import models
from django.contrib.auth.models import User

class Specialty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Symptom(models.Model):
    CATEGORY_CHOICES = [
        ('Respiratory', 'Respiratory'),
        ('Digestive', 'Digestive'),
        ('Neurological', 'Neurological'),
        ('General', 'General'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    # The rule-based mapping: which specialty handles this symptom?
    mapped_specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category} - {self.name}"

class PrescreeningReport(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    symptoms_summary = models.TextField() # Stores details like "Cough (Intensity 6)"
    recommended_specialty = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.patient.username} on {self.created_at.date()}"