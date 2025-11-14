import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Investment Profit Analysis")

# Lue tiedosto oikein
@st.cache_data  # Vähentää uudelleenlukua, jos data ei muutu
def load_data():
    df = pd.read_csv('investment_profit.csv', sep=';', decimal=',')
    return df

df = load_data()

# Debuggaus: Näytä sarakkeet ja data
st.subheader("Ladattu data (ensimmäiset rivit)")
st.write("Sarakkeet:", df.columns.tolist())
st.dataframe(df.head(10))  # Näyttää taulun

# Esimerkki: Piirrä kaavio (x = sijoitettu pääoma, y = tuotto 0,01 %:lla)
# Korvaa '0,01' haluamallasi sarakkeella, jos tarvitset toista tuottoa
if 'Sijoitettu_paaoma' in df.columns and '0,01' in df.columns:
    st.subheader("Tuotto kaaviona (0,01 % tuotto)")
    st.line_chart(df, x='Sijoitettu_paaoma', y='0,01')
else:
    st.error("Sarakkeita ei löytynyt – tarkista data.")

# Jos haluat käsitellä NaN-arvoja (esim. täytä nollilla), lisää tämä:
# df = df.fillna(0)