# Generated by Django 5.0.7 on 2024-08-29 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_rename_medication_needs_healthprediction_under_medication'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthprediction',
            name='name',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
