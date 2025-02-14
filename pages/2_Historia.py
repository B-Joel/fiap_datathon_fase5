import streamlit as st

st.title("História - Passos Mágicos")

st.markdown("""
A **Associação Passos Mágicos** possui uma trajetória de **30 anos de atuação**, dedicando-se à transformação da vida de crianças e jovens de baixa renda, proporcionando-lhes melhores oportunidades para o futuro.

A transformação, idealizada por **Michelle Flues** e **Dimetri Ivanoff**, teve início em **1992**, com atuação dentro de orfanatos no município de **Embu-Guaçu**.

Em **2016**, após anos de dedicação e impacto positivo, decidiram ampliar o programa para que um maior número de jovens tivesse acesso a essa **fórmula mágica de transformação**, baseada em:

- **Educação de qualidade**;
- **Auxílio psicológico e psicopedagógico**;
- **Ampliação da visão de mundo**;
- **Desenvolvimento do protagonismo juvenil**.

Foi então que o projeto evoluiu, tornando-se um programa social e educacional estruturado: nasceu a **Associação Passos Mágicos**.

### Missão e Visão

**Missão**

Transformar a vida de jovens e crianças, oferecendo ferramentas para levá-los a melhores oportunidades de vida.

**Visão**

Viver em um Brasil no qual todas as crianças e jovens tenham iguais oportunidades para realizarem seus sonhos e sejam agentes transformadores de suas próprias vidas.
""")


video_url = 'https://www.youtube.com/embed/36ZfZQa68og?feature=oembed'
st.video(video_url)

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
        }

        .custom-button:hover {
            background-color: #92B8D7; /* Cor ao passar o mouse, azul um pouco mais escuro */
            transform: scale(1.05);
        }

        .custom-button:active {
            background-color: #7A97B1; /* Cor ao pressionar, azul mais forte */
            transform: scale(0.98);
        }
    </style>
""", unsafe_allow_html=True)



# Botão com link
st.markdown('<a href="https://passosmagicos.org.br/" target="_blank" class="custom-button">Passos Mágicos, acesso em 10 de fevereiro de 2025</a>', unsafe_allow_html=True)