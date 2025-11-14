import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Investment Profit Trend Lines: Aika vs. Tuotto")

    # Lue tiedosto OIKEIN: nimi 'investmentProfit.csv', sep=';' ja decimal=','
    try:
        df = pd.read_csv('investmentProfit.csv', sep=';', decimal=',')
    except FileNotFoundError:
        st.error("Tiedostoa 'investmentProfit.csv' ei löytynyt! Varmista sijainti.")
        return

    # Debuggaus: Näytä sarakkeet ja data (tarkista täältä nimi!)
    st.subheader("Ladattu data (ensimmäiset rivit)")
    st.write("Sarakkeet:", df.columns.tolist())  # Kopioi nimi täältä, jos herja!
    st.dataframe(df.head(10))

    # Tarkista x-sarake (aika: 'kk')
    if 'kk' not in df.columns:
        st.error("Saraketta 'kk' (aika) ei löytynyt! Tarkista lista yllä.")
        return

    # Tarkista 'sijoitettuPaaoma' (jos tarvitset myöhemmin, esim. väreihin)
    if 'sijoitettuPaaoma' not in df.columns:
        st.error("Saraketta 'sijoitettuPaaoma' ei löytynyt! Tarkista nimi ylläolevasta listasta.")
        return

    # Hae tuotto-sarakkeet (y-akselin viivat)
    tuotto_sarakkeet = [col for col in df.columns if col.startswith('0,')]
    if not tuotto_sarakkeet:
        st.error("Tuotto-sarakkeita ei löytynyt! Tarkista data.")
        return

    # Valitse mitkä viivat piirretään (multi-select: kaikki oletuksena)
    selected_tuotto = st.multiselect("Valitse tuotto-viivat (y-akseli):", tuotto_sarakkeet, default=tuotto_sarakkeet)

    if not selected_tuotto:
        st.warning("Valitse ainakin yksi tuotto-sarake!")
        return

    # Poista NaN-rivit relevanttien sarakkeiden osalta
    df_plot = df.dropna(subset=['kk'] + selected_tuotto)

    # Line chart: x='kk' (aika), y=selected_tuotto (useita viivoja), color='sijoitettuPaaoma' (värit pääoman mukaan)
    fig = px.line(df_plot, x='kk', y=selected_tuotto,
                  color='sijoitettuPaaoma',  # Värit viivoja eri pääomilla (jos haluat; poista jos ei)
                  title='Tuotto-trendit aikajanalla (x: kuukaudet, y: tuotto)',
                  labels={'kk': 'Kuukaudet (aika)', 'value': 'Tuotto-arvo', 'sijoitettuPaaoma': 'Pääoma-väri'})
    fig.update_layout(hovermode='x unified')  # Parempi hover-tieto
    st.plotly_chart(fig, use_container_width=True)

    # Tilastot bonus: Näytä keskiarvot valituille sarakkeille
    st.subheader("Keskiarvot valituille tuotoille")
    keskiarvot = df_plot[selected_tuotto].mean()
    st.bar_chart(keskiarvot)

if __name__ == "__main__":
    main()