# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sijoituslaskuri", layout="wide")

st.title("Sijoitettu pääoma – korkoskenaariot")

# 1) Lue CSV oikein
# Vaihda polku omaan tiedostonimeen
CSV_PATH = "investmentProfit.csv"

df = pd.read_csv(
    CSV_PATH,
    sep=";",         # sarakkeet eroteltu puolipisteellä
    decimal=",",     # desimaalit pilkulla
    quotechar='"',   # koko rivi lainausmerkeissä
)

# siivotaan sarakenimet
df.columns = [c.strip() for c in df.columns]

# odotetut sarakkeet: kk, sijoitettuPaaoma, 0,01, 0,02, ...
# nimetään halutessa nätimmäksi
if "sijoitettuPaaoma" in df.columns:
    df = df.rename(columns={"sijoitettuPaaoma": "Sijoitettu_pääoma"})

st.subheader("Raakadata")
st.dataframe(df)

# 2) Valitse mitä korkoa piirretään
perussarakkeet = {"kk", "Sijoitettu_pääoma", "sijoitettuPaaoma"}
korkosarakkeet = [c for c in df.columns if c not in perussarakkeet]

valittu_korko = st.selectbox("Valitse korkoskenaario (sarake)", korkosarakkeet)

# 3) Piirrä kuvaaja
fig = px.line(
    df,
    x="kk",
    y=valittu_korko,
    labels={"kk": "Kuukausi", valittu_korko: "Pääoma"},
    title=f"Pääoman kehitys – korko {valittu_korko}",
)
st.plotly_chart(fig, use_container_width=True)

# 4) Näytä yksi rivi tarkemmin
st.subheader("Yksittäisen kuukauden tiedot")
kuukausi = st.slider("Kuukausi", int(df["kk"].min()), int(df["kk"].max()), int(df["kk"].min()))
st.write(df[df["kk"] == kuukausi])
