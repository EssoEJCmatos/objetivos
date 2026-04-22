# Setplay — Crew de Agentes com Docodex

Projeto CrewAI em Python que integra o agente **Docodex** para consulta de
documentação técnica em linguagem natural.

## 🗂 Estrutura de Pastas

```
setplay/
├── main.py                         # Ponto de entrada
├── pyproject.toml                  # Configuração do pacote
├── requirements.txt                # Dependências
├── .env.example                    # Exemplo de variáveis de ambiente
├── src/
│   └── setplay/
│       ├── __init__.py
│       ├── crew.py                 # Definição do Crew e agentes
│       ├── tools/
│       │   ├── __init__.py
│       │   └── docodex_tool.py    # Ferramenta Docodex personalizada
│       └── config/
│           ├── agents.yaml        # Configuração dos agentes
│           └── tasks.yaml         # Configuração das tarefas
└── tests/
    ├── __init__.py
    └── test_docodex_tool.py       # Testes unitários da ferramenta
```

## 🤖 Agentes

| Agente | Papel | Ferramenta |
|---|---|---|
| `researcher_agent` | Identifica termos-chave e contexto da pergunta | — |
| `docodex_agent` | Consulta documentação oficial e formula a resposta | `DocodexTool` |

## ⚙️ Configuração

1. **Instale as dependências:**

```bash
cd setplay
pip install -r requirements.txt
# ou com pip editável:
pip install -e .
```

2. **Configure as variáveis de ambiente:**

```bash
cp .env.example .env
# Edite .env e preencha OPENAI_API_KEY (obrigatório) e DOCODEX_API_KEY (opcional)
```

3. **Execute o Crew:**

```bash
# Interativo
python main.py

# Passando a pergunta como argumento
python main.py "Como usar decoradores em Python?"
```

## 🛠 Ferramenta Docodex (`DocodexTool`)

A `DocodexTool` é uma ferramenta personalizada baseada em `BaseTool` do CrewAI.
Ela realiza requisições à API do Docodex para buscar trechos de documentação
técnica relevantes para a pergunta do usuário.

| Parâmetro | Padrão | Descrição |
|---|---|---|
| `query` | — | Pergunta em linguagem natural |
| `language` | `python` | Linguagem/framework alvo |

Variáveis de ambiente aceitas:

| Variável | Descrição |
|---|---|
| `DOCODEX_BASE_URL` | URL base da API (padrão: `https://docodex.dev/api`) |
| `DOCODEX_API_KEY` | Chave de autenticação (opcional) |

## 🧪 Testes

```bash
cd setplay
pip install pytest
pytest tests/ -v
```

## 🔧 Tecnologias

- **Python 3.11+**
- **[CrewAI](https://docs.crewai.com/)** — framework de orquestração de agentes
- **[crewai-tools](https://pypi.org/project/crewai-tools/)** — ferramentas prontas e base para customização
- **[Docodex](https://docodex.dev)** — API de busca em documentação técnica
- **python-dotenv** — gerenciamento de variáveis de ambiente
- **pydantic** — validação de dados e schemas
