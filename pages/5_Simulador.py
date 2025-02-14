import streamlit as st
import pandas as pd
import numpy as np
import joblib
import ssl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from utils import Drop, OneHot, minMax

ssl._create_default_https_context = ssl._create_stdlib_context

#------------------------------------------------------------------------------------------
# Carregando o df
dados = pd.read_csv('dados/csv_tratado/dados_ML.csv')

#------------------------------------------------------------------------------------------
# Estilo personalizado para o botão
st.markdown("""
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            border-radius: 12px;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.write('## Simulador de Ponto de Virada')
st.markdown("""
    ### Ponto de Virada
    > "Passar pelo Ponto de Virada deve significar **estar apto a iniciar a transformação da sua vida por meio da educação**..."
    
    **PDE2020: Roteiro de Avaliação do Indicador de Ponto de Virada (IPV)**

    ### Simulador
    O simulador foi desenvolvido a partir da constatação de que apenas **14% dos estudantes** da instituição atingem o **Ponto de Virada**.
""")

st.divider()

#------------------------------------------------------------------------------------------
# Formulário
input_idade = int(st.slider('Selecione a idade do aluno', 7, 20, help="Idade atual do aluno para análise de adaptação e desenvolvimento"))
input_fase = int(st.slider('Selecione a fase em que o aluno está', 0, 8, help="Fase do aluno dentro do programa educacional"))
input_pedra = str(st.selectbox('Selecione a pedra do aluno:', 
                                ('Ametista', 'Quartzo', 'Topázio', 'Ágata'), help="Cada pedra representa uma fase do desenvolvimento do aluno"))
input_ian = float(st.slider('Selecione o Indicador de Adequação de Nível do aluno:', step=0.001, min_value=0.0, max_value=10.0))
input_ida = float(st.slider('Selecione o Indicador de Desempenho Acadêmico do aluno:', step=0.001, min_value=0.0, max_value=10.0))
input_ieg = float(st.slider('Selecione o Indicador de Engajamento do aluno:', step=0.001, min_value=0.0, max_value=10.0))
input_iaa = float(st.slider('Selecione o Indicador de Autoavaliação do aluno:', step=0.001, min_value=0.0, max_value=10.0))
input_ips = float(st.slider('Selecione o Indicador Psicossocial do aluno:', step=0.001, min_value=0.0, max_value=10.0))
input_ipp = float(st.slider('Selecione o Indicador Psicopedagógico do aluno:', step=0.001, min_value=0.0, max_value=10.0))
input_ipv = float(st.slider('Selecione o Indicador de Ponto de Virada do aluno:', step=0.001, min_value=0.0, max_value=10.0))
input_inde = float(st.slider('Selecione o Índice de Desenvolvimento Educacional do aluno:', step=0.001, min_value=0.0, max_value=10.0))
input_instituicao_ensino = str(st.selectbox('Selecione a Instituição de ensino do Aluno', ['Escola Pública', 'Escola Particular']))
escola_dict = {'Escola Pública': 0, 'Escola Particular': 1}
input_instituicao_ensino = escola_dict.get(input_instituicao_ensino)
input_anos_pm_2020 = int(st.slider('Selecione há quantos anos o aluno estuda na Passos Mágicos', 0, 5))

#------------------------------------------------------------------------------------------
# Função para plotar gráfico radar
def plot_radar(dados_aluno, indicadores):
    categorias = indicadores
    valores = dados_aluno

    angles = np.linspace(0, 2 * np.pi, len(categorias), endpoint=False).tolist()
    valores += valores[:1]  # Fechar o gráfico
    angles += angles[:1]  # Fechar o gráfico

    fig, ax = plt.subplots(figsize=(4, 4), dpi=120, subplot_kw=dict(polar=True))
    ax.fill(angles, valores, color='blue', alpha=0.25)
    ax.plot(angles, valores, color='blue', linewidth=2)
    ax.set_yticklabels([])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categorias, fontsize=12)

    st.pyplot(fig)

# Indicadores do aluno
indicadores = ['ian', 'ida', 'ieg', 'iaa', 'ips', 'ipp', 'ipv', 'inde']
dados_aluno = [input_ian, input_ida, input_ieg, input_iaa, input_ips, input_ipp, input_ipv, input_inde]

plot_radar(dados_aluno, indicadores)

#------------------------------------------------------------------------------------------
# Análise do aluno
novo_aluno = [input_idade, 
            input_fase,
            0,  # ponto_de_virada 
            input_pedra,
            input_ian, 
            input_ida, 
            input_ieg, 
            input_iaa, 
            input_ips, 
            input_ipp, 
            input_ipv, 
            input_inde,
            input_instituicao_ensino,
            input_anos_pm_2020
            ]

# Separando dados de treino e teste
SEED = np.random.seed(42)
dados_treino, dados_teste = train_test_split(dados, test_size=0.2, random_state=SEED)

# Criando df de novo aluno
novo_aluno_df = pd.DataFrame([novo_aluno], columns=dados.columns)

# Concatenando
dados_e_novo_aluno = pd.concat([dados_teste, novo_aluno_df], ignore_index=True)

#------------------------------------------------------------------------------------------
# Pipeline
def pipeline(dados):
    pipeline = Pipeline([
        ('DropFeatures', Drop()),
        ('OneHotEncoder', OneHot()),
        ('MinMaxScaler', minMax()),
    ])
    dados_pipeline = pipeline.fit_transform(dados)
    return dados_pipeline

# Aplicando a pipeline
dados_e_novo_aluno = pipeline(dados_e_novo_aluno)

# Retirando o target
pv_predito = dados_e_novo_aluno.drop(['ponto_de_virada'], axis=1)

#------------------------------------------------------------------------------------------
# Função para feedback visual instantâneo
def feedback_instantaneo():
    if input_ipv > 7:
        st.write("### O aluno tem boas chances de atingir o ponto de virada!")
    else:
        st.write("### O aluno pode precisar de mais suporte para atingir o ponto de virada.")

# Exibindo o feedback instantâneo
#feedback_instantaneo()

#------------------------------------------------------------------------------------------
# Estilo personalizado para as mensagens
st.markdown("""
    <style>
        .success-message {
            background-color: #A8D5BA; /* Verde suave para sucesso */
            color: #3C5C51; /* Texto em verde escuro */
            padding: 10px;
            border-radius: 8px;
            font-size: 16px;
            margin-top: 10px;
        }

        .error-message {
            background-color: #F4D03F; /* Amarelo suave para erro */
            color: #6C4F35; /* Texto em marrom escuro */
            padding: 10px;
            border-radius: 8px;
            font-size: 16px;
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Estilo personalizado para o botão
st.markdown("""
    <style>
        .custom-button {
            background-color: #A9C9E1; /* Azul claro suave */
            color: #2F3A45; /* Texto em azul escuro */
            font-size: 16px;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            border-radius: 8px;
            display: inline-block;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
        }

        .custom-button:hover {
            background-color: #92B8D7; /* Azul um pouco mais escuro */
            transform: scale(1.05); /* Efeito de crescimento suave */
        }

        .custom-button:active {
            background-color: #7A97B1; /* Azul mais forte ao pressionar */
            transform: scale(0.98); /* Efeito de redução ao pressionar */
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .box {
            background-color: #f0f4f8; /* Fundo claro */
            border: 2px solid #d1e3f1; /* Borda suave */
            padding: 20px;
            border-radius: 8px;
            font-size: 14px;
            color: #2F3A45; /* Texto em azul escuro */
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Botão de envio com o estilo personalizado
if st.button('Enviar', key='enviar', help="Clique para submeter a análise", use_container_width=True):
    modelo = joblib.load('modelo/logistic_regression.joblib')
    predicao = modelo.predict(pv_predito)
    if predicao[-1] == 1:
        st.markdown('<div class="success-message">### Parabéns! Este aluno está no caminho certo para atingir o Ponto de Virada!</div>', unsafe_allow_html=True)
        st.markdown('<div class="box">O aluno está demonstrando ótimos sinais de progresso. Com o apoio contínuo da instituição, ele pode alcançar grandes conquistas e transformar sua vida por meio da educação!</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="error-message">### Atenção! Este aluno pode enfrentar desafios para atingir o Ponto de Virada.</div>', unsafe_allow_html=True)
        st.markdown('<div class="box">Embora o aluno tenha potencial, ele pode precisar de mais suporte nas áreas de engajamento e desempenho acadêmico. Vamos trabalhar juntos para ajudá-lo a superar essas dificuldades e alcançar seus objetivos!</div>', unsafe_allow_html=True)
