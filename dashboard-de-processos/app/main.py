import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Aether ESG Intelligence",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
html, body, [class*="css"] {
    background-color: #070B14;
    color: white;
    font-family: 'Segoe UI';
}

.main {
    background: linear-gradient(135deg, #070B14 0%, #0D1321 40%, #111827 100%);
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
    background: linear-gradient(145deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
    border-radius: 22px;
    padding: 25px;
    border: 1px solid rgba(255,255,255,0.06);
    transition: 0.3s;
}

.kpi-card:hover {
    transform: translateY(-5px);
    border: 1px solid #00FFA3;
}

.kpi-title {
    font-size: 15px;
    color: #94A3B8;
}

.kpi-value {
    font-size: 42px;
    font-weight: bold;
    color: white;
}

.kpi-positive {
    color: #00FFA3;
    font-size: 15px;
}

.alert-box {
    background: linear-gradient(90deg, rgba(0,255,163,0.15), rgba(0,255,163,0.02));
    border-left: 4px solid #00FFA3;
    padding: 18px;
    border-radius: 16px;
}
</style>
""", unsafe_allow_html=True)

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

dados = pd.DataFrame({
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago"],
    "Energia (%)": [12, 15, 18, 17, 21, 25, 28, 32],
    "CO₂ (%)": [40, 37, 34, 30, 26, 22, 19, 15]
})

def card_kpi(titulo, valor, texto):
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">{titulo}</div>
        <div class="kpi-value">{valor}</div>
        <div class="kpi-positive">{texto}</div>
    </div>
    """, unsafe_allow_html=True)

if pagina == "Overview":

    st.markdown('<div class="big-title">Aether ESG Intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Plataforma autônoma de sustentabilidade corporativa</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        card_kpi("Eficiência Energética", "94%", "▲ +12% este mês")

    with c2:
        card_kpi("Emissões CO₂", "-31%", "▲ redução sustentável")

    with c3:
        card_kpi("Automação ESG", "87%", "▲ processos inteligentes")

    with c4:
        card_kpi("ESG Score Global", "91%", "▲ conformidade máxima")

    st.write("")

    col1, col2 = st.columns([2, 1])

    with col1:
        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=dados["Mês"],
            y=dados["Energia (%)"],
            mode="lines+markers",
            name="Eficiência Energética"
        ))

        fig.add_trace(go.Scatter(
            x=dados["Mês"],
            y=dados["CO₂ (%)"],
            mode="lines+markers",
            name="CO₂"
        ))

        fig.update_layout(
            title="Análise Inteligente ESG",
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            font=dict(color="white"),
            height=450,
            yaxis=dict(title="Porcentagem (%)")
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:
        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=91,
            number={"suffix": "%"},
            title={"text": "ESG Compliance"},
            gauge={"axis": {"range": [0, 100]}}
        ))

        gauge.update_layout(
            paper_bgcolor="#111827",
            font=dict(color="white"),
            height=450
        )

        st.plotly_chart(gauge, use_container_width=True)

    st.markdown("""
    <div class="alert-box">
        <b>IA Corporativa:</b>
        Detectamos uma oportunidade de otimização energética de 18% no setor industrial sul.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Análise Estratégica")
    st.dataframe(dados, use_container_width=True)

elif pagina == "Analytics IA":

    st.title("Analytics IA")
    st.write("Aqui ficará a análise inteligente baseada em IA.")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Precisão da IA", "89%", "+7%")

    with c2:
        st.metric("Previsão de Economia", "23%", "+5%")

    with c3:
        st.metric("Risco Ambiental", "14%", "-9%")

    st.dataframe(dados, use_container_width=True)

elif pagina == "Automações":

    st.title("Automações ESG")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Processos Automatizados", "87%", "+10%")

    with c2:
        st.metric("Alertas Resolvidos", "76%", "+8%")

    with c3:
        st.metric("Tempo Economizado", "42%", "+12%")

elif pagina == "ESG Score":

    st.title("ESG Score")

    st.metric(
        label="Pontuação ESG Global",
        value="91%",
        delta="+12%"
    )

    gauge_score = go.Figure(go.Indicator(
        mode="gauge+number",
        value=91,
        number={"suffix": "%"},
        title={"text": "Score ESG"},
        gauge={"axis": {"range": [0, 100]}}
    ))

    gauge_score.update_layout(
        paper_bgcolor="#111827",
        font=dict(color="white"),
        height=450
    )

    st.plotly_chart(gauge_score, use_container_width=True)

elif pagina == "Relatórios":

    st.title("Relatórios")
    st.write("Aqui ficarão os relatórios corporativos.")

    st.metric("Relatórios Gerados", "64%", "+15%")
    st.metric("Conformidade Documental", "92%", "+6%")

st.write("")
st.caption("Aether ESG Intelligence © 2026")