# Generated by Django 4.1.3 on 2022-11-15 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("doctor_name", models.CharField(max_length=64)),
                ("doctor_field", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Insurance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("insurance_name", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("patient_name", models.CharField(max_length=64)),
                ("patient_address", models.CharField(max_length=64)),
                (
                    "insurance_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="insuranceid",
                        to="appointment.insurance",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Confirmation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "doctor_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctor",
                        to="appointment.doctor",
                    ),
                ),
                (
                    "patient_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient",
                        to="appointment.patient",
                    ),
                ),
            ],
        ),
    ]
