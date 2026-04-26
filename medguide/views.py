from django.shortcuts import render, redirect
from .models import Symptom, Specialty, PrescreeningReport

# 1. Landing Page
def landing(request):
    return render(request, 'medguide/landing.html')

# 2. Symptom Selection
def selection(request):
    symptoms = Symptom.objects.all().order_by('category')
    if request.method == 'POST':
        # Get selected symptom IDs from the form
        selected_ids = request.POST.getlist('symptoms')
        request.session['selected_symptom_ids'] = selected_ids
        return redirect('details')
    return render(request, 'medguide/selection.html', {'symptoms': symptoms})

# 3. Symptom Details
def details(request):
    symptom_ids = request.session.get('selected_symptom_ids', [])
    selected_symptoms = Symptom.objects.filter(id__in=symptom_ids)
    
    if request.method == 'POST':
        # Store intensity and duration in session
        # Logic for processing form data goes here
        return redirect('recommendation')
    return render(request, 'medguide/details.html', {'symptoms': selected_symptoms})

# 4. Specialist Recommendation (The Rule Engine)
def recommendation(request):
    symptom_ids = request.session.get('selected_symptom_ids', [])
    # Rule: Find the most frequent specialty associated with selected symptoms
    # Simple logic: Pick the specialty of the first symptom selected
    first_symptom = Symptom.objects.get(id=symptom_ids[0])
    rec = first_symptom.mapped_specialty
    
    request.session['final_rec'] = rec.name
    return render(request, 'medguide/recommendation.html', {'specialty': rec})

# 5. Report Preview & Save
def preview(request):
    context = {
        'specialty': request.session.get('final_rec'),
        'date': "April 25, 2026"
    }
    return render(request, 'medguide/preview.html', context)

# 6. Moderator Dashboard
def moderator_dashboard(request):
    all_mappings = Symptom.objects.select_related('mapped_specialty').all()
    specialties = Specialty.objects.all()
    return render(request, 'medguide/moderator.html', {
        'mappings': all_mappings,
        'specialties': specialties
    })