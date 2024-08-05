from django.shortcuts import render
from .forms import PredictionForm
import pickle

# Load the trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def index(request):
    form = PredictionForm()
    return render(request, 'predictor/home.html', {'form': form})

def predict_diabetes(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            input_data = [
                data['pregnancies'],
                data['glucose'],
                data['blood_pressure'],
                data['skin_thickness'],
                data['insulin'],
                data['bmi'],
                data['diabetes_pedigree_function'],
                data['age']
            ]
            prediction = model.predict([input_data])
            result = 'Positive' if prediction[0] == 1 else 'Negative'
            return render(request, 'predictor/result.html', {'result': result})
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = PredictionForm()
    return render(request, 'predictor/home.html', {'form': form})
