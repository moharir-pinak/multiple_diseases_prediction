import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🩺")

import streamlit as st
import base64
import os

# Function to read the SVG file and convert it to base64
def svg_to_base64(svg_file_path):
    if not os.path.exists(svg_file_path):
        raise FileNotFoundError(f"The file {svg_file_path} does not exist.")
    
    try:
        with open(svg_file_path, "r") as svg_file:
            svg_content = svg_file.read()
    except Exception as e:
        raise RuntimeError(f"Error reading SVG file: {e}")

    # Encode the SVG content to base64
    b64_svg = base64.b64encode(svg_content.encode()).decode()
    return f"data:image/svg+xml;base64,{b64_svg}"

# Set up the page configuration
# st.set_page_config(page_title="Health Assistant", layout="wide")

# Get the base64 SVG
svg_icon_path = r"./stethoscope-doctor.svg"
try:
    svg_icon = svg_to_base64(svg_icon_path)
except Exception as e:
    st.error(str(e))
    svg_icon = None  # Set to None if there's an error

# Embed the SVG icon in the title if it was successfully loaded
if svg_icon:
    st.markdown(f'<img src="{svg_icon}" style="width:50px; height:50px;">', unsafe_allow_html=True)

# Rest of your app code here
st.title("Welcome to Health Assistant")
st.write("Your one-stop solution for disease prediction.")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

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
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)


#code2

# import os
# import pickle
# import streamlit as st
# from streamlit_option_menu import option_menu

# # Set page configuration
# st.set_page_config(page_title="Health Assistant",
#                    layout="wide",
#                    page_icon="🧑‍⚕️")

# Custom CSS for better appearance
# Custom CSS for better appearance
# st.markdown("""
# <style>
#     .main {
#         background-color: #f0f2f5;
#     }
#     .stButton > button {
#         background-color: #4CAF50; /* Green */
#         color: white;
#         border: none;
#         padding: 15px 32px;
#         text-align: center;
#         text-decoration: none;
#         display: inline-block;
#         font-size: 16px;
#         margin: 10px 0;
#         cursor: pointer;
#         border-radius: 8px;
#     }
#     .stTextInput, .stNumberInput, .stSelectbox {
#         margin-bottom: 15px;
#     }
# </style>
# """, unsafe_allow_html=True)

# # Function to create input fields
# def create_input_fields(model_type):
#     if model_type == 'Diabetes Prediction':
#         st.header('Diabetes Prediction using ML')
#         st.write("Please enter the following details to predict diabetes:")
#         inputs = {}
#         col1, col2, col3 = st.columns(3)

#         with col1:
#             inputs['Pregnancies'] = st.number_input('Number of Pregnancies', min_value=0)
#             inputs['Glucose Level'] = st.number_input('Glucose Level', min_value=0.0)
#             inputs['Skin Thickness'] = st.number_input('Skin Thickness value', min_value=0.0)

#         with col2:
#             inputs['Blood Pressure'] = st.number_input('Blood Pressure value', min_value=0.0)
#             inputs['Insulin Level'] = st.number_input('Insulin Level', min_value=0.0)
#             inputs['BMI'] = st.number_input('BMI value', min_value=0.0)

#         with col3:
#             inputs['Diabetes Pedigree Function'] = st.number_input('Diabetes Pedigree Function value', min_value=0.0)
#             inputs['Age'] = st.number_input('Age of the Person', min_value=0)

#         return inputs

#     elif model_type == 'Heart Disease Prediction':
#         st.header('Heart Disease Prediction using ML')
#         st.write("Please enter the following details to predict heart disease:")
#         inputs = {}
#         col1, col2, col3 = st.columns(3)

#         with col1:
#             inputs['Age'] = st.number_input('Age', min_value=0)
#             inputs['Resting Blood Pressure'] = st.number_input('Resting Blood Pressure')
#             inputs['Major vessels colored by fluoroscopy'] = st.number_input('Major vessels colored by fluoroscopy')

#         with col2:
#             inputs['Sex'] = st.selectbox('Sex', options=[0, 1])  # Assuming binary input
#             inputs['Serum Cholestoral in mg/dl'] = st.number_input('Serum Cholestoral in mg/dl')
#             inputs['thal: 0 = normal; 1 = fixed defect; 2 = reversible defect'] = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

