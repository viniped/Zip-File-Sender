# Zip-File-Sender

## Descrição
Este script Python automatiza o processo de envio de arquivos para um canal do Telegram especificado, utilizando a biblioteca Pyrogram. Ele suporta o envio de imagens, documentos e stickers.

## Pré-requisitos
- Python 3.10.12
- Pyrogram
- tqdm
- natsort
- Chocolatey (para instalação do Python no Windows)

## Passo a Passo

### 1. Instalar o Python 3.10.12 usando Chocolatey (Windows)
1. **Instalar Chocolatey:**
   - Visite [chocolatey.org/install](https://chocolatey.org/install).
   - Execute o script de instalação em um prompt de comando administrativo.
2. **Instalar Python via Chocolatey:**
   - Execute `choco install python --version=3.10.12` no prompt de comando administrativo.

#### No Ubuntu
1. **Atualizar lista de pacotes:**
   - Abra um terminal e execute `sudo apt update`.
2. **Instalar Python 3.10:**
   - Execute `sudo apt install python3.10`.

### 2. Configurar o Ambiente
1. **Clone o repositório ou baixe o script.**
2. **Instalar dependências:**
   - Navegue até o diretório do script.
   - Execute `pip install pyrogram tqdm natsort`.

### 3. Configurar o Script
1. **Criar arquivo `config.json`:**
   - Inclua `{"channel_id": "YOUR_CHANNEL_ID"}` substituindo `YOUR_CHANNEL_ID`.
2. **(Opcional) Adicionar arquivo `caption.txt`:**
   - Crie e escreva a legenda para as imagens.

### 4. Preparar os Arquivos para Envio
1. **Coloque os arquivos na pastas `input`**
2. Execute o script. o upload será iniciado após a compactação
   
### 5. Executar o Script
1. **Abra o terminal no diretório do script.**
2. **Execute o script:**
   - `python [nome_do_script].py`.

### Observações
- Este script é projetado para Windows e linux
- Para execução no linux você pode usar o mesmo arquivo que usa no windows ou usar o `main_async.py` cuja construção foi feita com um loop assincrono que promete acelerar os uploads
- Assegure as permissões necessárias no Telegram.
- A função `process_folder` divide arquivos grandes antes do envio.

## Notas
Certifique-se de ter as permissões necessárias e acesso ao canal onde deseja fazer o upload dos vídeos. Aproveite a organização e o compartilhamento do seu conteúdo audiovisual no Telegram!

## Suporte
Caso tenha alguma duvida entre nesse grupo
https://t.me/+uxnB4OwMYPhiNWMx

## Garantia 
O script é fornecido como está e o desenvolvedor e o github não se responsabilizam pelo mal uso
é dever do usuário certificar-se que tem permissões para fazer upload de contéudos para o Telegram 
por meio do script.
