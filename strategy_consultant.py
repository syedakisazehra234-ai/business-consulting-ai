from crewai import Agent
from llm import get_groq_llm


def create_strategy_consultant():

    return Agent(
        role="Senior Strategy Consultant",

        goal=(
            "Synthesize the consulting team's findings into "
            "clear strategic options, implementation priorities, "
            "trade-offs, risks and measurable objectives."
        ),

        backstory=(
            "You are a senior strategy consultant. You examine "
            "multiple perspectives, challenge unsupported assumptions "
            "and translate analysis into practical strategic options."
        ),

        llm=get_groq_llm(),

        verbose=True,

        allow_delegation=False
    )
