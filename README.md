# streamlit-maconomy#

Dette prosjektet er et mock-dashboard laget med [Streamlit](https://streamlit.io/) for å visualisere leveranse- og prosjektdata – inspirert av hvordan en integrasjon mot Deltek Maconomy kunne se ut.

Per i dag brukes data fra en mock API (mockapi.io), men strukturen er lagt opp slik at det enkelt kan utvides til ekte API-er og autentisering.

---

## 🚀 Funksjonalitet

- Oversikt over hvem som har levert / ikke levert timeliste forrige uke
- Visualisering som **stacked bar chart per avdeling**
- Kode og struktur klar for utvidelser som:
  - Fakturert vs. ikke fakturert
  - Prosjektoversikt
  - Tilgangsstyring / brukertilpasning

---

## 🗂️ Prosjektstruktur

streamlit-maconomy/
│
├── app.py # Hovedapplikasjonen
├── data_fetch.py # Henter data fra API (med caching)
├── requirements.txt # Avhengigheter
│
├── charts/ # Visualiseringer
│ └── stacked_charts.py # Stacked bar-diagrammer
│
├── components/ # Header/Sidebar osv.
│ └── layout.py # Gjenbrukbare UI-elementer
│
└── .env.example # Miljøvariabler (API-nøkler hvis aktuelt)

yaml
Copy code

---

## ⚙️ Hvordan kjøre appen

1. **Installer avhengigheter:**

```bash
pip install -r requirements.txt
(Valgfritt) Lag .env-fil hvis du bruker API-nøkler

bash
Copy code
cp .env.example .env
Kjør appen:

bash
Copy code
streamlit run app.py
🧪 Demo-API (MockAPI.io)
Dataene i appen hentes fra:

bash
Copy code
https://68ed61bfdf2025af78000a0f.mockapi.io/api/v1/deliveredTime
Dette gir en liste med personer og deres timeleveringsstatus per avdeling.

📌 Planlagte utvidelser
🔒 Autentisering med API-nøkkel

📊 Flere dashboards: fakturering, prosjektstatus

👥 Rollebasert tilgang

☁️ Distribusjon på Streamlit Cloud eller egen server

👤 Forfatter
Jon Aurdal
GitHub: @jonaurdal

📝 Lisens
Dette prosjektet kan brukes fritt for læring og utvikling. Se LICENSE for mer info.

yaml
Copy code

---

Vil du at jeg lager en `README.md`-fil og sender deg den som fil også – eller vil du lime dette rett
