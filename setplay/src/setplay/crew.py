"""Definição do Crew Setplay com o agente Docodex integrado."""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from setplay.tools.docodex_tool import DocodexTool


@CrewBase
class SetplayCrew:
    """Crew Setplay — consultoria técnica com suporte a documentação via Docodex."""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # ------------------------------------------------------------------ #
    # Agentes                                                              #
    # ------------------------------------------------------------------ #

    @agent
    def researcher_agent(self) -> Agent:
        """Agente pesquisador: identifica conceitos e contexto da pergunta."""
        return Agent(
            config=self.agents_config["researcher_agent"],
            tools=[],
        )

    @agent
    def docodex_agent(self) -> Agent:
        """Agente especialista: consulta documentação oficial via Docodex."""
        return Agent(
            config=self.agents_config["docodex_agent"],
            tools=[DocodexTool()],
        )

    # ------------------------------------------------------------------ #
    # Tarefas                                                              #
    # ------------------------------------------------------------------ #

    @task
    def research_task(self) -> Task:
        """Tarefa de pesquisa e identificação de termos-chave."""
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def documentation_task(self) -> Task:
        """Tarefa de consulta e resposta com base na documentação."""
        return Task(
            config=self.tasks_config["documentation_task"],
        )

    # ------------------------------------------------------------------ #
    # Crew                                                                 #
    # ------------------------------------------------------------------ #

    @crew
    def crew(self) -> Crew:
        """Monta o Crew com processo sequencial."""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
