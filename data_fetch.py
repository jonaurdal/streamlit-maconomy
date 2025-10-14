import requests
import pandas as pd
import streamlit as st

@st.cache_data(ttl=300)  # Cache i 300 sekunder (TTL = Time To Live)
def hent_alle_brukere(api_url: str) -> pd.DataFrame:
    """Henter alle brukere fra MockAPI og returnerer som DataFrame."""
    try:
        res = requests.get(api_url)
        res.raise_for_status()
        data = res.json()
        df = pd.DataFrame(data)

        # Rydd opp kolonnenavn
        df.rename(columns={
            "Name1": "Navn",
            "hasDeliveredTime": "Levert",
            "department": "Avdeling"
        }, inplace=True)

        return df

    except requests.exceptions.RequestException as e:
        st.error(f"Feil ved henting av data: {e}")
        return pd.DataFrame()
