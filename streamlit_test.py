import streamlit as st
import mysql.connector
import pandas as pd

# ---------- PERUS-TYYLIT (staattinen osa) ----------
st.markdown("""
    <style>
        /* Card-tyyppinen keskialue */
        .block-container {
            max-width: 900px;
            padding-top: 40px;
            padding-bottom: 40px;
            background: rgba(255, 255, 255, 0.04);
            margin-top: 40px;
            border-radius: 16px;
            padding-left: 40px;
            padding-right: 40px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }

        h1, h2, h3, h4 {
            color: #ffffff !important;
            text-align: center;
        }

        p, label, span {
            color: #f0f0f0 !important;
        }

        /* Multiselect-boksi */
        .stMultiSelect > div > div {
            background-color: rgba(0, 0, 0, 0.35) !important;
            border: 1px solid rgba(255, 255, 255, 0.35) !important;
        }

        /* Selectin tekstit */
        .stMultiSelect div[data-baseweb="select"] * {
            color: #ffffff !important;
        }

        /* Varoitukset tummemmaksi */
        .stAlert {
            background-color: rgba(0, 0, 0, 0.45) !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- DATA ----------


conn = mysql.connector.connect(host='localhost', user='kartso', password='kartso123', database='weather')
df = pd.read_sql('SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 50',
conn)
conn.close()
st.title('Säädata Helsingistä')
st.dataframe(df)