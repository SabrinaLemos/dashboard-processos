⸻

1. Conteúdo do pacote

* app.py – aplicação principal desenvolvida em Python utilizando Streamlit.
* requirements.txt – dependências necessárias para execução.
* README.md – documentação do projeto.
* assets/ – recursos adicionais do sistema.
* dados/ – arquivos utilizados para alimentação do dashboard (quando aplicável).

2. Esquema de diretórios

aether_esg_intelligence/

│── app.py
│── requirements.txt
│── README.md
│
├── assets/
│
├── dados/
│
└── imagens/

3. Pré-requisitos

* Python 3.11 ou superior;
* Bibliotecas:
    * Streamlit
    * Pandas
    * Plotly
* Sistema operacional Windows, Linux ou macOS;
* Navegador web atualizado.

⸻

4. Como executar o dashboard

1. Entrar na pasta do projeto;

2. Instalar as dependências:
pip install -r requirements.txt

3. Executar a aplicação:
streamlit run app.py

4. Acessar:
http://localhost:8501

5. Módulos disponíveis

Overview

Painel principal contendo:

* Eficiência Energética;
* Emissões de CO₂;
* Automação ESG;
* Score Global ESG;
* Alertas inteligentes;
* Gráficos analíticos.

Analytics IA

Responsável pela análise inteligente dos indicadores e previsões.

Indicadores:

* Precisão da IA;
* Previsão de economia;
* Risco ambiental.

Automações

Monitoramento de processos automatizados.

Indicadores:

* Processos automatizados;
* Alertas resolvidos;
* Tempo economizado.

ESG Score

Módulo responsável pela avaliação global de conformidade ESG.

Relatórios

Área destinada ao acompanhamento e geração de relatórios corporativos

6. Base de dados utilizada

A versão atual utiliza uma base simulada em Pandas contendo:

Mês

Eficiência Energética (%)

Emissões de CO₂ (%)

7. Tecnologias utilizadas

* Python
* Streamlit
* Pandas
* Plotly
* HTML
* CSS

⸻

8. Decisões técnicas adotadas

* Utilização do Streamlit para acelerar o desenvolvimento da interface;
* Plotly empregado para criação de gráficos interativos;
* Pandas utilizado para manipulação e tratamento dos dados;
* Interface construída com tema escuro e componentes personalizados em CSS;
* Arquitetura modular dividida em cinco áreas principais;
* Sistema desenvolvido inicialmente sem dependência de APIs externas.

⸻

9. Implementações futuras sugeridas

* Integração com banco de dados SQL;
* Upload de planilhas Excel;
* APIs externas;
* Atualização em tempo real via WebSocket;
* Sistema de autenticação e perfis de usuário;
* Deploy em nuvem;
* Machine Learning para análise preditiva;
* Exportação automática de relatórios em PDF;
* Integração com Power BI.

10. Autores

Projeto desenvolvido para fins acadêmicos e de monitoramento corporativo. Sabrina lemos e Vitor Hugo.

Aether ESG Intelligence © 2026
