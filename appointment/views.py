from django.shortcuts import render, get_object_or_404

from .models import Patient,Doctor,Confirmation

from django.http import HttpResponseRedirect, HttpResponse

from django.urls import reverse

from .forms import Patients

# Create your views here.
def home(request):
    return render(request, 'appointment/home.html')

def patient(request,patientname):
    patient=Patient.objects.get(name=patientname)
    return render(request, "appointment/patient.html",{
        "patient":patient,
    }
    )

def doctor(request, doctorname):
    doctor=Doctor.objects.get(name=doctorname)
    patient=Doctor.patient_set.all()
    return render(request, "appointment/doctor.html",{
        "doctor":doctor,
        "patient":patient
    }
    )

def doctorlist(request):
    doctor=Doctor.objects.all()
    return render(request, 'appointment/doctorlist.html', {"doctor":doctor})

def confirmation(request, conf_number):
    confirmation=Confirmation.objects.get(conf_number=conf_number)
    return render(request, "appointment/confirmation.html",{
        "confirmation":confirmation,
    }
    )

def search_patient(request):
    if request.method == 'POST':
        form = Patients(request.POST)
        if form.is_valid():
            patientname=form.cleaned_data('name')
            patientaddress=form.cleaned_data('adress')
            patientage=form.cleaned_data('age')
            if Patient.objects.get(name=patientname).count()>0 and Patient.objects.get(address=patientaddress).cound()>0:
                return render(request, 'appointment/patient.html', {'error_message':"Information already existed"})
    else:
        form = Patients()
    return render(request, 'appointment/add.html', {'form':form})
    
    



