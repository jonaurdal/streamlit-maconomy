import streamlit as st

def vis_header(tittel, undertittel=""):
    st.title(tittel)
    if undertittel:
        st.markdown(f"### {undertittel}")
        st.markdown("---")
