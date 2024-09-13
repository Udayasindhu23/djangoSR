from django.db import models  # Corrected import statement

class HealthPrediction(models.Model):
    name = models.CharField(max_length=100,default=0)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    smoking = models.BooleanField(default=False)
    alcohol = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    hypertension = models.BooleanField(default=False)
    other_conditions = models.TextField(blank=True)
    under_medication = models.TextField(blank=True)
    assistance = models.TextField(blank=True) 
    def __str__(self):
        return f"Health Prediction for Age {self.age}, Gender {self.gender}"

