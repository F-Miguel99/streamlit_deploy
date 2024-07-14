import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime

# reading csv file
# df_data = pd.read_csv("dash_analise_fifa/datasets/FIFA23_official_data.csv", index_col=0)
# displaying data
# df_data
if "data" not in st.session_state:
    df_data = pd.read_csv("dash_analise_fifa/datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    # df_data["Contract Valid Until"] = df_data["Contract Valid Until"].astype(int)
    # df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data



st.write("# FIFA OFFICIAL DATASET! ")
st.sidebar.markdown("Developed by: Filipe Miguel")

btn = st.link_button("Acesse os dos no Kaggle", 
                     "https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database?resource=download"


text_explan ="""
The data was retrieved thanks to a crawler that I implemented to retrieve:

    Aggregated data such as name of the players, age, country
    Detailed data such as offensive potential, defense, acceleration
    I like football a lot and this dataset is for me the opportunity to bring my contribution for the realization of projects that can go from simple analysis to elaboration of strategies on optimal composition under constraints…

Acknowledgements

We wouldn't be here without the help of others. I would like to thanks @karangadiya who I got inspiration from, check his repo here !
"""
st.markdown(text_explan)