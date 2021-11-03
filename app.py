from pathlib import Path

import streamlit as st


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

st.title("Fit Tracker")

nf_md_check = st.checkbox("Nutritional Facts")
nf_md = read_markdown_file("guide/1-Nutritional-Facts.md")

mp_md_check = st.checkbox("Meal Plan")
mp_md = read_markdown_file("guide/2-Meal-Plan.md")

e_md_check = st.checkbox("Exercises")
e_md = read_markdown_file("guide/3-Exercises.md")

ee_md_check = st.checkbox("Exercise Equipment")
ee_md = read_markdown_file("guide/4-Exercise-Equipment.md")

ws_md_check = st.checkbox("Workout Schedule")
ws_md = read_markdown_file("guide/5-Workout-Schedule.md")

if nf_md_check:
    st.markdown(nf_md, unsafe_allow_html=True)
elif mp_md_check:
    st.markdown(mp_md, unsafe_allow_html=True)
elif e_md_check:
    st.markdown(e_md, unsafe_allow_html=True)
elif ee_md_check:
    st.markdown(ee_md, unsafe_allow_html=True)
elif ws_md_check:
    st.markdown(ws_md, unsafe_allow_html=True)