import streamlit as st
import pandas as pd
from firebase_utils.firebase_utils import get_all_patients

def dataframe_with_selections(df):
    df_with_selections = df.copy()
    df_with_selections.insert(0, "Select", False)

    # Get dataframe row-selections from user with st.data_editor
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        disabled=df.columns,
    )

    # Filter the dataframe using the temporary column, then drop the column
    selected_rows = edited_df[edited_df.Select]
    return selected_rows.drop('Select', axis=1)


st.title("View Patients")

# retrieve all patients
patients = get_all_patients()

#process patients
patients_display = []
for id, patient in patients.items():
    patients_display.append(
        {
            "ID": id,
            "Name": patient['name']
        }
    )

patient_df = pd.DataFrame(patients_display)
# select one, show the patient json details
selected_patients = dataframe_with_selections(patient_df)

if len(selected_patients) > 0:
    if len(selected_patients) > 1:
        st.write("Multiple patients selected - displaying the first selection only")
    selected_patient_id = selected_patients.iloc[0]["ID"]
    st.write(patients[selected_patient_id])

