import streamlit as st
import pandas as pd
import plotly.express as px
import time

from automation.excel_reader import ExcelReader


st.set_page_config(
    page_title="Nexus ESG",
    layout="wide"
)

reader = ExcelReader()

# AUTO REFRESH
placeholder = st.empty()

while True:

    df = reader.carregar_dados()

    with placeholder.container():

        st.title(
            "Nexus ESG Intelligence"
        )

        st.caption(
            "Monitoramento inteligente em tempo real"
        )

        # KPIs
        c1, c2, c3 = st.columns(3)

        energia = df["Energia"].mean()

        co2 = df["CO2"].mean()

        agua = df["Água"].mean()

        c1.metric(
            "Energia",
            f"{energia:.1f}%"
        )

        c2.metric(
            "CO₂",
            f"{co2:.1f}%"
        )

        c3.metric(
            "Água",
            f"{agua:.1f}%"
        )

        # GRÁFICO
        fig = px.line(
            df,
            x="Mes",
            y=[
                "Energia",
                "CO2",
                "Água"
            ],
            markers=True
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # TABELA
        st.dataframe(
            df,
            use_container_width=True
        )

    time.sleep(5)