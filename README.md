# Documentação do Programa de Tradução de Legendas

## Descrição


Este programa foi desenvolvido para traduzir legendas de vídeos, utilizando a biblioteca [deep-translator](https://pypi.org/project/deep-translator/). Ele realiza a tradução de legendas de maneira simples e eficiente, através de um processo em que o arquivo de legenda é lido, dividido em blocos de texto, traduzido e então reorganizado para formar o arquivo de legenda final. A tradução é feita por meio do Google Tradutor, o que permite a conversão do texto original para o idioma de destino de forma rápida.

## Como Utilizar

1. **Preparação do Ambiente**:  
   Certifique-se de ter o Python instalado em sua máquina. Caso não tenha, faça o download em [python.org](https://www.python.org/downloads/).

2. **Configuração Inicial**:
   - Abra o arquivo `ler_txt.py` no seu editor de código favorito.
   - Localize as variáveis onde o diretório da legenda e o nome final da legenda precisam ser definidos. Exemplo:

     ```python
     diretório_legenda = "caminho/para/o/arquivo.srt"
     nome_final = "nome_da_legenda_traduzida.srt"
     ```

   - Defina os idiomas de origem e de destino. Exemplo:
  
      ```python
      idioma_origem = 'en'
      idioma_final = 'pt'
      ```
3. **Requisitos de legenda**:
   Para que funcione de forma adequada, o arquivo de legenda deve estar formatado de maneira semelhante a essa:

   ```text
    1
    00:00:01,833 --> 00:00:03,000
    I'm always sad to say goodbye
    
    2
    00:00:03,066 --> 00:00:05,333
    to the makeup that has
    seen me through the day.
   ```

3. **Executando o Programa**:
   - Depois de configurar os caminhos dos arquivos de legenda, execute o programa no terminal ou na interface de desenvolvimento de sua preferência.
   - O programa irá ler a legenda e realizar a tradução, gerando um novo arquivo com a tradução no diretório onde o arquivo executado está.

## Contribuições

Este projeto está em desenvolvimento. Se você deseja contribuir, fique à vontade para enviar pull requests ou sugestões de melhorias.
