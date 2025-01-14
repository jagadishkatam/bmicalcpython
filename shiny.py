
import streamlit as st
import streamlit.web.bootstrap
import pandas as pd
from streamlit.web import cli as stcli
import sys
#import statsmodels.api as sm
# from PIL import image

st.title('BMI Calculator')
st.sidebar.markdown("## User Inputs")
age = st.sidebar.slider('Age',0,100,40)
gender = st.sidebar.radio('Gender',['Male','Female'])
height = st.sidebar.number_input('Height in cm', placeholder='in cm', value=170)
weight = st.sidebar.number_input('Weight in kg', placeholder='in kg', value=73)


code = """
# code used to calculate the BMI
bmi = weight/((height/100)**2)

"""

st.code(code, language='python')

def classify_bmi_with_age_gender(bmi, gender, age):
    """
    Classify BMI based on gender and age-specific ranges.

    Parameters:
        bmi (float): The calculated BMI.
        gender (str): Gender of the person ('male' or 'female').
        age (int): Age of the person in years.

    Returns:
        str: BMI classification category.
    """
    gender = gender.lower()
    if gender not in ["male", "female"]:
        raise ValueError("Gender must be 'male' or 'female'.")
    if age <= 0:
        raise ValueError("Age must be greater than zero.")

    # General adult classification (18+ years)
    if age >= 18:
        if gender == "male":
            if bmi < 18.5:
                return st.image("bmi1.png", caption="Underweight")
            elif 18.5 <= bmi < 25:
                return st.image("bmi2.png", caption="Normal weight")
            elif 25 <= bmi < 30:
                return st.image("bmi3.png", caption="Overweight")
            else:
                return st.image("bmi4.png", caption="Obesity")
        else:  # Female
            if bmi < 18.0:
                return st.image("wbmi1.png", caption="Underweight")
            elif 18.0 <= bmi < 24:
                return st.image("wbmi2.png", caption="Normal weight")
            elif 24 <= bmi < 29:
                return st.image("wbmi3.png", caption="Overweight")
            else:
                return st.image("wbmi4.png", caption="Obesity")

    # Children and teens classification (<18 years)
    else:
        if bmi < 5:
            return "Underweight"
        elif 5 <= bmi < 85:
            return "Healthy weight"
        elif 85 <= bmi < 95:
            return "Overweight"
        else:
            return "Obesity"


if st.sidebar.button('Submit'):
    bmi = weight/((height/100)**2)
    st.text("Your BMI Index is {0:.3}.".format(bmi))
    bmi_category = classify_bmi_with_age_gender(bmi, gender, age)
    # print(bmi_category)


