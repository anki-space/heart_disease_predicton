from django.shortcuts import render, redirect
from .forms import RegisterForm,Prediction_form
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile,Profile_result

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data.get('phone_number')
            dob = form.cleaned_data.get('dob')
            Hospital_name=form.cleaned_data.get('Hospital_name')
            #saving phno and dob to the userprofile model
            profile=UserProfile(user=user,phone_number=phone_number,dob=dob,Hospital_name=Hospital_name)
            profile.save()

            login(request, user)
            return redirect('successfully_registered')
    
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

def successfully_registered(request):
    return render(request, 'users/successfully_registered.html')


def login_view(request):  #dont name "login" bcoz django already have build-in log in function"
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('successfully_logged_in')  # Redirect successful login
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required  # Ensure the user is logged in before accessing this view
def successfully_logged_in(request):
    return render(request,'users/successfully_logged_in.html')
    # return redirect('successfully_logged_in')  # Redirect successful login
    # return redirect('prediction_form')

@login_required
def signout_profile(request):
    logout(request)
    return redirect ('home')
@login_required
def result(request):
    return render(request, 'users/result.html')
@login_required
def prediction(request):
    return redirect('prediction_form')
@login_required
def view_history(request):
    user = request.user
    profile_results = Profile_result.objects.filter(user=user)
    return render(request, 'users/view_history.html', {'profile_results': profile_results})



import numpy as np
import pandas as pd
import joblib
model=joblib.load('./hdp_model_pipeline.pkl')
label_encoder=joblib.load('./label_encoder.pkl')

@login_required    
def prediction_form(request):
    if request.method == 'POST':
        form = Prediction_form(data=request.POST)
        if form.is_valid():
            patient_data={
            'Height_cm':form.cleaned_data['height'],
            'Weight_kg':form.cleaned_data['weight'],
            'Temperature_C':form.cleaned_data['temperature'],
            'Heart_Rate':form.cleaned_data['heart_rate'],
            'Symptoms':form.cleaned_data['symptoms'],
            'Existing_Conditions':form.cleaned_data['existing_conditions'],
            'Laboratory_Test_Results':form.cleaned_data['laboratory_results'],
            'Cholesterol_mg_dL':form.cleaned_data['cholesterol'],
            'Blood_Sugar_mg_dL':form.cleaned_data['blood_sugar'],
            'Family_History_Heart_Disease':form.cleaned_data['family_history'],
            'Smoking_Status':form.cleaned_data['smoking_status'],
            'Blood_Pressure_Systolic':form.cleaned_data['systolic'],
            'Blood_Pressure_Diastolic':form.cleaned_data['diastolic']

            }
            categorical_columns = [
                "Symptoms",
                "Existing_Conditions",
                "Laboratory_Test_Results",
                "Smoking_Status",
                "Family_History_Heart_Disease"
            ]
            features_after_onehotencoding =['Height_cm', 'Weight_kg', 'Temperature_C', 'Heart_Rate',
            'Cholesterol_mg_dL', 'Blood_Sugar_mg_dL', 'Blood_Pressure_Systolic',
            'Blood_Pressure_Diastolic', 'Symptoms_dizziness', 'Symptoms_fatigue',
            'Symptoms_nausea', 'Symptoms_palpitations','Symptoms_shortness of breath', 'Existing_Conditions_Diabetes',
            'Existing_Conditions_High Cholesterol',
            'Existing_Conditions_Hypertension',
            'Laboratory_Test_Results_High Cholesterol',
            'Laboratory_Test_Results_Low Iron', 'Laboratory_Test_Results_Normal',
            'Family_History_Heart_Disease_Yes', 'Smoking_Status_Former',
            'Smoking_Status_Never']

            input_df = pd.DataFrame([patient_data])

            input_df = pd.get_dummies(input_df, columns=categorical_columns)

            for col in features_after_onehotencoding:
                if col not in input_df:
                    input_df[col] = 0

            input_df = input_df[features_after_onehotencoding]  


            prediction = model.predict(input_df)
            prediction = label_encoder.inverse_transform(prediction)

            if prediction[0] is not None:
                profile_save = Profile_result(
                    user=request.user,
                    height=form.cleaned_data['height'],
                    weight=form.cleaned_data['weight'], 
                    temperature=form.cleaned_data['temperature'],
                    heart_rate=form.cleaned_data['heart_rate'],
                    cholesterol=form.cleaned_data['cholesterol'],
                    blood_sugar=form.cleaned_data['blood_sugar'],
                    systolic=form.cleaned_data['systolic'],
                    diastolic=form.cleaned_data['diastolic'],
                    symptoms=form.cleaned_data['symptoms'],
                    existing_conditions=form.cleaned_data['existing_conditions'],
                    family_history=form.cleaned_data['family_history'],
                    smoking_status=form.cleaned_data['smoking_status'],
                    laboratory_results=form.cleaned_data['laboratory_results'],
                    prediction=prediction[0]
                )
            

                profile_save.save()
            return render(request, 'users/result.html', {
                'prediction': prediction, 
                'patient_data': patient_data
            })
        
        
    else:
        form = Prediction_form()
    return render(request, 'users/prediction_form.html', {'form': form})