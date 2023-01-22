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
            if Patient.objects.get(Patients.name).count()==0 and Patient.objects.get(Patients.address).count()==0:
                patientname=form.cleaned_data('name')
                patientadress=form.cleaned_data('adress')
                patientage=form.cleaned_data('age')
                return HttpResponseRedirect(reverse('appointment:patient', args=patientname))
            else:
                return HttpResponse('Your information already existed')
    else:
        form = Patients()
    return render(request, 'appointment/add.html', {'form':form})
    
    



