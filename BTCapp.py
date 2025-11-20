import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px

# ---------- PERUS-TYYLIT (staattinen osa) ----------
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Roboto+Mono:wght@400;500&display=swap');

        .stApp {
            font-family: 'Inter', sans-serif;
        }

        /* Glass container */
        .block-container {
            max-width: 980px;
            padding: 48px 56px 56px 56px;
            margin-top: 40px;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.18);
            border-radius: 22px;
            backdrop-filter: blur(14px) saturate(140%);
            box-shadow: 0 12px 32px -8px rgba(0,0,0,0.55);
        }

        h1, h2, h3, h4 {
            font-weight: 700;
            letter-spacing: 0.5px;
            background: linear-gradient(90deg,#ffddb7,#ffd37c,#ff9e7a,#ff6f91);
            -webkit-background-clip: text;
            color: transparent !important;
            text-align: center;
            margin-top: 0.75rem;
            margin-bottom: 1.25rem;
        }

        p, label, span {
            color: #f5f7fa !important;
        }

        /* Buttons */
        div.stButton > button {
            background: linear-gradient(135deg,#3d5afe 0%,#00bcd4 100%);
            color: #fff;
            border: none;
            padding: 0.65rem 1.2rem;
            font-weight: 600;
            border-radius: 10px;
            transition: transform .15s ease, box-shadow .15s ease;
        }
        div.stButton > button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 24px -6px rgba(0,188,212,.45);
        }
        div.stButton > button:active {
            transform: translateY(0);
            box-shadow: 0 4px 14px -4px rgba(0,188,212,.35);
        }

        /* Alerts */
        .stAlert {
            background: rgba(0,0,0,0.55) !important;
            border-radius: 14px;
            border: 1px solid rgba(255,255,255,0.2);
        }

        /* DataFrame tweaks */
        .stDataFrame, .stTable {
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 6px 18px -4px rgba(0,0,0,0.5);
        }
        .stDataFrame [data-testid="styled-table"] tbody tr:hover {
            background: rgba(255,255,255,0.07);
        }

        /* Plotly card feel */
        .plot-container {
            border-radius: 18px !important;
            background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.06), rgba(0,0,0,0.55));
            padding: 12px;
        }

        /* Scrollbar */
        ::-webkit-scrollbar { width: 10px; }
        ::-webkit-scrollbar-track { background: rgba(255,255,255,0.05); }
        ::-webkit-scrollbar-thumb { background: linear-gradient(180deg,#3d5afe,#00bcd4); border-radius: 20px; }

        /* Fade-in */
        .block-container, h1, h2, h3, h4, .stDataFrame {
            animation: fadeIn .7s ease;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(12px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
""", unsafe_allow_html=True)

def main():
    bg_gradient = "linear-gradient(125deg,#0f172a 0%,#16253d 35%,#003b54 65%,#005e79 100%)"
    st.markdown(f"""
        <style>
            .stApp {{
                background: {bg_gradient};
                color: white;
                min-height: 100vh;
                background-attachment: fixed;
            }}
        </style>
    """, unsafe_allow_html=True)

    conn = mysql.connector.connect(host='localhost', user='<user>', password='<pass>', database='db_name')
    df = pd.read_sql('SELECT * FROM crypto_prices ORDER BY timestamp',conn)
    conn.close()
    st.title('BTC hintakehitys')    
    st.markdown("<h4>Dataa kerätty 20.11.2025 19:40 UTC+2 alkaen. Näytteenkeruuväli 10min</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:0.85rem; opacity:0.75;'>Näytteenkeruu voi loppua, jos API-rajapinnan käyttörajat tulee vastaan. Näin ei pitäisi kuitenkaan käydä</p>", unsafe_allow_html=True)
    st.dataframe(df)

    st.markdown("<h1>Kerätty BTC:n hintakehitys</h1>", unsafe_allow_html=True)
 
    # # Kaikki sarakkeet jotka eivät ole pvm tai id = paikkakuntia
    cols = [c for c in df.columns if c not in ('timestamp', 'id')]

    if not cols:
        st.error("Tietokannasta ei löytynyt yhtään hintasaraketta.")
        return

    # Piirrä kuvaaja
    fig = px.line(
        df,
        x="timestamp",
        y="price_usd",
        markers=True,
        title="Hinta [USD]",
        template="plotly_dark",
    )

    fig.update_layout(
        xaxis_title="Päivämäärä",
        yaxis_title="Hinta [USD]",
        legend_title="BTC",
    )

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
