from django.shortcuts import render, redirect
from .forms import HealthPredictionForm

def predict_health(request):
    if request.method == 'POST':
        form = HealthPredictionForm(request.POST)
        if form.is_valid():
            prediction = form.save(commit=False)
            
            score = 0
            if prediction.age < 30:
                score += 1
            if prediction.gender == 'M':
                score += 1
            if not prediction.smoking:
                score += 1
            if not prediction.alcohol:
                score += 1
            if not prediction.diabetes:
                score += 1
            if not prediction.hypertension:
                score += 1
            if not prediction.other_conditions:
                score += 1
            if not prediction.under_medication:
                score += 1

            health_status = 'Healthy' if score >= 5 else 'Not Healthy'
            
            assistance = generate_assistance(prediction)

            prediction.assistance = assistance
            prediction.save()
            
            return render(request, 'result.html', {
                'health_status': health_status, 
                'assistance': assistance
            })
    else:
        form = HealthPredictionForm()
    
    return render(request, 'predict_health.html', {'form': form})

def generate_assistance(prediction):
    assistance = []
    
    if prediction.smoking:
        assistance.append("Consider quitting smoking to improve your health.")
    if prediction.alcohol:
        assistance.append("Limit your alcohol intake to reduce health risks.")
    if prediction.diabetes:
        assistance.append("Maintain a balanced diet and monitor your blood sugar levels regularly.")
    if prediction.hypertension:
        assistance.append("Monitor your blood pressure and reduce salt intake.")
    if prediction.age > 50:
        assistance.append("Regular check-ups are recommended for those over 50.")
    if prediction.other_conditions:
        assistance.append(f"Consult a specialist regarding your condition: {prediction.other_conditions}.")
    
    if not assistance:
        assistance.append("Keep up with a healthy lifestyle!")

    return " ".join(assistance)
