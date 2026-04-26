from django.shortcuts import render


def index_view(request):
    return render(request, "ehr/index.html")


def past_diagnosis_view(request):
    return render(request, "ehr/past-diagnosis.html")


def surgery_view(request):
    return render(request, "ehr/surgery.html")


def treatments_view(request):
    return render(request, "ehr/treatments.html")
