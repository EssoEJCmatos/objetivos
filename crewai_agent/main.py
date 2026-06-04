import os
from pathlib import Path

from crewai import Agent, Crew, Process, Task
from dotenv import load_dotenv


def build_crew() -> Crew:
    researcher = Agent(
        role="Pesquisador de Conteúdo",
        goal="Gerar um resumo objetivo para atualização da edição especial",
        backstory="Especialista em curadoria de conteúdo científico em português.",
        verbose=True,
    )

    write_summary = Task(
        description=(
            "Criar um resumo curto com 3 pontos sobre tendências de ciência e "
            "tecnologia que podem ser usadas como atualização do jornal."
        ),
        expected_output=(
            "Texto em português com 3 bullets objetivos e linguagem acessível."
        ),
        agent=researcher,
    )

    return Crew(
        agents=[researcher],
        tasks=[write_summary],
        process=Process.sequential,
        verbose=True,
    )


def run() -> None:
    env_path = Path(__file__).with_name(".env")
    if not env_path.exists():
        raise SystemExit(
            "Arquivo de ambiente não encontrado. Crie 'crewai_agent/.env' com a OPENAI_API_KEY."
        )

    load_dotenv(env_path)
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit(
            "OPENAI_API_KEY não definida em 'crewai_agent/.env'."
        )
    try:
        result = build_crew().kickoff()
    except Exception as exc:
        raise SystemExit(f"Falha ao executar o CrewAI: {exc}") from exc

    print(result)


if __name__ == "__main__":
    run()
