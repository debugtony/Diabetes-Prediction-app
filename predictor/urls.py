
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # other URL patterns for the predictor app
    path('predict/', views.predict_diabetes, name='predict_diabetes'),
]
