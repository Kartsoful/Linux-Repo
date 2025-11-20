import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px

# ---------- PERUS-TYYLIT (staattinen osa) ----------
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        .stApp, .block-container, * {
            font-family: 'Inter', sans-serif;
        }

        /* Keskialue (card) */
        .block-container {
            max-width: 960px;
            padding: 48px 48px 56px 48px;
            background: rgba(255, 255, 255, 0.06);
            margin-top: 32px;
            border-radius: 20px;
            backdrop-filter: blur(18px);
            border: 1px solid rgba(255, 255, 255, 0.25);
            box-shadow: 0 8px 32px rgba(0,0,0,0.35);
        }

        h1, h2, h3, h4 {
            color: #F5F7FA !important;
            text-align: center;
            letter-spacing: .5px;
        }

        p, label, span, .stMarkdown, .stText, .stDataFrame, .stPlotlyChart {
            color: #E6E9ED !important;
        }

        /* Napit */
        .stButton > button {
            background: linear-gradient(135deg,#3d5afe 0%,#00bcd4 80%);
            color: #fff;
            border: none;
            padding: .6rem 1.1rem;
            font-weight: 600;
            border-radius: 10px;
            transition: transform .15s ease, box-shadow .15s ease;
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(0,188,212,0.35);
        }

        /* Alertit */
        .stAlert {
            background: rgba(0,0,0,0.55) !important;
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 12px;
        }

        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }
        ::-webkit-scrollbar-track {
            background: rgba(255,255,255,0.05);
        }
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg,#3d5afe,#00bcd4);
            border-radius: 20px;
        }

        /* DataFrame header */
        .stDataFrame [data-testid="column-header"] {
            background: linear-gradient(135deg,#283e91,#006b88) !important;
            color: #fff !important;
        }

        /* Linkit */
        a {
            color: #7ddfff !important;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
""", unsafe_allow_html=True)

def main():
    bg_gradient = "linear-gradient(140deg, #1a2a6c 0%, #243b89 30%, #0b6685 65%, #008fa1 100%)"
    st.markdown(f"""
        <style>
            .stApp {{
                background: {bg_gradient};
                animation: fadeIn 1.2s ease;
            }}
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: scale(.985); }}
                to   {{ opacity: 1; transform: scale(1); }}
            }}
        </style>
    """, unsafe_allow_html=True)

    conn = mysql.connector.connect(host='localhost', user='<user>', password='<password>', database='db_name')
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
