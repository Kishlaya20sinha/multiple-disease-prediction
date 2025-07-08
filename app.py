import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
try:
    diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
    parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.warning("You may need to retrain your models with your current scikit-learn version (1.5.0)")
    st.stop()

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', '0')

    with col2:
        Glucose = st.text_input('Glucose Level', '0')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value', '0')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value', '0')

    with col2:
        Insulin = st.text_input('Insulin Level', '0')

    with col3:
        BMI = st.text_input('BMI value', '0')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', '0')

    with col2:
        Age = st.text_input('Age of the Person', '0')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        try:
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                          BMI, DiabetesPedigreeFunction, Age]
            
            # Check if any input is empty
            if '' in user_input:
                st.error("Please fill in all fields before prediction.")
            else:
                user_input = [float(x) for x in user_input]
                
                diab_prediction = diabetes_model.predict([user_input])

                if diab_prediction[0] == 1:
                    diab_diagnosis = 'The person is diabetic'
                else:
                    diab_diagnosis = 'The person is not diabetic'
                
                st.success(diab_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values in all fields.")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age', '0')

    with col2:
        sex = st.text_input('Sex (1 = male, 0 = female)', '0')

    with col3:
        cp = st.text_input('Chest Pain types (0-3)', '0')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure', '0')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', '0')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true, 0 = false)', '0')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0-2)', '0')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', '0')

    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = yes, 0 = no)', '0')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', '0')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (0-2)', '0')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy (0-4)', '0')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', '0')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        try:
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            
            # Check if any input is empty
            if '' in user_input:
                st.error("Please fill in all fields before prediction.")
            else:
                user_input = [float(x) for x in user_input]
                
                heart_prediction = heart_disease_model.predict([user_input])

                if heart_prediction[0] == 1:
                    heart_diagnosis = 'The person is having heart disease'
                else:
                    heart_diagnosis = 'The person does not have any heart disease'
                
                st.success(heart_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values in all fields.")

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)', '0')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', '0')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', '0')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)', '0')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', '0')

    with col1:
        RAP = st.text_input('MDVP:RAP', '0')

    with col2:
        PPQ = st.text_input('MDVP:PPQ', '0')

    with col3:
        DDP = st.text_input('Jitter:DDP', '0')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer', '0')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', '0')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3', '0')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5', '0')

    with col3:
        APQ = st.text_input('MDVP:APQ', '0')

    with col4:
        DDA = st.text_input('Shimmer:DDA', '0')

    with col5:
        NHR = st.text_input('NHR', '0')

    with col1:
        HNR = st.text_input('HNR', '0')

    with col2:
        RPDE = st.text_input('RPDE', '0')

    with col3:
        DFA = st.text_input('DFA', '0')

    with col4:
        spread1 = st.text_input('spread1', '0')

    with col5:
        spread2 = st.text_input('spread2', '0')

    with col1:
        D2 = st.text_input('D2', '0')

    with col2:
        PPE = st.text_input('PPE', '0')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        try:
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                          RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                          APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            
            # Check if any input is empty
            if '' in user_input:
                st.error("Please fill in all fields before prediction.")
            else:
                user_input = [float(x) for x in user_input]
                
                parkinsons_prediction = parkinsons_model.predict([user_input])

                if parkinsons_prediction[0] == 1:
                    parkinsons_diagnosis = "The person has Parkinson's disease"
                else:
                    parkinsons_diagnosis = "The person does not have Parkinson's disease"
                
                st.success(parkinsons_diagnosis)
        except ValueError:
            st.error("Please enter valid numerical values in all fields.")