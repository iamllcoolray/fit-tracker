from pathlib import Path

import streamlit as st


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

st.title("Fit Tracker")

with st.expander("Nutritional Facts"):
    nf_md = read_markdown_file("guide/1-Nutritional-Facts.md")
    st.markdown(nf_md, unsafe_allow_html=True)

with st.expander("Meal Plan"):
    mp_md = read_markdown_file("guide/2-Meal-Plan.md")
    st.markdown(mp_md, unsafe_allow_html=True)

with st.expander("Exercises"):
    e_md = read_markdown_file("guide/3-Exercises.md")
    st.markdown(e_md, unsafe_allow_html=True)

with st.expander("Exercise Equipment"):
    ee_md = read_markdown_file("guide/4-Exercise-Equipment.md")
    st.markdown(ee_md, unsafe_allow_html=True)

with st.expander("Workout Schedule"):
    ws_md = read_markdown_file("guide/5-Workout-Schedule.md")
    st.markdown(ws_md, unsafe_allow_html=True)