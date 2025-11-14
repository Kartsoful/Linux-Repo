import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Investment Profit Scatter Plot")

    # Lue tiedosto OIKEIN: uusi nimi, sep=';' ja decimal=',' desimaaleille
    try:
        df = pd.read_csv('investmentProfit.csv', sep=';', decimal=',')
    except FileNotFoundError:
        st.error("Tiedostoa 'investmentProfit.csv' ei löytynyt! Varmista, että se on samassa kansiossa.")
        return

    # Debuggaus: Näytä sarakkeet ja data (poista myöhemmin jos ei tarvita)
    st.subheader("Ladattu data (ensimmäiset rivit)")
    st.write("Sarakkeet:", df.columns.tolist())
    st.dataframe(df.head(10))

    # Tarkista x-sarake
    if 'sijoitettuPaaoma' not in df.columns:
        st.error("Saraketta 'sijoitettuPaaoma' ei löytynyt! Tarkista nimi ylläolevasta listasta.")
        return

    # Valitse y-sarake: Tuotto-sarakkeet (kuten '0,01')
    tuotto_sarakkeet = [col for col in df.columns if col.startswith('0,')]
    if not tuotto_sarakkeet:
        st.error("Tuotto-sarakkeita ei löytynyt! Tarkista data.")
        return

    selected_y = st.selectbox("Valitse tuotto-sarake y-akselille (esim. 0,01 %):", tuotto_sarakkeet, index=0)

    # Valinnainen: Suodata kk (kuukaudet) -sarakkeella
    selected_kk = st.slider("Suodata kuukaudet (kk):", min_value=0, max_value=df['kk'].max() if 'kk' in df.columns else 0, value=0)

    # Tarkista valittu y-sarake
    if selected_y not in df.columns:
        st.error(f"Saraketta '{selected_y}' ei löytynyt!")
        return

    # Poista NaN-rivit ja suodata kk
    df_plot = df.dropna(subset=['sijoitettuPaaoma', selected_y])
    if 'kk' in df.columns:
        df_plot = df_plot[df_plot['kk'] >= selected_kk]

    # Korjattu scatter-plot
    fig = px.scatter(df_plot, x='sijoitettuPaaoma', y=selected_y,
                     title=f'Tuotto vs. Sijoitettu Pääoma ({selected_y} tuotto, kk >= {selected_kk})',
                     labels={'sijoitettuPaaoma': 'Sijoitettu Pääoma', selected_y: 'Tuotto', 'kk': 'Kuukaudet'})
    st.plotly_chart(fig, use_container_width=True)

    # Bonus: Line chart 'kk' vs. tuotto (jos haluat aikajanaa)
    if 'kk' in df.columns and len(df_plot) > 1:
        st.subheader("Tuotto aikajanalla (line chart)")
        fig_line = px.line(df_plot, x='kk', y=selected_y, color='sijoitettuPaaoma',
                           title=f'Tuotto kehitys kuukausittain ({selected_y})')
        st.plotly_chart(fig_line, use_container_width=True)

if __name__ == "__main__":
    main()