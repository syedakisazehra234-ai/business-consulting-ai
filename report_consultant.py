from crewai import Agent
from llm import get_groq_llm


def create_report_consultant():

    return Agent(
        role="Business Consulting Report Specialist",

        goal=(
            "Transform the complete consulting analysis into a "
            "professional business strategy report containing "
            "clear findings, strategic options, implementation "
            "priorities, KPIs and risks."
        ),

        backstory=(
            "You are an experienced management consulting report "
            "writer. You communicate complex business analysis "
            "clearly and professionally for business decision makers."
        ),

        llm=get_groq_llm(),

        verbose=True,

        allow_delegation=False
    )
