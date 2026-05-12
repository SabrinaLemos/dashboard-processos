import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ==================================================
# CONFIG
# ==================================================

st.set_page_config(
    page_title="Aether ESG Intelligence",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# CSS
# ==================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #070B14;
    color: white;
    font-family: 'Segoe UI';
}

.main {
    background: linear-gradient(
        135deg,
        #070B14 0%,
        #0D1321 40%,
        #111827 100%
    );
}

section[data-testid="stSidebar"] {
    background: #050816;
    border-right: 1px solid rgba(255,255,255,0.08);
}

.big-title {
    font-size: 42px;
    font-weight: 700;
    color: white;
}

.subtitle {
    color: #94A3B8;
    font-size: 18px;
    margin-bottom: 20px;
}

.kpi-card {
    background: linear-gradient(
        145deg,
        rgba(255,255,255,0.06),
        rgba(255,255,255,0.02)
    );

    border-radius: 22px;
    padding: 25px;

    border: 1px solid rgba(255,255,255,0.06);

    transition: 0.3s;

    min-height: 180px;
}

.kpi-card:hover {
    transform: translateY(-5px);
    border: 1px solid #00FFA3;
}

.kpi-title {
    font-size: 15px;
    color: #94A3B8;
    margin-bottom: 20px;
}

.kpi-value {
    font-size: 42px;
    font-weight: bold;
    color: white;
    margin-bottom: 15px;
}

.kpi-positive {
    color: #00FFA3;
    font-size: 15px;
}

.alert-box {
    background: linear-gradient(
        90deg,
        rgba(0,255,163,0.15),
        rgba(0,255,163,0.02)
    );

    border-left: 4px solid #00FFA3;

    padding: 18px;

    border-radius: 16px;
}

[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.markdown("# AETHER ESG")

pagina = st.sidebar.radio(
    "Módulos",
    [
        "Overview",
        "Analytics IA",
        "Automações",
        "ESG Score",
        "Relatórios"
    ]
)

st.sidebar.markdown("---")
st.sidebar.success("Sistema Operacional")

# ==================================================
# DATA
# ==================================================

dados = pd.DataFrame({
    "Mes": [
        "Jan",
        "Fev",
        "Mar",
        "Abr",
        "Mai",
        "Jun",
        "Jul",
        "Ago"
    ],

    "Energia": [
        12,
        15,
        18,
        17,
        21,
        25,
        28,
        32
    ],

    "CO2": [
        40,
        37,
        34,
        30,
        26,
        22,
        19,
        15
    ]
})

# ==================================================
# OVERVIEW
# ==================================================

if pagina == "Overview":

    st.markdown(
        """
        <div class="big-title">
            Aether ESG Intelligence
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
            Plataforma autônoma de sustentabilidade corporativa
        </div>
        """,
        unsafe_allow_html=True
    )

    # ==================================================
    # KPI CARDS
    # ==================================================

    c1, c2, c3, c4 = st.columns(4)

    cards = [
        (
            "Eficiência Energética",
            "94%",
            "▲ +12% este mês"
        ),

        (
            "Emissões CO₂",
            "-31%",
            "▲ redução sustentável"
        ),

        (
            "Automação ESG",
            "87%",
            "▲ processos inteligentes"
        ),

        (
            "ESG Score Global",
            "AAA",
            "▲ conformidade máxima"
        )
    ]

    for col, card in zip(
        [c1, c2, c3, c4],
        cards
    ):

        titulo, valor, status = card

        with col:

            st.markdown(
                f"""
                <div class="kpi-card">

                    <div class="kpi-title">
                        {titulo}
                    </div>

                    <div class="kpi-value">
                        {valor}
                    </div>

                    <div class="kpi-positive">
                        {status}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.write("")

    # ==================================================
    # CHARTS
    # ==================================================

    col1, col2 = st.columns([2, 1])

    with col1:

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=dados["Mes"],
            y=dados["Energia"],
            mode="lines+markers",
            name="Eficiência",
            line=dict(width=4)
        ))

        fig.add_trace(go.Scatter(
            x=dados["Mes"],
            y=dados["CO2"],
            mode="lines+markers",
            name="CO₂",
            line=dict(width=4)
        ))

        fig.update_layout(
            title="Análise Inteligente ESG",
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            font=dict(color="white"),
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:

        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=91,

            title={
                "text": "ESG Compliance"
            },

            gauge={
                "axis": {
                    "range": [0, 100]
                }
            }
        ))

        gauge.update_layout(
            paper_bgcolor="#111827",
            font=dict(color="white"),
            height=450
        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    # ==================================================
    # ALERTA IA
    # ==================================================

    st.markdown(
        """
        <div class="alert-box">
            <b>IA Corporativa:</b>
            Detectamos uma oportunidade de otimização energética
            de 18% no setor industrial sul.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # ==================================================
    # TABELA
    # ==================================================

    st.subheader("Análise Estratégica")

    st.dataframe(
        dados,
        use_container_width=True
    )

# ==================================================
# ANALYTICS IA
# ==================================================

elif pagina == "Analytics IA":

    st.title("Analytics IA")

    st.write(
        "Aqui ficará a análise inteligente baseada em IA."
    )

    st.dataframe(
        dados,
        use_container_width=True
    )

# ==================================================
# AUTOMAÇÕES
# ==================================================

elif pagina == "Automações":

    st.title("Automações ESG")

    st.write(
        "Aqui ficarão os processos automatizados."
    )

# ==================================================
# ESG SCORE
# ==================================================

elif pagina == "ESG Score":

    st.title("ESG Score")

    st.metric(
        "Pontuação ESG Global",
        "91",
        "+12 pontos"
    )

# ==================================================
# RELATÓRIOS
# ==================================================

elif pagina == "Relatórios":

    st.title("Relatórios")

    st.write(
        "Aqui ficarão os relatórios corporativos."
    )

# ==================================================
# FOOTER
# ==================================================

st.write("")

st.caption(
    "Aether ESG Intelligence © 2026"
)