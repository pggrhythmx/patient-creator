import streamlit as st

from firebase_utils.firebase_utils import write_to_fb

st.title("Rhythm X - Patient Creation Portal")

# create patient form
with st.form("patient-creation", clear_on_submit=True):


    def create_patient(patient_obj):
        write_to_fb(patient_obj)

    st.write("Basic Info")

    name = st.text_input("Patient Name (First and Last)")
    dob = st.text_input("DOB (MM-DD-YYYY)")
    # compute the age manually vs 2024
    #age = st.text_input("Age")
    gender = st.text_input("Gender (M or F)")

    # allergies = []

    submitted = st.form_submit_button("Create Patient")

    if submitted:
        patient_obj = {
            "name": name,
            "dob": dob,
            "gender": gender,
        }
        create_patient(patient_obj)