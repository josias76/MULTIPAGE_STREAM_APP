import streamlit as st



my_var = "This is a home variable"







def main () : 
    st.header("HOME PAGE")
    st.title("APPLICATION MULTIPAGES")
    st.write(my_var)


    choix = st.sidebar.radio("SubMenu",["Description","Documentation"])
    if choix == "Description" : 
        st.subheader("Voici la description de l'application web")
    if choix == "Documentation" : 
        st.subheader("Voici la Documentation de l'application web")

if __name__ == '__main__':
    main ()

st.sidebar.image("logo1.jpeg", caption="SDA Consulting")
# Bande de bas de page
st.markdown("""
    <hr style="border-top: 1px solid #4CAF50; margin-top: 50px;"/>
    <div style="text-align: center; color: #888; font-size: 0.9em;">
        &copy; 2025 <strong>Josias Nteme</strong> - Tous droits réservés.
    </div>
""", unsafe_allow_html=True)