from pathlib import Path

import streamlit as st

class markdown_files():
    
    def markdown_expander():
        expander_titles = ["Nutritional Facts", "Meal Plan", "Workout Schedule"]
        markdown_files = ["guide/1-Nutritional-Facts.md",
                        "guide/2-Meal-Plan.md", "guide/3-Workout-Schedule.md"]
        for ex_t, md_f in zip(expander_titles, markdown_files):
            with st.expander(ex_t):
                md = Path(md_f).read_text()
                st.markdown(md, unsafe_allow_html=True)

    def hide_footer():
        hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>

        """
        st.markdown(hide_streamlit_style, unsafe_allow_html=True)