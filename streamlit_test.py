import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- PERUS-TYYLIT (ilman taustaväriä) ----------
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
    df = load_data()

    st.markdown("<h1>Lämpötilat MySQL-tietokannasta</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center; margin-bottom:25px;'>Valitse yksi tai useampi kaupunki, joiden vuorokauden keskilämpötilat haluat nähdä.</p>",
        unsafe_allow_html=True,
    )

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

    # ----- LASKE KESKIARVO VALITUILLE KAUPUNGEILLE -----
    # Kaikkien valittujen kaupunkien kaikkien lämpötilojen keskiarvo
    avg_temp = df[selected].stack().mean()

    # Valitse taustagradientti keskiarvon perusteella
    if avg_temp <= 3:
        # kylmä
        bg_gradient = "linear-gradient(135deg, #001f3f 0%, #003f7f 40%, #0074d9 100%)"
        label = "Kylmä"
    elif avg_temp <= 8:
        # viileä
        bg_gradient = "linear-gradient(135deg, #1a2a6c 0%, #3d5afe 40%, #00bcd4 100%)"
        label = "Viileä"
    else:
        # lämmin
        bg_gradient = "linear-gradient(135deg, #7b1fa2 0%, #ff7043 40%, #ff9800 100%)"
        label = "Lämmin"

    # Injektoi taustaväri dynaamisesti .stApp:iin
    st.markdown(f"""
        <style>
            .stApp {{
                background: {bg_gradient};
                color: white;
                transition: background 1.2s ease-in-out;
            }}
        </style>
    """, unsafe_allow_html=True)


    # Näytä keskiarvo ja luokitus
    st.markdown(
        f"<p style='text-align:center; font-size:18px; margin-top:5px;'>"
        f"Valittujen kaupunkien keskilämpötila: <b>{avg_temp:.1f} °C</b> ({label})"
        f"</p>",
        unsafe_allow_html=True,
    )

    # ----- PIIRRÄ KUVA -----
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
