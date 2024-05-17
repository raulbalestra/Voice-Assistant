# Voice Assistant using OpenAI GPT-4o and Eleven Labs TTS

## Descrição

Este projeto implementa um assistente de voz pessoal usando Python. Ele utiliza a API da OpenAI para gerar respostas baseadas em comandos de voz e a API da Eleven Labs para converter texto em fala. O assistente captura comandos de voz, gera respostas utilizando o modelo GPT-4o e responde com uma voz sintetizada.

## Funcionalidades

- **Reconhecimento de Fala**: Captura e transcreve comandos de voz usando `speech_recognition`.
- **Geração de Respostas**: Utiliza a API do OpenAI GPT-4o para gerar respostas a partir dos comandos de voz.
- **Síntese de Voz**: Converte texto em fala usando a API da Eleven Labs e reproduz o áudio gerado.
- **Execução Contínua**: Funciona em um loop contínuo para permitir interações contínuas.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python:
  - `openai`
  - `speech_recognition`
  - `requests`
  - `pyaudio`
  - `mpg123` (para reprodução de áudio)

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Defina as chaves da API diretamente no script:

```python
# Definir chaves da API diretamente no script
openai_api_key = 'YOUR_OPENAI_API_KEY'
eleven_labs_api_key = 'YOUR_ELEVEN_LABS_API_KEY'
```

## Uso

Para iniciar o assistente de voz, execute o script:

```bash
python3 script.py
```

## Estrutura do Código

### Bibliotecas Utilizadas
- `os`: Para operações de sistema, como verificar e manipular arquivos.
- `openai`: Para integração com a API da OpenAI.
- `speech_recognition`: Para captura e transcrição de comandos de voz.
- `requests`: Para fazer requisições HTTP.
- `time`: Para manipulação de tempo e delays.

### Funções Principais

#### `record_audio()`
Captura áudio do microfone e usa a API do Google para transcrever o áudio para texto.

#### `get_gpt_response(prompt)`
Envia o prompt do usuário para a API da OpenAI e retorna a resposta gerada pelo modelo GPT-4o.

#### `speak_text(text)`
Gera áudio a partir de texto utilizando a API da Eleven Labs e reproduz o áudio gerado.

### Função Principal

A função `main()` gerencia o ciclo principal de interação do assistente, capturando comandos de voz, gerando respostas e falando as respostas.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE]((https://github.com/raulbalestra/Voice-Assistant/blob/7e786369d6fff4428e09a29a0cbe2591458288a4/License)) para mais detalhes.

