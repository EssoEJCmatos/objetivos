"""Ferramenta personalizada Docodex para agentes CrewAI.

Permite que os agentes consultem documentação de linguagens e frameworks
através da API do Docodex (https://docodex.dev).
"""

import os
from typing import Optional, Type

import requests
from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class DocodexToolInput(BaseModel):
    """Esquema de entrada para a ferramenta Docodex."""

    query: str = Field(
        description="Pergunta ou termo a ser pesquisado na documentação."
    )
    language: Optional[str] = Field(
        default="python",
        description=(
            "Linguagem ou framework alvo da pesquisa. "
            "Exemplos: 'python', 'javascript', 'typescript', 'react', 'django'."
        ),
    )


class DocodexTool(BaseTool):
    """Ferramenta que consulta o Docodex para obter respostas de documentação técnica.

    Usa a API pública do Docodex para buscar trechos relevantes de documentação
    com base em uma pergunta em linguagem natural.
    """

    name: str = "Docodex Documentation Search"
    description: str = (
        "Pesquisa documentação técnica de linguagens e frameworks usando o Docodex. "
        "Útil para responder dúvidas de programação com base em fontes oficiais. "
        "Informe a pergunta e, opcionalmente, a linguagem alvo (padrão: python)."
    )
    args_schema: Type[BaseModel] = DocodexToolInput

    base_url: str = Field(
        default_factory=lambda: os.getenv(
            "DOCODEX_BASE_URL", "https://docodex.dev/api"
        )
    )
    api_key: Optional[str] = Field(
        default_factory=lambda: os.getenv("DOCODEX_API_KEY")
    )
    timeout: int = Field(default=15, description="Timeout em segundos para a requisição.")

    def _run(self, query: str, language: str = "python") -> str:
        """Executa a busca na API do Docodex e retorna o resultado."""
        headers = {"Accept": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"

        params = {"q": query, "lang": language}

        try:
            response = requests.get(
                f"{self.base_url}/search",
                params=params,
                headers=headers,
                timeout=self.timeout,
            )
            response.raise_for_status()
            data = response.json()
            return self._format_results(data)
        except requests.exceptions.ConnectionError:
            return (
                f"[Docodex] Não foi possível conectar à API ({self.base_url}). "
                "Verifique sua conexão ou a variável DOCODEX_BASE_URL."
            )
        except requests.exceptions.Timeout:
            return "[Docodex] A requisição excedeu o tempo limite."
        except requests.exceptions.HTTPError as exc:
            return f"[Docodex] Erro HTTP: {exc.response.status_code} — {exc.response.text}"
        except Exception as exc:  # noqa: BLE001
            return f"[Docodex] Erro inesperado: {exc}"

    @staticmethod
    def _format_results(data: dict) -> str:
        """Formata o JSON de resposta do Docodex em texto legível."""
        results = data.get("results") or data.get("hits") or []
        if not results:
            return "[Docodex] Nenhum resultado encontrado para a consulta."

        parts = []
        for idx, item in enumerate(results[:5], start=1):
            title = item.get("title") or item.get("name") or "Sem título"
            excerpt = item.get("excerpt") or item.get("description") or item.get("body") or ""
            url = item.get("url") or item.get("link") or ""
            block = f"{idx}. **{title}**\n{excerpt}"
            if url:
                block += f"\n   Referência: {url}"
            parts.append(block)

        return "\n\n".join(parts)
