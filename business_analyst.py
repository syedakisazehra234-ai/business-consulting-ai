from crewai import Agent
from llm import get_groq_llm


def create_business_analyst():

    return Agent(
        role="Business Analysis Consultant",

        goal=(
            "Evaluate the business model, value proposition, "
            "customers, revenue logic, cost considerations, "
            "operational requirements, SWOT factors and key risks."
        ),

        backstory=(
            "You are a business analyst who evaluates business "
            "models and converts market and competitive information "
            "into structured business insights."
        ),

        llm=get_groq_llm(),

        verbose=True,

        allow_delegation=False
    )
