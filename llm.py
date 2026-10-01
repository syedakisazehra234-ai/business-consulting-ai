import os
import streamlit as st
from crewai import LLM


def get_groq_llm():

    # Get API key from Streamlit Secrets
    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Please add GROQ_API_KEY to Streamlit Secrets."
        )

    return LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=api_key,
        temperature=0.2,
        max_tokens=6000,

        # Important:
        # Prevent LiteLLM/CrewAI from using prompt caching
        extra_params={
            "cache_control": None
        }
    )
