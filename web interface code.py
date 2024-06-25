
import pandas as
pd import numpy
as np import pickle

#loading the saved model
loaded_model=pickle.load(open('C:/Users/hemanth kumar/OneDrive/Desktop/project/machinelearning/trained_model.sav','rb'))

new_data=pd.DataFrame({ 'age': 57,
'sex': 0, 'chest_pain_type':3 , 'resting_bp_s':160 , 'cholesterol':180 , 'fasting_blood_sugar':0 , 'resting_ecg':0 , 'max_heart_rate':156 , 'exercise_angina':0 , 'oldpeak': 1,
'ST_slope': 2
}, index=[1])

p=loaded_model.predict(new_data) if p[0]==0:
print('NO-HEART DISEASE')
else: print('DISEASED')

import numpy as np import pickle
import streamlit as st #loading the saved model

loaded_model=pickle.load(open('C:/Users/hemanth kumar/OneDrive/Desktop/project/machinelearning/trained_model.sav','rb'))

# creating a function for prediction
def heart_prediction(new_data):

#changing the input_data to numpy array
input_data_as_numpy_array=np.asarray(new_data)

#reshape the array as it is predicting for one instance
input_data_reshcayaped=input_data_as_numpy_array.reshape(1,-1)

p=loaded_model.predict(input_data_reshaped) if p[0]==0:
return 'NO-HEART DISEASE'
else:
return 'DISEASED' def main():
#giving a title
st.title('Heart disease prediction web app')

#getting the input data from the user
age=st.text_input('Age of the person		')
sex=st.text_input('Gender of the person	M:1, F:0')
chest_pain_type=st.text_input('Type of the chest pain Typical:1, Atypical:2')
resting_bp_s=st.text_input('Blood sugar value')
cholesterol=st.text_input('Cholesterol value')
fasting_blood_sugar=st.text_input('Fasting blood sugar type')
resting_ecg=st.text_input('Resting ecg value')
max_heart_rate=st.text_input('Heart rate value')
exercise_angina=st.text_input('Exercise angina value')
oldpeak=st.text_input('oldpeak value')

ST_slope=st.text_input('ST slope type')

#code for prediction diagnosis=''

#creating the button for prediction
if st.button('Heart disease test prediction'):

diagnosis=heart_prediction([age,sex,chest_pain_type,resting_bp_s,cholesterol,fasting_blood_sug ar,resting_ecg,max_heart_rate,exercise_angina,oldpeak,ST_slope])

st.success(diagnosis)



if     name ==' main ': main()
