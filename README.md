# Jornal Científico Nacional — 1950-1960

Página estática em HTML/CSS com visual de jornal antigo, dedicada ao tema de ciência, tecnologia e inovação no período de 1950 a 1960.

## 🎯 Objetivo do Projeto

- **Exibir uma edição especial em formato de jornal histórico.**
- **Praticar estrutura semântica de HTML e estilização com CSS.**
- **Manter código limpo, acessível e responsivo.**

### Tecnologias e Práticas Implementadas

Este projeto foi desenvolvido com as seguintes práticas:

- ✅ **HTML Semântico** — Utilização adequada de tags como `<header>`, `<main>`, `<article>`, `<section>`, `<figure>` e `<footer>`
- ✅ **CSS Responsivo** — Design adaptado para todos os tamanhos de tela
- ✅ **Clean Code** — Organização, clareza e fácil manutenção
- ✅ **Acessibilidade (WCAG)** — Navegação por teclado, skip links, contraste adequado
- ✅ **Performance** — Sem dependências externas, lazy loading de imagens

## 📁 Estrutura de Pastas

```
html3/
├── objetivos.html          # Documento HTML semântico
├── README.md               # Este arquivo
└── assets/
    ├── css/
    │   └── styles.css      # Stylesheet único e organizado
    └── imagem/
        └── peb.png         # Imagem histórica
```

## 🚀 Como Executar a Página

### Opção 1: Abrir no Navegador (Mais Simples)

1. Localize o arquivo `objetivos.html`
2. Clique duas vezes para abrir no navegador padrão
3. Pronto! A página será exibida

### Opção 2: Usar Live Server no VS Code

1. **Instale a extensão** [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)
2. **Abra o arquivo** `objetivos.html` no VS Code
3. **Clique com o botão direito** no arquivo
4. **Selecione** "Open with Live Server"
5. A página será aberta em `http://localhost:5500` com recarregamento automático

## ♿ Acessibilidade, Usabilidade e Responsividade

### Melhorias Implementadas

#### HTML Semântico
- ✅ Uso de landmarks estruturais (`<header>`, `<main>`, `<article>`, `<section>`, `<footer>`)
- ✅ Elementos `<figure>` e `<figcaption>` para imagens
- ✅ Atributos `aria-label` e `aria-labelledby` onde apropriado
- ✅ Atributos `aria-hidden` para elementos decorativos

#### Acessibilidade
- ✅ **Skip link** — Navegação direta para o conteúdo principal via teclado
- ✅ **Foco visível** — Indicadores de foco `:focus-visible` com contraste adequado
- ✅ **Classe `.visually-hidden`** — Conteúdo acessível a leitores de tela
- ✅ **Lazy loading** — Imagens carregadas sob demanda para performance
- ✅ **Semântica clara** — Uso apropriado de tags HTML5

#### Responsividade
- ✅ **Mobile-first** — Design otimizado para telas pequenas (até 480px)
- ✅ **Breakpoints estratégicos** — Tablets (até 960px), Smartphones (até 680px), Mini phones (até 480px)
- ✅ **Tipografia fluida** — Uso de `clamp()` para escalabilidade dinâmica
- ✅ **Grid responsivo** — Layout em 3 colunas → 2 colunas → 1 coluna
- ✅ **Espaçamentos adaptativos** — Padding e margin ajustados com `clamp()`

#### Clean Code
- ✅ **CSS variáveis** — Definição centralizada de cores e valores
- ✅ **Seções comentadas** — Organização visual e fácil manutenção
- ✅ **Nomes descritivos** — Classes e IDs significativos
- ✅ **Sem elementos obsoletos** — Remoção de tags como `<center>`
- ✅ **Centralização via CSS** — Não via HTML obsoleto

#### Preferências do Usuário
- ✅ **Suporte `prefers-reduced-motion`** — Respeita preferências de acessibilidade
- ✅ **Estilos de impressão** — Página otimizada para print
- ✅ **Suporte futuro para tema escuro** — Estrutura pronta para `prefers-color-scheme`

## 🎨 Design e Paleta de Cores

| Variável | Cor | Uso |
|----------|-----|-----|
| `--bg-page` | #9d8a6f | Fundo da página |
| `--bg-paper` | #ead9bd | Fundo principal do jornal |
| `--bg-paper-soft` | #f6efe3 | Fundo alternativo |
| `--ink-strong` | #1d130c | Texto principal e headings |
| `--ink-normal` | #2e2217 | Texto corpo |
| `--ink-soft` | #5a4a3b | Texto secundário |
| `--border-strong` | #3a2f25 | Bordas |
| `--focus-color` | #0b4f9e | Foco (acessibilidade) |

## 📱 Breakpoints de Responsividade

| Tamanho | Breakpoint | Aplicação |
|---------|-----------|-----------|
| Desktop | 960px+ | Grid 3 colunas |
| Tablet | até 960px | Grid 2 colunas |
| Mobile | até 680px | Grid 1 coluna |
| Mini Phone | até 480px | Ajustes finos de espaçamento |

## 🔧 Tecnologias Utilizadas

- **HTML5** — Semântica moderna e estrutura acessível
- **CSS3** — Variáveis CSS, Grid, Flexbox, Media Queries
- **Sem dependências externas** — Código puro e performático

