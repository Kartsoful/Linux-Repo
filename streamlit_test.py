import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Plot some data")
    df = pd.read_csv("Electric_prices.csv", sep=",")
    ff = px.scatter(df, x="Date", y="Price")
    st.plotly_chart(ff, use_container_width=True)

if __name__ == "__main__":
    main()