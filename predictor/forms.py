from django import forms

class PredictionForm(forms.Form):
    pregnancies = forms.IntegerField(label='Pregnancies')
    glucose = forms.IntegerField(label='Glucose')
    blood_pressure = forms.IntegerField(label='Blood Pressure')
    skin_thickness = forms.IntegerField(label='Skin Thickness')
    insulin = forms.IntegerField(label='Insulin')
    bmi = forms.FloatField(label='BMI')
    diabetes_pedigree_function = forms.FloatField(label='Diabetes Pedigree Function')
    age = forms.IntegerField(label='Age')
