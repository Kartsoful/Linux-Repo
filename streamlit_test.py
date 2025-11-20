import streamlit as st
import mysql.connector
import pandas as pd

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

def main():
    conn = mysql.connector.connect(host='localhost', user='kartso', password='kartso123', database='weather')
    df = pd.read_sql('SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 50',conn)
    conn.close()
    st.title('Säädata Helsingistä')
    st.dataframe(df)

    st.markdown("<h1>Helsingin lämpötilat MySQL-tietokannasta</h1>", unsafe_allow_html=True)
 
    # # Kaikki sarakkeet jotka eivät ole pvm tai id = paikkakuntia
    city_cols = [c for c in df.columns if c not in ('timestamp', 'id')]

    if not city_cols:
        st.error("Tietokannasta ei löytynyt yhtään kaupunkisaraketta.")
        return

    # # Oletuksena Oulu jos löytyy, muuten kaikki
    # default_selection = ['Helsinki'] if 'Oulu' in city_cols else city_cols

    # selected = st.multiselect(
    #     "Valitse kaupungit:",
    #     options=city_cols,
    #     default=default_selection,
    # )

    # # Oletusgradientti (jos aiempaa ei ole tallessa)
    # default_gradient = "linear-gradient(135deg, #0a0f24 0%, #1a2a6c 50%, #3d9ecf 100%)"

    # # Jos jotain valittu → laske keskiarvo ja gradientti
    # if selected:
    #     avg_temp = df[selected].stack().mean()

    #     if avg_temp <= 3:
    #         bg_gradient = "linear-gradient(135deg, #001f3f 0%, #003f7f 40%, #0074d9 100%)"
    #         label = "Kylmä"
    #     elif avg_temp <= 8:
    #         bg_gradient = "linear-gradient(135deg, #1a2a6c 0%, #3d5afe 40%, #00bcd4 100%)"
    #         label = "Viileä"
    #     else:
    #         bg_gradient = "linear-gradient(135deg, #7b1fa2 0%, #ff7043 40%, #ff9800 100%)"
    #         label = "Lämmin"

    #     # Talleta viimeisin gradientti ja label sessioon
    #     st.session_state["last_bg_gradient"] = bg_gradient
    #     st.session_state["last_label"] = label
    #     st.session_state["last_avg"] = avg_temp
    # else:
    #     st.warning("Valitse vähintään yksi kaupunki.")
    #     # Käytä viimeksi talletettua gradienttia, tai oletusta jos ei ole
    #     bg_gradient = st.session_state.get("last_bg_gradient", default_gradient)
    #     label = st.session_state.get("last_label", None)
    #     avg_temp = st.session_state.get("last_avg", None)

    # # Aina: aseta tausta viimeisimmän gradientin mukaan
    # st.markdown(f"""
    #     <style>
    #         .stApp {{
    #             background: {bg_gradient};
    #             color: white;
    #             transition: background 1.2s ease-in-out;
    #         }}
    #     </style>
    # """, unsafe_allow_html=True)

    # # Näytä keskiarvo vain jos se on laskettu
    # if selected and avg_temp is not None:
    #     st.markdown(
    #         f"<p style='text-align:center; font-size:18px; margin-top:5px;'>"
    #         f"Valittujen kaupunkien keskilämpötila: <b>{avg_temp:.1f} °C</b> ({label})"
    #         f"</p>",
    #         unsafe_allow_html=True,
    #     )

    # # Jos mitään ei valittu → ei piirretä kuvaa
    # if not selected:
    #     return

    # # Piirrä kuvaaja
    # fig = px.line(
    #     df,
    #     x="pvm",
    #     y=selected,
    #     markers=True,
    #     title="Vuorokauden keskilämpötila",
    #     template="plotly_dark",
    # )

    # fig.update_layout(
    #     xaxis_title="Päivämäärä",
    #     yaxis_title="Lämpötila (°C)",
    #     legend_title="Kaupunki",
    # )

    # st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
