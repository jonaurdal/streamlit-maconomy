import streamlit as st
from data_fetch import hent_alle_brukere
from charts.stacked_charts import vis_timer_levert_stacked
from components.layout import vis_header

API_URL = "https://68ed61bfdf2025af78000a0f.mockapi.io/api/v1/deliveredTime"

def main():
    st.set_page_config(page_title="Maconomy Dashboard", layout="wide")
    vis_header("Maconomy Dashboard", "Oversikt over leverte timer per avdeling")
    
    df = hent_alle_brukere(API_URL)
    if df.empty:
        st.warning("Ingen data tilgjengelig.")
        return

    valg = st.sidebar.selectbox("Velg visning:", ["Timer levert (stacked)"])
    if valg == "Timer levert (stacked)":
        st.subheader("📌 Timer levert – per avdeling")
        st.altair_chart(vis_timer_levert_stacked(df), use_container_width=True)

if __name__ == "__main__":
    main()
