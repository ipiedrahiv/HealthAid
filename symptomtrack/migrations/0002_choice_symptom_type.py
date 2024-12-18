# Generated by Django 5.1.3 on 2024-12-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("symptomtrack", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="choice",
            name="symptom_type",
            field=models.CharField(
                choices=[
                    ("headache", "Head Ache"),
                    ("abdominal-pain", "Abdominal Pain"),
                    ("chest-pain", "Chest Pain"),
                    ("back-pain", "Back Pain"),
                    ("sore-throat", "Sore Throat"),
                ],
                default="headache",
                max_length=50,
                verbose_name="symptom type",
            ),
        ),
    ]