from django.urls import path,include
from . import views

urlpatterns = [
    path("<int:patient_id>/", views.patient, name="patient"),
    path("<int:doctor_id>/", views.doctor, name="doctor"),
    path("<int:conf_number>/", views.confirmation, name="confirmation"),
    path("", views.home, name="home"),
    path("add/", views.add, name="add"),
    path("doctorlist/", views.doctorlist, name="dlist")
]