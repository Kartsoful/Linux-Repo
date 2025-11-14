import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Electric price - Test")
    df = pd.read_csv("Electric_prices.csv", sep=",")
    ff = px.scatter(df, x="Date", y=["Paaoma", "2%", "4%", "6%"])
    st.plotly_chart(ff, use_container_width=True)

if __name__ == "__main__":
    main()