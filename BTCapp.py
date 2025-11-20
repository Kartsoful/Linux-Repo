import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px

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
            color: #3C2042 !important;
            text-align: center;
        }

        p, label, span {
            color: #f0f0f0 !important;
        }

        /* Varoitukset tummemmaksi */
        .stAlert {
            background-color: rgba(0, 0, 0, 0.45) !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- DATA ----------

def main():
    bg_gradient = "linear-gradient(135deg, #1a2a6c 0%, #3d5afe 40%, #00bcd4 100%)"
    st.markdown(f"""
        <style>
            .stApp {{
                background: {bg_gradient};
                color: white;
                transition: background 1.2s ease-in-out;
            }}
        </style>
    """, unsafe_allow_html=True)

    conn = mysql.connector.connect(host='localhost', user='kartso', password='kartso123', database='weather')
    df = pd.read_sql('SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 50',conn)
    conn.close()
    st.title('Säädata Helsingistä')    
    st.markdown("<h4>Dataa kerätty 20.11.2025 18:00 UTC+2 alkaen. Näytteenkeruuväli 15min</h4>", unsafe_allow_html=True)
    st.markdown("<h4>Kellonaika on UTC-ajassa</h4>", unsafe_allow_html=True)
    
    st.dataframe(df)

    st.markdown("<h1>Helsingin lämpötilat MySQL-tietokannasta</h1>", unsafe_allow_html=True)
 
    # # Kaikki sarakkeet jotka eivät ole pvm tai id = paikkakuntia
    city_cols = [c for c in df.columns if c not in ('timestamp', 'id')]

    if not city_cols:
        st.error("Tietokannasta ei löytynyt yhtään kaupunkisaraketta.")
        return

    # Piirrä kuvaaja
    fig = px.line(
        df,
        x="timestamp",
        y="temperature",
        markers=True,
        title="Lämpötila",
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
