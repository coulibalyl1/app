import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

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
st.title("CL TRANSPORT: BAGAGES")
date_input = st.date_input("Date")
Date = date_input.strftime("%d/%m/%Y")
Abidjan=st.text_input("Abidjan")
Yakro = st.text_input("Yakro")
Ferke = st.text_input("Ferké")
Kong = st.text_input("Kong")
Koye = st.text_input("Koye")

# 🔹 Bouton
if st.button("Envoyer"):
    if Date or Abidjan or Yakro or Ferke or Kong or Koye:
        sheet.append_row([Date,Abidjan,Yakro, Ferke, Kong, Koye])
        st.success("✅ Données envoyées dans Google Sheets !")
