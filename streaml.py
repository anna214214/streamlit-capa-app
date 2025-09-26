import streamlit as st
import pandas as pd

import streamlit as st

# Pobieramy hasło z secrets
APP_PASSWORD = st.secrets["password"]

# Proste logowanie
password_input = st.text_input("🔑 Podaj hasło:", type="password")
if password_input == APP_PASSWORD:
    st.success("✅ Dostęp przyznany")
    # tu umieszczasz całą logikę swojej aplikacji
else:
    st.warning("❌ Złe hasło")


uploaded_file = st.file_uploader("📂 Wgraj raport Excel", type="xlsx")
if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Podgląd danych
    st.write("Podgląd danych:", df.head())

    # KPI
    st.metric("Liczba rekordów", len(df))
    st.metric("Otwarte", df[df["Status"] == "Open"].shape[0])
    st.metric("Zamknięte", df[df["Status"] == "Closed"].shape[0])

    # Wykres
    st.bar_chart(df["Record Type"].value_counts())

    # Filtr statusu
    status_filter = st.selectbox("Filtruj po statusie:", ["All"] + df["Status"].unique().tolist())
    if status_filter != "All":
        df = df[df["Status"] == status_filter]

    st.dataframe(df)
else:
    st.info("👉 Wgraj plik Excel, żeby zobaczyć KPI.")
