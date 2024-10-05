# .venv\Scripts\activate.bat
# deactivate

import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("Ma consommation d'énergie")


csv_file_path = 'AEP_hourly.csv' 
csv_file = pd.read_csv(csv_file_path)

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode("utf-8")


csv = convert_df(csv_file)


st.download_button(
    label="Télecharger le modèle",
    data=csv,
    file_name="Modele_CSV.csv",
    mime="text/csv",
)

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    
    dataframe.columns.values[0] = "date"
    dataframe.columns.values[1] = "MW"

    dataframe['date'] = pd.to_datetime(dataframe['date'], errors='coerce')  # Use errors='coerce' to handle invalid dates

    # st.line_chart(dataframe, x="date", y="MW")
    st.line_chart(dataframe.set_index("date")["MW"])

    st.dataframe(dataframe,use_container_width=True)



# left_column, right_column = st.columns((9, 1))
# progress_bar = left_column.progress(0)
# status_text = right_column.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)

# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%%" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

# progress_bar.empty()
# status_text.empty()

