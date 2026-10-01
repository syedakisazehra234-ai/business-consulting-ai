import os
import streamlit as st

# ---------------------------------------------------------
# FIX FOR CREWAI + GROQ CACHE BREAKPOINT BUG
# ---------------------------------------------------------
import crewai.llms.cache as crewai_cache

# CrewAI adds cache_breakpoint=True to messages.
# Groq does not support this property.
crewai_cache.mark_cache_breakpoint = lambda message: message


from crewai import LLM


def get_groq_llm():

    try:
        api_key = st.secrets["GROQ_API_KEY"]
    except Exception:
        api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Please add it to Streamlit Secrets."
        )

    return LLM(
        model="groq/openai/gpt-oss-120b",
        api_key=api_key,
        temperature=0.2,
        max_tokens=6000
    )
