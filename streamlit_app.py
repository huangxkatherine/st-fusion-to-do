import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Fusion Education", layout="wide")

def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
                return None
        return r.json()

# -- ASSETS --
lottie = "https://lottie.host/58fb7ece-b89d-4757-ba79-db51a7842646/LWQp5WwdiE.json"

# -- HEADER SECTION --
    
with st.container():
    
        st.subheader("Fusion Education")
        st.title("To-Do List")
        st.write("[Learn More](https://www.fusionedus.com)")

# -- LIST OF ACTIVITIES --

with st.container():
        st.write("---")
        left_column, right_column = st. columns(2)
        with left_column:
                st. header("Activities to be completed:")
                st.write(
                        """
                        - Activity 1
                        - Activity 2
                        - Activity 3
                        """
                )
        with right_column:
                st_lottie(lottie, height=300, key="to do")
