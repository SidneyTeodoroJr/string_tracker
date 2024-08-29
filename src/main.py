import streamlit as st
from tabela import criar_tabela_e_preencher

def main():
    st.title('Criação de Tabela de string tracker')

    # Upload do arquivo TXT
    uploaded_file = st.file_uploader("Escolha um arquivo de texto", type="txt")

    if uploaded_file:
        # Exibir as opções para o usuário
        inicio_tracker = st.number_input('Início do Tracker (ex: 22):', min_value=1, value=22)
        num_trackers = st.number_input('Quantidade de Trackers:', min_value=1, value=35)
        placas_por_tracker = st.number_input('Quantas Placas por Tracker:', min_value=1, value=90)

        if st.button('Criar Tabela'):
            # Criar e salvar a tabela
            caminho_txt = uploaded_file.name
            with open(caminho_txt, 'wb') as f:
                f.write(uploaded_file.getvalue())
                
            df_criado = criar_tabela_e_preencher(caminho_txt, inicio_tracker, num_trackers, placas_por_tracker)
            st.success('A tabela foi criada com sucesso!')

            # Exibir o DataFrame na interface
            st.dataframe(df_criado)

            # Botão de download para o arquivo Excel
            st.download_button(label='Baixar o arquivo Excel', data=open('tabela_criada.xlsx', 'rb').read(), file_name='tabela_criada.xlsx')

if __name__ == "__main__":
    main()