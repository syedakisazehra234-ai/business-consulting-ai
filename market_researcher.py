from crewai import Agent
from llm import get_groq_llm


def create_market_researcher():

    return Agent(
        role="Market Research Analyst",

        goal=(
            "Analyze the target market, customer segments, demand "
            "drivers, market trends, opportunities and threats using "
            "the information provided by the client."
        ),

        backstory=(
            "You are an experienced market research analyst. "
            "You structure market information carefully and clearly "
            "distinguish between supplied evidence, reasonable "
            "inferences and assumptions that require validation."
        ),

        llm=get_groq_llm(),

        verbose=True,

        allow_delegation=False
    )
