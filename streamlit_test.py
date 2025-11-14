import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Investment Profit Scatter Plot")

    # Lue tiedosto (sep=';' ja decimal=',' eurooppalaiselle formaatille)
    df = pd.read_csv('investment_profit.csv', sep=';', decimal=',')

    # Debuggaus: Näytä sarakkeet ja data
    st.subheader("Ladattu data (ensimmäiset rivit)")
    st.write("Sarakkeet:", df.columns.tolist())
    st.dataframe(df.head())

    # Tarkista x-sarake
    if 'SijoitettuPaaoma' not in df.columns:
        st.error("Saraketta 'SijoitettuPaaoma' ei löytynyt! Tarkista nimi: " + str(df.columns))
        return

    # Valitse y-sarake (tuotto): Listaa saatavilla olevat tuotto-sarakkeet
    tuotto_sarakkeet = [col for col in df.columns if col.startswith('0,')]
    if not tuotto_sarakkeet:
        st.error("Yhtään tuotto-saraketta (kuten '0,01') ei löytynyt!")
        return

    selected_y = st.selectbox("Valitse tuotto-sarake y-akselille:", tuotto_sarakkeet, index=0)

    # Tarkista valittu y-sarake
    if selected_y not in df.columns:
        st.error(f"Saraketta '{selected_y}' ei löytynyt!")
        return

    # Korjattu scatter-plot: x = SijoitettuPaaoma, y = valittu tuotto
    fig = px.scatter(df, x='SijoitettuPaaoma', y=selected_y, 
                     title=f'Tuotto vs. Sijoitettu Pääoma ({selected_y} % tuotto)')
    fig.update_layout(xaxis_title='Sijoitettu Pääoma', yaxis_title='Tuotto')
    st.plotly_chart(fig)

    # Jos haluat poistaa NaN-arvot (jos dataa puuttuu), lisää ennen plottausta:
    # df_plot = df.dropna(subset=['SijoitettuPaaoma', selected_y])
    # fig = px.scatter(df_plot, ...)

if __name__ == "__main__":
    main()