# Generated by Django 5.0.4 on 2024-04-08 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_delete_parkingrate_delete_registerednumberplate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlacklistedVehicle',
        ),
    ]
