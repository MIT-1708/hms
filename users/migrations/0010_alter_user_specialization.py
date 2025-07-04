# Generated by Django 5.2 on 2025-06-29 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_remove_user_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='specialization',
            field=models.CharField(blank=True, choices=[('GENERAL_MEDICINE', 'General Medicine & Internal Medicine'), ('CARDIOLOGY', 'Cardiology & Cardiovascular Surgery'), ('ORTHOPEDIC', 'Orthopedic & Bone Surgery'), ('NEUROLOGY', 'Neurology & Neurosurgery'), ('EMERGENCY', 'Emergency Medicine & Critical Care'), ('ONCOLOGY', 'Oncology & Cancer Treatment')], max_length=20),
        ),
    ]
