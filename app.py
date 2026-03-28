import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# 🔹 Connexion à Google Sheets
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)

client = gspread.authorize(creds)

sheet = client.open("Form_dat").sheet1  # ⚠️ mets le nom exact de ton fichier

# 🔹 Interface utilisateur
st.title("📋 Formulaire simple")

Ferke = st.text_input("ferké")
Kong = st.text_input("kong")
Koye = st.text_input("koye")

# 🔹 Bouton
if st.button("Envoyer"):
    if nom and age and ville:
        sheet.append_row([nom, age, ville])
        st.success("✅ Données envoyées dans Google Sheets !")
    else:
        st.error("❌ Remplis tous les champs")
