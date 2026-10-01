# 📊 Business Consulting AI

A multi-agent business consulting system built with CrewAI,
Groq GPT-OSS 120B and Streamlit.

## Overview

The system uses six specialized AI consultants:

1. Business Strategist
2. Market Researcher
3. Competitor Analyst
4. Business Analyst
5. Strategy Consultant
6. Report Consultant

The agents work sequentially to transform business information
into a structured strategy report.

## Architecture

User Input
    ↓
Business Strategist
    ↓
Market Researcher
    ↓
Competitor Analyst
    ↓
Business Analyst
    ↓
Strategy Consultant
    ↓
Report Consultant
    ↓
Business Strategy Report

## Technology

- Python
- CrewAI
- Groq
- GPT-OSS 120B
- Streamlit

## Important limitation

Version 1 does not perform live internet research.

The system analyzes information supplied by the user.

Future versions can add external research tools.

## Deployment

The application is designed for Streamlit Community Cloud.

The Groq API key should be stored in Streamlit Secrets
and must never be committed to GitHub.

## Project Structure

business-consulting-ai/

├── app.py
├── crew.py
├── llm.py
├── business_strategist.py
├── market_researcher.py
├── competitor_analyst.py
├── business_analyst.py
├── strategy_consultant.py
├── report_consultant.py
├── requirements.txt
└── README.md
