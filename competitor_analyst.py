from crewai import Agent
from llm import get_groq_llm


def create_competitor_analyst():

    return Agent(
        role="Competitive Intelligence Analyst",

        goal=(
            "Analyze the identified competitors, their offerings, "
            "target customers, positioning, strengths, weaknesses, "
            "differentiation and potential market gaps."
        ),

        backstory=(
            "You are a competitive intelligence specialist. "
            "You compare businesses systematically and avoid "
            "inventing competitor facts when information is unavailable."
        ),

        llm=get_groq_llm(),

        verbose=True,

        allow_delegation=False
    )
