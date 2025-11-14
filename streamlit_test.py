import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sijoitustrendit", layout="wide")
st.title("Sijoitustrendit ajassa")

# --- LUE TIEDOSTO SUORAAN ---
file_path = "investmentProfit.csv"

df = pd.read_csv(
    file_path,
    sep=";",
    decimal=",",
    quotechar='"',
    engine="python"
)

# Poista tyhjät / ylimääräiset sarakkeet lopusta
df = df.dropna(axis=1, how="all")
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# Varmista, että kk on numeerinen
df["kk"] = pd.to_numeric(df["kk"], errors="coerce")

# Näytä raakadata
st.subheader("Raakadata")
st.dataframe(df)

# Y-sarakkeet (kaikki muut kuin "kk")
numeric_cols = [c for c in df.columns if c != "kk"]

st.subheader("Valitse piirtosarakkeet")
selected_cols = st.multiselect(
    "Valitse mitä sarakkeita piirretään Y-akselille",
    numeric_cols,
    default=numeric_cols
)

if not selected_cols:
    st.warning("Valitse vähintään yksi sarake nähdäksesi trendin.")
else:
    plot_df = df.set_index("kk")[selected_cols]

    st.subheader("Trendikäyrät")
    st.line_chart(plot_df)
