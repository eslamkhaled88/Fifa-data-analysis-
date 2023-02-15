

import pandas as pd 
import joblib
import streamlit as st


model = joblib.load('banking.h5')
inputs = joblib.load('input.h5')


def predict (CreditScore, Geography, Gender, Age, Tenure, Balance ,NumOfProducts , HasCrCard , IsActiveMember ,EstimatedSalary ):
    test_dataframe = pd.DataFrame(columns=inputs)
    test_dataframe.at[0, 'CreditScore'] = CreditScore
    test_dataframe.at[0, 'Geography'] =Geography
    test_dataframe.at[0, 'Gender'] =Gender
    test_dataframe.at[0, 'Age']=Age
    test_dataframe.at[0, 'Tenure']=Tenure
    test_dataframe.at[0,'Balance'] =Balance 
    test_dataframe.at[0,'NumOfProducts'] =NumOfProducts 
    test_dataframe.at[0,'HasCrCard'] = HasCrCard
    test_dataframe.at[0,'IsActiveMember'] = IsActiveMember
    test_dataframe.at[0,'EstimatedSalary'] =EstimatedSalary
    results = model.predict(test_dataframe)[0]
    return results

def main ():
    st.title("welcome to banking classfier project")
    CreditScore = st.slider('CreditScore' , min_value=350.000000 , max_value=850.000000 , value=400.000000 , step=20.000000)
    Geography = st.selectbox("Geography" ,['France', 'Germany', 'Spain'])
    Gender = st.selectbox('Gender' , ['Male' , 'Female'])
    Age = st.slider('Age' , min_value=18 , max_value=80 , value=20 , step=1)
    Tenure = st.slider('Tenure' , min_value=1.0 , max_value=8.0 , value=2.0 , step=0.5)
    Balance = st.slider('Balance' , min_value=0 , max_value=250000 , value= 50000 , step=2000)
    NumOfProducts = st.slider('NumOfProducts' , min_value=1 , max_value=5 , value=1 , step=1)
    HasCrCard = st.selectbox('HasCrCard' , [0 , 1])
    IsActiveMember = st.selectbox('IsActiveMember' , [0 , 1])
    EstimatedSalary = st.slider('EstimatedSalary' , min_value= 11.0 , max_value=199992.480000 , value = 20000.0 , step=200.0)
    
    
    if st.button('predict'):
        ans = predict(CreditScore, Geography, Gender, Age, Tenure, Balance ,NumOfProducts , HasCrCard , IsActiveMember ,EstimatedSalary )
        if ans == 0 :
            st.write("you are exited")
        else :
            st.write("you are not exited")
main() 