## 🤖 Integração com agente CrewAI

Foi adicionada uma integração mínima de agente em:

```
crewai_agent/main.py
```

### Como executar

1. Tenha Python 3.10+ (mínimo recomendado; confirme também os requisitos atuais do CrewAI na documentação oficial)
2. Instale dependências:

```bash
pip install crewai python-dotenv
```

3. Crie o arquivo de ambiente:

```bash
cp crewai_agent/.env.example crewai_agent/.env
```

4. Configure sua chave no `crewai_agent/.env` (ex.: `OPENAI_API_KEY`)
5. Execute:

```bash
python crewai_agent/main.py
```

Esse agente gera um resumo curto em português para apoiar atualizações editoriais do projeto.

## 💻 Configuração do VS Code

O repositório inclui configuração pronta em `.vscode/` para abrir e desenvolver diretamente no VS Code.

### Extensões recomendadas (instaladas automaticamente pelo VS Code)

| Extensão | Finalidade |
|----------|-----------|
| Live Server | Servir `objetivos.html` com recarregamento automático |
| Python + Pylance | Desenvolvimento e depuração do agente CrewAI |
| GitLens | Histórico e anotações Git avançadas |
| GitHub Pull Requests | Gerenciar PRs sem sair do editor |

### Tarefas disponíveis (`Ctrl+Shift+B`)

- **Sincronizar com GitHub** — executa `scripts/sync.sh` (commit + push automático)
- **Instalar dependências CrewAI** — instala `crewai` e `python-dotenv`

### Debug (`F5`)

- **Executar agente CrewAI** — inicia `crewai_agent/main.py` no terminal integrado com `.env` carregado

### Sincronização automática via terminal

```bash
# Commita todas as alterações e envia para o GitHub em um comando:
./scripts/sync.sh "sua mensagem aqui"
```

## ⚙️ CI — GitHub Actions

O workflow `.github/workflows/ci.yml` executa automaticamente a cada `push`:

1. **Validação de sintaxe Python** — verifica `crewai_agent/main.py`
2. **Validação de HTML** — verifica `objetivos.html` com o validador oficial W3C
3. **Auto-atualização de data no README** — atualiza "Última atualização" em merges para `main`/`master`

Nenhuma configuração extra é necessária: o workflow usa o token `GITHUB_TOKEN` já disponível no repositório.

## 📁 Estrutura de Pastas (atualizada)

```
objetivos/
├── objetivos.html          # Documento HTML semântico
├── README.md               # Este arquivo
├── .gitignore              # Ignorar artefatos Python e .env
├── assets/
│   ├── css/styles.css      # Stylesheet único e organizado
│   └── imagem/peb.png      # Imagem histórica
├── crewai_agent/
│   ├── main.py             # Agente CrewAI
│   └── .env.example        # Exemplo de configuração de ambiente
├── scripts/
│   └── sync.sh             # Script de commit + push rápido
├── .vscode/
│   ├── settings.json       # Configurações do editor
│   ├── extensions.json     # Extensões recomendadas
│   ├── launch.json         # Configurações de depuração
│   └── tasks.json          # Tarefas de build/sync
└── .github/
    └── workflows/
        └── ci.yml          # Pipeline de CI/CD
```

## 📊 Performance e Otimizações

- ✅ Imagem com `loading="lazy"` para lazy loading
- ✅ Atributo `decoding="async"` para decodificação não-bloqueante
- ✅ CSS único e bem organizado (sem fragmentação)
- ✅ Transições suaves respeitando preferências do usuário
- ✅ Sem JavaScript — Performance máxima

## 🛠️ Melhorias Recentes (Patch v1)

- 🔄 **Refatoração completa de CSS** — Melhor organização e comentários
- 📝 **HTML ajustado** — Atributos `meta` adicionais para acessibilidade
- 📱 **Responsividade ampliada** — Suporte melhorado para telas mini (até 480px)
- ✅ **Validação semântica** — Uso de `<div class="date-line">` em vez de `<p>`
- 🔐 **Segurança de links** — Atributos `rel="noopener noreferrer"` em links externos
- 🎯 **Skip link aprimorado** — Transição suave e melhor visibilidade

## 🧪 Testes de Acessibilidade

Para validar a acessibilidade desta página:

1. **Teste com teclado** — Navegue usando `Tab` e `Shift+Tab`
2. **Use um leitor de tela** — NVDA (Windows), JAWS, VoiceOver (Mac)
3. **Verifique contraste** — Use ferramentas como WebAIM Contrast Checker
4. **Inspecione elementos** — DevTools para verificar hierarquia de headings

## 📚 Referências e Recursos

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [MDN Web Docs — HTML Semântico](https://developer.mozilla.org/en-US/docs/Glossary/Semantics)
- [CSS-Tricks — Responsive Typography](https://css-tricks.com/books/fundamental-css-curriculum/)
- [Web.dev — Accessibility](https://web.dev/accessibility/)

## 📄 Licença

Este projeto é educacional e pode ser livremente modificado e distribuído.

---

**Última atualização:** Março 2026  
**Status:** ✅ Completo e totalmente responsivo
