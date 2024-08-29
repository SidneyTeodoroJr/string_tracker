import pandas as pd

def ler_arquivo_txt(caminho_txt):
    """
    Função para ler o arquivo de texto com codificação adequada e remover espaços extras e linhas em branco.
    """
    codificacoes = ['utf-8', 'iso-8859-1', 'cp1252']
    for codificacao in codificacoes:
        try:
            with open(caminho_txt, 'r', encoding=codificacao) as file:
                linhas = [linha.strip() for linha in file if linha.strip()]
                return linhas
        except (UnicodeDecodeError, IOError) as e:
            print(f"Erro ao ler o arquivo com codificação {codificacao}: {e}")
    raise ValueError("Não foi possível ler o arquivo com nenhuma das codificações tentadas.")

def criar_tabela_e_preencher(caminho_txt, inicio_tracker, num_trackers, placas_por_tracker):
    """
    Cria um DataFrame com colunas 'TR22' a 'TR56' e preenche com códigos do arquivo txt.
    """
    # Carregar códigos do arquivo de texto
    codigos = ler_arquivo_txt(caminho_txt)
    
    # Definir parâmetros
    num_linhas = placas_por_tracker  # Número de linhas por coluna
    total_codigos_necessarios = num_trackers * num_linhas
    
    # Preencher com espaços em branco, se necessário
    if len(codigos) < total_codigos_necessarios:
        codigos.extend([''] * (total_codigos_necessarios - len(codigos)))
    
    # Criar DataFrame com colunas de acordo com a ordem de contagem
    colunas = [f"TR{num:02d}" for num in range(inicio_tracker, inicio_tracker + num_trackers)]
    
    # Criar um DataFrame vazio com as colunas especificadas e o número necessário de linhas
    df = pd.DataFrame(index=range(num_linhas), columns=colunas)

    # Preencher as colunas com os códigos
    for i, coluna in enumerate(colunas):
        df.loc[:, coluna] = codigos[i*num_linhas:(i+1)*num_linhas]
    
    # Salvar o DataFrame em um arquivo Excel
    df.to_excel('tabela_criada.xlsx', index=False, engine='openpyxl')
    return df