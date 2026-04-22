"""Testes para a ferramenta DocodexTool."""

from unittest.mock import MagicMock, patch

import pytest

from setplay.tools.docodex_tool import DocodexTool


@pytest.fixture()
def tool() -> DocodexTool:
    return DocodexTool(base_url="https://docodex.dev/api", api_key=None)


def test_format_results_empty(tool: DocodexTool) -> None:
    result = tool._format_results({})
    assert "Nenhum resultado" in result


def test_format_results_with_hits(tool: DocodexTool) -> None:
    data = {
        "results": [
            {"title": "venv", "excerpt": "Cria ambientes virtuais.", "url": "https://docs.python.org/3/library/venv.html"},
        ]
    }
    result = tool._format_results(data)
    assert "venv" in result
    assert "Cria ambientes virtuais" in result
    assert "docs.python" in result or "python.org" in result


def test_run_connection_error(tool: DocodexTool) -> None:
    import requests

    with patch("requests.get", side_effect=requests.exceptions.ConnectionError):
        result = tool._run(query="venv", language="python")
    assert "Não foi possível conectar" in result


def test_run_timeout(tool: DocodexTool) -> None:
    import requests

    with patch("requests.get", side_effect=requests.exceptions.Timeout):
        result = tool._run(query="venv", language="python")
    assert "tempo limite" in result


def test_run_success(tool: DocodexTool) -> None:
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "results": [{"title": "venv", "excerpt": "Virtual environments."}]
    }

    with patch("requests.get", return_value=mock_response):
        result = tool._run(query="venv", language="python")

    assert "venv" in result
    assert "Virtual environments" in result
