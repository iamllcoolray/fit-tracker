from tracker.markdown_files import markdown_files

import streamlit as st

def losing_weight(pounds, total_weight, ideal_weight):
    return ((total_weight - ideal_weight) / pounds) / 4.34524


def gaining_weight(pounds, total_weight, ideal_weight):
    return ((ideal_weight - total_weight) / pounds) / 4.34524

def bmi(total_weight, total_height):
    return (total_weight / (total_height**2)) * 703

def male_body_fat(bmi, age):
    return ((1.2 * bmi) + (0.23 * age)) - 16.2

def male_bmr(total_weight, total_height, age):
    return 66.47 + (6.24 * total_weight) + \
            (12.7 * total_height) - (6.755 * age)

def female_body_fat(bmi, age):
    return ((1.2 * bmi) + (0.23 * age)) - 5.4

def female_bmr(total_weight, total_height, age):
    return 655.1 + (4.35 * total_weight) + \
            (4.7 * total_height) - (4.7 * age)

def caloric_intake_adj(adjusted):
    if(adjusted == 1):
        return 500
    elif(adjusted == 2):
        return 1000

def caloric_intake_multi(bmr, multiplier):
    return bmr * multiplier

markdown_files.hide_footer()

st.title("Fit Tracker")

with st.sidebar:

    st.header("Tracker Entry")

    st.subheader("How old are you?")
    age = st.number_input("Age", 13, 130, 18)

    st.subheader("What is your sex?")
    sex = st.radio("Sex", ("Male", "Female"))

    st.subheader("How tall are you?")
    feet_height = st.number_input("Feet", 4, 8, 6)
    inches_height = st.number_input("Inches", 0, 11)
    total_height = (feet_height * 12) + inches_height

    st.subheader("How much do you weight?")
    total_weight = st.number_input("Weight", 100, 400, 150)

    st.subheader("How active are you each day?")
    activity_level = st.selectbox(
        "Activity Level", ("Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extremely Active"))

    st.subheader("What is your fitness goal?")
    fitness_goal = st.radio(
        "Fitness Goal", ("Maintain Current Weight", "Lose Weight/Body Fat", "Build Muscle"))

    lose_weight = ""
    gain_weight = ""
    approx_duration = 0

    if fitness_goal == "Lose Weight/Body Fat":
        st.subheader("How much weight do you want to lose in a week?")
        lose_weight = st.radio("Weight", ("1lbs", "2lbs"))

        st.subheader("What is your ideal weight?")
        ideal_weight = st.number_input("Ideal Weight", 100, total_weight)
    elif fitness_goal == "Maintain Current Weight":
        pass
    elif fitness_goal == "Build Muscle":
        st.subheader("How much weight do you want to gain in a week?")
        gain_weight = st.radio("Weight", ("1lbs", "2lbs"))

        st.subheader("What is your ideal weight?")
        ideal_weight = st.number_input("Ideal Weight", total_weight, 400)

results_container = st.container()
with results_container:

    st.header("Personalized Results")

    if lose_weight == "1lbs" or gain_weight == "1lbs":
        pounds = 1
    elif lose_weight == "2lbs" or gain_weight =="2lbs":
        pounds = 2

    bmi = bmi(total_weight, total_height)

    if sex == "Male":
        body_fat = male_body_fat(bmi, age)
        bmr = male_bmr(total_weight, total_height, age)
    elif sex == "Female":
        body_fat = female_body_fat(bmi, age)
        bmr = female_bmr(total_weight, total_height, age)

    if activity_level == "Sedentary":
        caloric_intake = caloric_intake_multi(bmr, 1.2)
    elif activity_level == "Lightly Active":
        caloric_intake = caloric_intake_multi(bmr, 1.375)
    elif activity_level == "Moderately Active":
        caloric_intake = caloric_intake_multi(bmr, 1.55)
    elif activity_level == "Very Active":
        caloric_intake = caloric_intake_multi(bmr, 1.725)
    elif activity_level == "Extremely Active":
        caloric_intake = caloric_intake_multi(bmr, 1.9)

    if lose_weight == "1lbs":
        caloric_intake -= caloric_intake_adj(pounds)
        approx_duration = losing_weight(pounds, total_weight, ideal_weight)
    elif lose_weight == "2lbs":
        caloric_intake -= caloric_intake_adj(pounds)
        approx_duration = losing_weight(pounds, total_weight, ideal_weight)
    elif gain_weight == "1lbs":
        caloric_intake += caloric_intake_adj(pounds)
        approx_duration = gaining_weight(pounds, total_weight, ideal_weight)
    elif gain_weight == "2lbs":
        caloric_intake += caloric_intake_adj(pounds)
        approx_duration = gaining_weight(pounds, total_weight, ideal_weight)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Body Fat Percentage", str(round(body_fat)) + "%")
    col2.metric("Body Mass Index", round(bmi))
    col3.metric("Basal Metabolic Rate", round(bmr))
    col4.metric("Caloric Intake", round(caloric_intake))
    if round(approx_duration) > 0:
        st.metric("Approximate Duration (months)", round(approx_duration))

info_container = st.container()
with info_container:
    st.header("Additional Information")
    markdown_files.markdown_expander()
