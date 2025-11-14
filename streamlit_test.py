import streamlit as st
import pandas as pd
import plotly.express as px
@st.cache_resource
def mySql():

    # Initialize connection.
    conn = st.connection('mysql', type='sql')
    # Perform query.
    df = conn.query('SELECT Oulu from lampotilat;', ttl=600)
    return df
# Streamlit


def main():
    st.title("Plot data from MySql")
    st.write("Lämpötiloja")
    data = mySql()
    #plot data

#     options = st.multiselect(
#     "Minkä kaupungin lämpötilat?",
#     ["Utsjoki", "Oulu", "Helsinki"],
#     default=["Oulu"],
# )

    df2 = pd.DataFrame(data, columns=["Oulu"])
    lampotila = px.line(df2, x=df2.index, y="Oulu")
    st.plotly_chart(lampotila, use_container_width=True)

if __name__ == "__main__":
    main()



# import streamlit as st
# import pandas as pd
# import plotly.express as px
# @st.cache_resource
# def mySql():

#     # Initialize connection.
#     conn = st.connection('mysql', type='sql')
#     # Perform query.
#     df = conn.query('SELECT TotalKg from powerlifting_28_12_24 LIMIT 100;', ttl=600)
#     return df
# # Streamlit
# def main():
#     st.title("Plot data from MySql")
#     st.write("TotalKg from powerlifting")
#     data = mySql()
#     #plot data
#     df2 = pd.DataFrame(data, columns=["TotalKg"])
#     totalKg = px.line(df2, x=df2.index, y="TotalKg")
#     st.plotly_chart(totalKg, use_container_width=True)
# if __name__ == "__main__":
#     main()