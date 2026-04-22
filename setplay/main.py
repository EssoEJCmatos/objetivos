#!/usr/bin/env python
"""Script principal para executar o Crew Setplay."""

import sys

from dotenv import load_dotenv

from setplay.crew import SetplayCrew


def run(question: str | None = None) -> None:
    """Inicializa e executa o Crew com a pergunta fornecida."""
    load_dotenv()

    if question is None:
        question = (
            input("Digite sua pergunta técnica (ou pressione Enter para usar o exemplo): ").strip()
            or "Como criar um ambiente virtual em Python usando venv?"
        )

    inputs = {"question": question}
    result = SetplayCrew().crew().kickoff(inputs=inputs)
    print("\n" + "=" * 60)
    print("RESULTADO FINAL:")
    print("=" * 60)
    print(result)


def train() -> None:
    """Treina o Crew por N iterações (para uso com crewai train)."""
    load_dotenv()
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    question = sys.argv[2] if len(sys.argv) > 2 else "O que é list comprehension em Python?"
    SetplayCrew().crew().train(
        n_iterations=n,
        filename="trained_crew.pkl",
        inputs={"question": question},
    )


if __name__ == "__main__":
    question_arg = sys.argv[1] if len(sys.argv) > 1 else None
    run(question_arg)
