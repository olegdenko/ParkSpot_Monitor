# Generated by Django 5.0.4 on 2024-04-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_balance_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessions',
            name='total_hours_spent',
            field=models.IntegerField(default=0),
        ),
    ]
