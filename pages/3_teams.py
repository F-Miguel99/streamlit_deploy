import streamlit as st


st.set_page_config(
    page_title="Players",
    layout="wide",
    #age_tiitle="Players",
)


df_data = st.session_state["data"]


clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)


df_filtered = df_data[df_data["Club"] == club]

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

columns =["Age", "Name", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", 
          "Height(cm.)", "Weight(lbs.)",
          "Contract Valid Until", 'Release Clause(£)']

# df_filtered[columns]

st.dataframe(df_filtered[columns],
             column_config ={
                 "Overall": st.column_config.ProgressColumn("Overall", format="%d", min_value=0, max_value=100),
                 "Value(£)":st.column_config.NumberColumn(),
                 "Photo": st.column_config.ImageColumn(),
                 "Flag": st.column_config.ImageColumn("Country"),
                 }, height=1000)

