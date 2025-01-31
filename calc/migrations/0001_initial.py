# Generated by Django 5.0.7 on 2024-08-29 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HealthPrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('smoking', models.BooleanField(default=False)),
                ('alcohol', models.BooleanField(default=False)),
                ('diabetes', models.BooleanField(default=False)),
                ('hypertension', models.BooleanField(default=False)),
                ('other_conditions', models.TextField(blank=True)),
                ('medication_needs', models.TextField(blank=True)),
                ('assistance', models.TextField(blank=True)),
            ],
        ),
    ]
