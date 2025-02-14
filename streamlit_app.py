import streamlit as st
import matplotlib.pyplot as plt

# Carregamento de imagens por cach
@st.cache_data
def load_img(img):
    return plt.imread(img)

# Configuração inicial
st.set_page_config(page_title="Datathon", 
                   page_icon=":house:", 
                   layout="wide",
)

# Exibir logotipo
st.image(load_img('images/logo.png'))


# Cabeçalho
with st.container():
    st.title("Bem-vindo(a)")
    st.title("Fase 5 - Datathon: ONG Passos Mágicos")
    
# Informações dos integrantes
with st.container():
    st.write("---")
    st.subheader("Grupo 66 - Integrantes:")
    st.markdown(
        """
        - **rm356228** - Joel Pedro Bellatto  
        - **rm356366** - Pedro de Almeida Matos  
        - **rm349836** - Micael Silva Lemos  
        - **rm355565** - Nathalia Alves da Silva Lima
        """
    )