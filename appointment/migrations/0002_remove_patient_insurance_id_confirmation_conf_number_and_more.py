# Generated by Django 4.1.3 on 2022-11-16 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appointment", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="patient", name="insurance_id",),
        migrations.AddField(
            model_name="confirmation",
            name="conf_number",
            field=models.IntegerField(default=6),
        ),
        migrations.AddField(
            model_name="patient",
            name="patient_age",
            field=models.IntegerField(default=2),
        ),
        migrations.DeleteModel(name="Insurance",),
    ]
