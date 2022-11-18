from django.shortcuts import render

from .models import Patient,Doctor,Confirmation

from django.http import HttpResponseRedirect, HttpResponse

from .forms import Search, Add

from django.urls import reverse

# Create your views here.
def patient(request, patient_id):
    patient=Patient.objects.get(patient_id=patient_id)
    return render(request, "appointment/patient.html",{
        "patient":patient,
    }
    )

def doctor(request, doctor_id):
    doctor=Doctor.objects.get(doctor_id=doctor_id)
    return render(request, "appointment/doctor.html",{
        "doctor":doctor,
    }
    )

def confirmation(request, conf_number):
    confirmation=Confirmation.objects.get(conf_number=conf_number)
    return render(request, "appointment/confirmation.html",{
        "confirmation":confirmation,
    }
    )

def home(request):
    context={}
    form=Search(request.POST)
    context["form"] = form
    if request.POST:
        if form.is_valid():
            name=form.cleaned_data.get("name")
            context["name"]=Patient.objects.get(patient_name=name)        
    return render(request, "appointment/home.html", context,)

def add(request):
    context={}
    form=Add(request.POST)
    context["form"] = form
    if request.POST:
        if form.is_valid():
            name=form.cleaned_data.get("name")
            address=form.cleaned_data.get("address")
            age=form.cleaned_data.get("age")
            id=form.cleaned_data.get("id")
            if Patient.objects.filter(patient_id=id).exist():
                return HttpResponse("This id already belongs to another patient.")
            else:
                context["name"]=Patient.objects.create(patient_name=name)
                context["address"]=Patient.objects.create(patient_address=address)
                context["age"]=Patient.objects.create(patient_age=age)
                context["id"]=Patient.objects.create(patient_id=id)     
    return render(request, "appointment/add.html", context,)

def doctorlist(request):
    doctor=Doctor.objects.all()
    return render(request, "appointment/doctorlist.html",{
        "doctor":doctor}
        )


