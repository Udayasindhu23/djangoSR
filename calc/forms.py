from django import forms
from .models import HealthPrediction

class HealthPredictionForm(forms.ModelForm):
    class Meta:
        model = HealthPrediction
        fields = ['name','age', 'gender', 'smoking', 'alcohol', 'diabetes', 'hypertension', 'other_conditions', 'under_medication']
