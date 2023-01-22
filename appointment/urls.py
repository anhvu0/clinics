from django.urls import path,include
from . import views

urlpatterns = [
    path("<str:patientname>/", views.patient, name="patient"),
    path("<str:doctorname>/", views.doctor, name="doctor"),
    path("<int:conf_number>/", views.confirmation, name="confirmation"),
    path("", views.home, name="home"),
    path("add/", views.search_patient, name="add"),
    path("doctorlist/", views.doctorlist, name="dlist")
]