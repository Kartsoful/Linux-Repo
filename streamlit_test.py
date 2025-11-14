import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Electric price - Test")

    # Lue CSV
    df = pd.read_csv("Electric_prices.csv", sep=",")

    # Siivoa sarakeotsikoista puolipisteet pois
    df.columns = [c.replace(";", "") for c in df.columns]

    # Tarkista mitä sarakkeita oikeasti on (debug)
    st.write("Columns:", list(df.columns))

    # Jos sarakkeet ovat Paaoma, 2%, 4%, 6%, piiretään ne
    fig = px.line(
        df,
        x="Date",
        y=["Paaoma", "2%", "4%", "6%"],  # monta trendiviivaa
        markers=True,
    )

    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
