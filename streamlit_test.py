import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Investment Profit Scatter Plot")

    # Lue tiedosto OIKEIN: sep=';' erottimelle, decimal=',' desimaaleille
    try:
        df = pd.read_csv('investment_profit.csv', sep=';', decimal=',')
    except FileNotFoundError:
        st.error("Tiedostoa 'investment_profit.csv' ei löytynyt! Varmista, että se on samassa kansiossa.")
        return

    # Debuggaus: Näytä sarakkeet ja data (poista myöhemmin jos ei tarvita)
    st.subheader("Ladattu data (ensimmäiset rivit)")
    st.write("Sarakkeet:", df.columns.tolist())
    st.dataframe(df.head(10))

    # Tarkista x-sarake (täsmää errorisi otsikkoon)
    if 'sijoitettuPaaoma' not in df.columns:
        st.error("Saraketta 'sijoitettuPaaoma' ei löytynyt! Tarkista nimi ylläolevasta listasta.")
        return

    # Valitse y-sarake: Tuotto-sarakkeet (kuten '0,01')
    tuotto_sarakkeet = [col for col in df.columns if col.startswith('0,')]
    if not tuotto_sarakkeet:
        st.error("Tuotto-sarakkeita ei löytynyt! Tarkista data.")
        return

    selected_y = st.selectbox("Valitse tuotto-sarake y-akselille (esim. 0,01 %):", tuotto_sarakkeet, index=0)

    # Tarkista valittu y-sarake
    if selected_y not in df.columns:
        st.error(f"Saraketta '{selected_y}' ei löytynyt!")
        return

    # Poista NaN-rivit, jos dataa puuttuu (valinnainen)
    df_plot = df.dropna(subset=['sijoitettuPaaoma', selected_y])

    # Korjattu scatter-plot
    fig = px.scatter(df_plot, x='sijoitettuPaaoma', y=selected_y,
                     title=f'Tuotto vs. Sijoitettu Pääoma ({selected_y} tuotto)',
                     labels={'sijoitettuPaaoma': 'Sijoitettu Pääoma', selected_y: 'Tuotto'})
    st.plotly_chart(fig, use_container_width=True)

    # Jos haluat lisätä 'Amount'-sarakkeen (esim. summa tuotoista)
    # df['Amount'] = df[tuotto_sarakkeet].sum(axis=1)
    # Sitten voit käyttää y='Amount' valikossa

if __name__ == "__main__":
    main()