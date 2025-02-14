import streamlit as st

# URL do dashboard Looker Studio (substitua com o seu link de incorporação)
looker_url = 'https://lookerstudio.google.com/embed/reporting/7c7bf319-9e22-4610-9100-58a930eb142c/page/UgY7D'

# Código HTML com iframe para incorporar o painel
html_code = f"""
<iframe src="{looker_url}" width="90%" height="800" frameborder="0" style="border:0" allowfullscreen></iframe>
"""

# Inserir o código HTML no Streamlit usando markdown
st.markdown(html_code, unsafe_allow_html=True)