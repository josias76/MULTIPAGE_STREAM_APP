import streamlit as st
from Home import my_var



st.subheader("Load Data Page")

from Home import my_var
st.write(my_var)












st.sidebar.image("logo1.jpeg", caption="SDA Consulting")
# Bande de bas de page
st.markdown("""
    <hr style="border-top: 1px solid #4CAF50; margin-top: 50px;"/>
    <div style="text-align: center; color: #888; font-size: 0.9em;">
        &copy; 2025 <strong>Josias Nteme</strong> - Tous droits réservés.
    </div>
""", unsafe_allow_html=True)