diretório_legenda = "Living Single - S01 E03 - Whose Date Is It Anyway (480p - HULU Web-DL).srt"
nome_final = "traduzido.srt"

from module import module
module()

from deep_translator import GoogleTranslator
from tqdm import tqdm  # Importar tqdm para a barra de progresso

# Função para traduzir um bloco de texto
def traduzir_bloco(blocos):
    # Definir um separador único que não será usado no texto
    separador = '@@SEPARATOR@@'

    # Concatenar os textos de todos os blocos para tradução, com o separador entre eles
    texto_para_traduzir = separador.join(['\n'.join(bloco[2:]) for bloco in blocos])  # Pegar o texto a partir da linha 3 de cada bloco
    
    # Traduzir o texto completo usando GoogleTranslator
    translated_text = GoogleTranslator(source='en', target='pt').translate(texto_para_traduzir)
    
    # Separar o texto traduzido de volta em blocos com base no separador
    textos_traduzidos = translated_text.split(separador)

    # Atribuir o texto traduzido de volta aos blocos, mantendo o timestamp
    for i, bloco in enumerate(blocos):
        blocos[i] = bloco[:2] + [textos_traduzidos[i]]  # Substitui o texto original com o traduzido
    
    return blocos

# Ler o arquivo de legendas .srt
with open(diretório_legenda, 'r', encoding='utf-8-sig') as f:
    texto = f.readlines()

# Lista para armazenar os blocos de legendas
bloco_todos = []

# Lista temporária para armazenar o bloco atual de legendas
bloco_atual = []

# Percorrer cada linha do arquivo
for linha in texto:
    # Se a linha for vazia, significa que o bloco acabou
    if linha == "\n":
        # Se o bloco atual não estiver vazio, adiciona à lista de blocos
        if bloco_atual:
            bloco_todos.append(bloco_atual)
            bloco_atual = []  # Limpa o bloco para começar um novo
    else:
        # Adiciona a linha ao bloco atual
        bloco_atual.append(linha.strip())  # .strip() para remover espaços extras e quebras de linha

# Adicionar o último bloco, se houver
if bloco_atual:
    bloco_todos.append(bloco_atual)

# Lista para armazenar os blocos traduzidos
bloco_traduzido_todos = []

# Traduzir os blocos em grupos de 20
for i in tqdm(range(0, len(bloco_todos), 20), desc="Traduzindo Blocos", unit="bloco"):
    # Pegar um grupo de até 20 blocos
    blocos_para_traduzir = bloco_todos[i:i+20]
    
    # Traduzir o grupo de blocos
    blocos_traduzidos = traduzir_bloco(blocos_para_traduzir)
    
    # Adicionar os blocos traduzidos à lista final
    bloco_traduzido_todos.extend(blocos_traduzidos)

# Salvar os blocos traduzidos em um novo arquivo .srt
with open(nome_final, 'w', encoding='utf-8-sig') as f:
    for bloco in bloco_traduzido_todos:
        f.write(f"{bloco[0]}\n")
        f.write(f"{bloco[1]}\n")
        f.write(f"{bloco[2]}\n")
        f.write("\n")

print("Arquivo traduzido gerado com sucesso!")
