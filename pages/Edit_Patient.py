import streamlit as st
from firebase_utils.firebase_utils import get_all_patients, update_patient

st.title("Edit Patient")

# retrieve all patients
patients = get_all_patients()

patient_id = st.text_input("Patient ID")

# ('Allergy', 'Immunization', 'Family History', 'Functional Status', 'Lab Value', 'Condition', 'Vital Sign')

ENTRY_TYPES = {
    'Allergy': {
        'substance': 'Substance',
        'reaction': 'Reaction',
        'detection_date': 'Detection Date'
    },
    'Immunization': {
        'vaccine': 'Vaccine',
        'date': "Date (MM-DD-YYYY)",
        'response': 'Adverse Reaction (Y or N)'
    },
    'Family History': {
        'relation': "Family Relation",
        'condition': 'Condition',
        "age_at_diagnosis": "Age at Diagnosis"
    },
    "Condition": {
        "condition": "Condition Name",
        "diagnosis_date": "Diagnosis Date (MM-DD-YYY)",
        "active": "Active? (Y/N)"
    },
    "Vital Sign": {
        "name": "Name",
        "value": "Value",
        "date": "Date (MM-DD-YYYY)"
    },
    "Lab Value": {
        "name": "Name",
        "value": "Value",
        "date": "Date (MM-DD-YYYY)"
    }
}

entry_keys = set(ENTRY_TYPES.keys())


entry_option = st.selectbox(
    "What do you want to add to the patient?",
    entry_keys
)

entry_form_keys = ENTRY_TYPES[entry_option]

if patient_id != '' and patient_id not in patients:
    st.write("Patient ID not found")

if patient_id in patients:
    selected_patient = patients[patient_id]
    #st.write(selected_patient)

    with st.form("entry-form", clear_on_submit=True):
        for key, value in entry_form_keys.items():
            st.text_input(value, key=key)

        submitted = st.form_submit_button("Update Patient")

        if submitted:
            entry_obj = {}
            for key in entry_form_keys.keys():
                entry_obj[key] = st.session_state[key]

            st.write(entry_obj)
            update_patient(patient_id, entry_option, entry_obj)

    st.write(patients[patient_id])
