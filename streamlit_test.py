import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Electric price - Test")

    # Lue data
    df = pd.read_csv("Electric_prices.csv", sep=",")

    # Siivoa otsikot: poista mahdolliset ; ja välilyönnit alusta/lopusta
    df.columns = [c.strip().replace(";", "") for c in df.columns]

    # Näytä debugina mitä sarakkeita oikeasti on
    st.write("Sarakkeet:", list(df.columns))

    # Oletus: Date = x-akseli, kaikki muut sarakkeet (esim. Paaoma, 2%, 4%, 6%) = viivat
    y_cols = [c for c in df.columns if c != "Aika [kk]"]

    fig = px.line(
        df,
        x="Aika [kk]",
        y=y_cols,
        markers=True,
        title="Trendiviivat"
    )

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
