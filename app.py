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

st.subheader("In-depth Information")
markdown_expander()