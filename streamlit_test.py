import streamlit as st
import pandas as pd
import plotly.express as px

# Haetaan data MySQL:stä
@st.cache_data
def load_data():
    conn = st.connection("mysql", type="sql")
    # Hae kaikki sarakkeet lampotilat-taulusta
    df = conn.query("SELECT * FROM lampotilat ORDER BY pvm;", ttl=600)
    # Varmistetaan että pvm on datetime
    df["pvm"] = pd.to_datetime(df["pvm"])
    return df

def main():
    st.title("Plot data from MySql")
    st.write("Lämpötiloja (lampotilat-taulusta)")

    df = load_data()
    st.write("Raakadata:")
    st.dataframe(df)

    # Paikkakuntasarakkeet = kaikki muut paitsi pvm ja id (jos sellainen on)
    city_cols = [c for c in df.columns if c not in ("pvm", "id")]

    # Multiselect: käyttäjä valitsee mitä piirretään
    selected = st.multiselect(
        "Minkä kaupunkien lämpötilat piirretään?",
        options=city_cols,
        default=["Oulu"] if "Oulu" in city_cols else city_cols,
    )

    if not selected:
        st.warning("Valitse vähintään yksi kaupunki.")
        return

    # Muutetaan data long-muotoon, jotta saadaan yksi kuva jossa monta käyrää
    df_long = df.melt(
        id_vars="pvm",
        value_vars=selected,
        var_name="Kaupunki",
        value_name="Lämpötila",
    )

    fig = px.line(
        df_long,
        x="pvm",
        y="Lämpötila",
        color="Kaupunki",
        markers=True,
        title="Lämpötilat paikkakunnittain",
    )

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
