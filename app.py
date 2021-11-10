from pathlib import Path

import streamlit as st


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

def markdown_expander():
    expander_titles = ["Nutritional Facts", "Meal Plan", "Exercises", "Exercise Equipment", "Workout Schedule"]
    markdown_files = ["1-Nutritional-Facts.md", "2-Meal-Plan.md", "3-Exercises.md", "4-Exercise-Equipment.md", "5-Workout-Schedule.md"]
    for ex_t, md_f in zip(expander_titles, markdown_files):
        with st.expander(ex_t):
            md = read_markdown_file("guide/" + md_f)
            st.markdown(md, unsafe_allow_html=True)

st.title("Fit Tracker")

data_container = st.container()
with data_container:
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Data Input")
        
        st.subheader("How old are you?")
        age = st.number_input("Age", 13, 130)

        st.subheader("What is your sex?")
        sex = st.radio("Sex", ("Male", "Female"))

        st.subheader("How tall are you?")
        feet_height = st.number_input("Feet", 4, 8)
        inches_height = st.number_input("Inches", 0, 11)
        total_height = (feet_height * 12) + inches_height

        st.subheader("How much do you weight?")
        total_weight = st.slider("Weight", 50, 400)
    
    with col2:
        st.header("Your Results")
        bmi = (total_weight / (total_height**2)) * 703
        
        if sex == "Male":
            body_fat = ((1.2 * bmi) + (0.23 * age)) - 16.2
        elif sex == "Female":
            body_fat = ((1.2 * bmi) + (0.23 * age)) - 5.4

info_container = st.container()
with info_container:
    st.header("Additional Information")
    markdown_expander()