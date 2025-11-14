import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- TYYLIT ----------
st.markdown("""
    <style>
        /* Tausta koko appille */
        .stApp {
            background: linear-gradient(135deg, #0a0f24 0%, #1a2a6c 50%, #3d9ecf 100%);
            color: white;
        }

        /* Keskimmäinen "kortti" sisällölle */
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

        /* Varoitusboxit jne */
        .stAlert {
            background-color: rgba(0, 0, 0, 0.45) !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- DATA ----------

@st.cache_data
def load_data():
    # Yhteys .streamlit/secrets.toml -> [connections.mysql]
    conn = st.connection("mysql", type="sql")
    df = conn.query("SELECT * FROM lampotilat ORDER BY pvm;", ttl=600)

    # Varmistetaan että pvm on datetime
    df["pvm"] = pd.to_datetime(df["pvm"])

    return df

# ---------- APP ----------

def main():
    st.markdown("<h1>Lämpötilat MySQL-tietokannasta</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center; margin-bottom:25px;'>Valitse yksi tai useampi kaupunki, joiden vuorokauden keskilämpötilat haluat nähdä.</p>",
        unsafe_allow_html=True,
    )

    df = load_data()

    # Kaikki sarakkeet jotka eivät ole pvm tai id = paikkakuntia
    city_cols = [c for c in df.columns if c not in ("pvm", "id")]

    if not city_cols:
        st.error("Tietokannasta ei löytynyt yhtään kaupunkisaraketta.")
        return

    # Oletuksena Oulu jos löytyy, muuten kaikki
    default_selection = ["Oulu"] if "Oulu" in city_cols else city_cols

    selected = st.multiselect(
        "Valitse kaupungit:",
        options=city_cols,
        default=default_selection,
    )

    if not selected:
        st.warning("Valitse vähintään yksi kaupunki.")
        return

    # Piirretään kuvaaja
    fig = px.line(
        df,
        x="pvm",
        y=selected,
        markers=True,
        title="Vuorokauden keskilämpötila",
        template="plotly_dark",
    )

    fig.update_layout(
        xaxis_title="Päivämäärä",
        yaxis_title="Lämpötila (°C)",
        legend_title="Kaupunki",
    )

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
