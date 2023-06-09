import streamlit as st
import streamlit.components.v1 as stc

# Importing other Modules
from eda_app import run_eda_app
from ml_app import run_ml_app


# Core Libraries
import pandas as pd
import numpy as np

html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Early Stage DM Risk Data App </h1>
		<h3 style="color:white;text-align:center;">WINE DATA SET </h3>
		</div>
		"""

decs_temp = """
	### Early Stage Wine Risk Predictor App
			This dataset contains the sign and symptoms data of newly diabetic or would be diabetic patient.
			#### Datasource
				(C:\\Users\\user\\Downloads\\DataSets-main (1)\\DataSets-main\\wine.csv)
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App
"""




# Fxns

def main():
    # st.header("Streamlit")
    stc.html(html_temp)
    
    menu = ['Home','EDA',"ML","About"]
    choice = st.sidebar.selectbox("Memu",menu)
    
    if choice == 'Home':
        st.subheader("Home")
        st.write(decs_temp)
    
    elif choice == "EDA":
        run_eda_app()
        
    elif choice == 'ML':
        run_ml_app()
    
if __name__ == "__main__":
    main()
    