# Generated by Django 5.0.4 on 2024-04-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_plates_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plates',
            name='plate',
            field=models.TextField(unique=True),
        ),
    ]