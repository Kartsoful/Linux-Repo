import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    # Yhteys .streamlit/secrets.toml -> [connections.mysql]
    conn = st.connection("mysql", type="sql")
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

    # Kaikki sarakkeet jotka eivät ole pvm tai id = paikkakuntia
    city_cols = [c for c in df.columns if c not in ("pvm", "id")]

    # Valinta: mitkä kaupungit piirretään
    selected = st.multiselect(
        "Valitse kaupungit:",
        options=city_cols,
        default=city_cols,  # oletuksena kaikki
    )

    if not selected:
        st.warning("Valitse vähintään yksi kaupunki.")
        return

    # px.line osaa piirtää useita sarakkeita, kun annetaan lista
    fig = px.line(
        df,
        x="pvm",
        y=selected,
        markers=True,
        title="Lämpötilat paikkakunnittain",
    )

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