#         with col3:
#             inputs['Chest Pain types'] = st.number_input('Chest Pain types', min_value=0)
#             inputs['Fasting Blood Sugar > 120 mg/dl'] = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1])
#             inputs['Maximum Heart Rate achieved'] = st.number_input('Maximum Heart Rate achieved')

#         return inputs

#     elif model_type == "Parkinsons Prediction":
#         st.header("Parkinson's Disease Prediction using ML")
#         st.write("Please enter the following details to predict Parkinson's disease:")
#         inputs = {}
#         cols = st.columns(5)

#         with cols[0]:
#             inputs['MDVP:Fo(Hz)'] = st.number_input('MDVP:Fo(Hz)')
#             inputs['MDVP:Jitter(%)'] = st.number_input('MDVP:Jitter(%)')
#             inputs['MDVP:RAP'] = st.number_input('MDVP:RAP')
#             inputs['MDVP:Shimmer'] = st.number_input('MDVP:Shimmer')
#             inputs['NHR'] = st.number_input('NHR')

#         with cols[1]:
#             inputs['MDVP:Fhi(Hz)'] = st .number_input('MDVP:Fhi(Hz)')
#             inputs['MDVP:Jitter(Abs)'] = st.number_input('MDVP:Jitter(Abs)')
#             inputs['MDVP:PPQ'] = st.number_input('MDVP:PPQ')
#             inputs['MDVP:Shimmer(dB)'] = st.number_input('MDVP:Shimmer(dB)')
#             inputs['HNR'] = st.number_input('HNR')

#         with cols[2]:
#             inputs['MDVP:Flo(Hz)'] = st.number_input('MDVP:Flo(Hz)')
#             inputs['MDVP:RAP'] = st.number_input('MDVP:RAP')
#             inputs['Shimmer:APQ3'] = st.number_input('Shimmer:APQ3')
#             inputs['Shimmer:APQ5'] = st.number_input('Shimmer:APQ5')
#             inputs['RPDE'] = st.number_input('RPDE')

#         with cols[3]:
#             inputs['MDVP:APQ'] = st.number_input('MDVP:APQ')
#             inputs['Shimmer:DDA'] = st.number_input('Shimmer:DDA')
#             inputs['DFA'] = st.number_input('DFA')
#             inputs['spread1'] = st.number_input('spread1')
#             inputs['D2'] = st.number_input('D2')

#         with cols[4]:
#             inputs['PPE'] = st.number_input('PPE')
#             inputs['spread2'] = st.number_input('spread2')

#         return inputs

# # getting the working directory of the main.py
# working_dir = os.path.dirname(os.path.abspath(__file__))

# # loading the saved models
# diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
# heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
# parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# # sidebar for navigation
# with st.sidebar:
#     selected = option_menu('Multiple Disease Prediction System',
#                            ['Diabetes Prediction',
#                             'Heart Disease Prediction',
#                             'Parkinsons Prediction'],
#                            menu_icon='hospital-fill',
#                            icons=['activity', 'heart', 'person'],
#                            default_index=0)

# # Function to create input fields
# def create_input_fields(model_type):
#     if model_type == 'Diabetes Prediction':
#         st.header('Diabetes Prediction using ML')
#         st.write("Please enter the following details:")
#         inputs = {
#             'Pregnancies': st.number_input('Number of Pregnancies', min_value=0),
#             'Glucose Level': st.number_input('Glucose Level', min_value=0.0),
#             'Blood Pressure': st.number_input('Blood Pressure value', min_value=0.0),
#             'Skin Thickness': st.number_input('Skin Thickness value', min_value=0.0),
#             'Insulin Level': st.number_input('Insulin Level', min_value=0.0),
#             'BMI': st.number_input('BMI value', min_value=0.0),
#             'Diabetes Pedigree Function': st.number_input('Diabetes Pedigree Function value', min_value=0.0),
#             'Age': st.number_input('Age of the Person', min_value=0)
#         }
#         return inputs

