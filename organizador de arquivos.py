# Renomear todos os arquivos de uma pasta automaticamente, colocando um nome padrão seguido de um número sequencial

import os

# Pasta no Computador que deseja selecionar
caminho = input("Digite o caminho completo da pasta com os arquivos: ")

# Prefixo / Nome que deseja usar no arquivo final
prefixo = input("Digite o prefixo que deseja usar: ")

# Listando todos os arquivos da Pasta selecionada
arquivos = os.listdir(caminho)

# Para cada arquivo, criar um novo nome
for i, arquivo in enumerate(arquivos, start=1):

    # Caminho completo do arquivo atual
    caminho_antigo = os.path.join(caminho, arquivo)

    # Separar a extensão (.jpg, .txt, etc.)
    _, extensao = os.path.splitext(arquivo)

    # Criar novo nome 
    novo_nome = f"{prefixo}_{i}{extensao}"
    caminho_novo = os.path.join(caminho, novo_nome)

    # Renomear o arquivo final na pasta 
    os.rename(caminho_antigo, caminho_novo)
    print(f"{arquivo} --> {novo_nome}")