#     elif model_type == 'Heart Disease Prediction':
#         st.header('Heart Disease Prediction using ML')
#         st.write("Please enter the following details:")
#         inputs = {
#             'Age': st.number_input('Age', min_value=0),
#             'Sex': st.selectbox('Sex', options=[0, 1]),  # Assuming binary input
#             'Chest Pain types': st.number_input('Chest Pain types', min_value=0),
#             'Resting Blood Pressure': st.number_input('Resting Blood Pressure'),
#             'Serum Cholestoral in mg/dl': st.number_input('Serum Cholestoral in mg/dl'),
#             'Fasting Blood Sugar > 120 mg/dl': st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1]),
#             'Resting Electrocardiographic results': st.number_input('Resting Electrocardiographic results'),
#             'Maximum Heart Rate achieved': st.number_input('Maximum Heart Rate achieved'),
#             'Exercise Induced Angina': st.selectbox('Exercise Induced Angina', options=[0, 1]),
#             'ST depression induced by exercise': st.number_input('ST depression induced by exercise'),
#             'Slope of the peak exercise ST segment': st.number_input('Slope of the peak exercise ST segment'),
#             'Major vessels colored by fluoroscopy': st.number_input('Major vessels colored by fluoroscopy'),
#             'thal: 0 = normal; 1 = fixed defect; 2 = reversible defect': st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')
#         }
#         return inputs

#     elif model_type == "Parkinsons Prediction":
#         st.header("Parkinson's Disease Prediction using ML")
#         st.write("Please enter the following details:")
#         inputs = {
#             'MDVP:Fo(Hz)': st.number_input('MDVP:Fo(Hz)'),
#             'MDVP:Fhi(Hz)': st.number_input('MDVP:Fhi(Hz)'),
#             'MDVP:Flo(Hz)': st.number_input('MDVP:Flo(Hz)'),
#             'MDVP:Jitter(%)': st.number_input('MDVP:Jitter(%)'),
#             'MDVP:Jitter(Abs)': st.number_input('MDVP:Jitter(Abs)'),
#             'MDVP:RAP': st.number_input('MDVP:RAP'),
#             'MDVP:PPQ': st.number_input('MDVP:PPQ'),
#             'Jitter:DDP': st.number_input('Jitter:DDP'),
#             'MDVP:Shimmer': st.number_input('MDVP:Shimmer'),
#             'MDVP:Shimmer(dB)': st.number_input('MDVP:Shimmer(dB)'),
#             'Shimmer:APQ3': st.number_input('Shimmer:APQ3'),
#             'Shimmer:APQ5': st.number_input('Shimmer:APQ5'),
#             'MDVP:APQ': st.number_input('MDVP:APQ'),
#             'Shimmer:DDA': st.number_input('Shimmer:DDA'),
#             'NHR': st.number_input('NHR'),
#             'HNR': st.number_input('HNR'),
#             'RPDE': st.number_input ('RPDE'),
#             'DFA': st.number_input('DFA'),
#             'spread1': st.number_input('spread1'),
#             'spread2': st.number_input('spread2'),
#             'D2': st.number_input('D2'),
#             'PPE': st.number_input('PPE')
#         }
#         return inputs

# # Create input fields based on selected prediction type
# user_inputs = create_input_fields(selected)

# # Prediction logic
# if selected == 'Diabetes Prediction':
#     if st.button('Diabetes Test Result'):
#         user_input = [user_inputs[key] for key in user_inputs]
#         diab_prediction = diabetes_model.predict([user_input])
#         diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
#         st.success(diab_diagnosis)

# elif selected == 'Heart Disease Prediction':
#     if st.button('Heart Disease Test Result'):
#         user_input = [user_inputs[key] for key in user_inputs]
#         heart_prediction = heart_disease_model.predict([user_input])
#         heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
#         st.success(heart_diagnosis)

# elif selected == "Parkinsons Prediction":
#     if st.button("Parkinson's Test Result"):
#         user_input = [user_inputs[key] for key in user_inputs]
#         parkinsons_prediction = parkinsons_model.predict([user_input])
#         parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
#         st.success(parkinsons_diagnosis) 
