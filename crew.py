from crewai import Crew, Task, Process

from business_strategist import create_business_strategist
from market_researcher import create_market_researcher
from competitor_analyst import create_competitor_analyst
from business_analyst import create_business_analyst
from strategy_consultant import create_strategy_consultant
from report_consultant import create_report_consultant


def run_business_consulting(inputs):

    # =========================================================
    # CREATE AGENTS
    # =========================================================

    strategist = create_business_strategist()
    market_researcher = create_market_researcher()
    competitor = create_competitor_analyst()
    business_analyst = create_business_analyst()
    strategy_consultant = create_strategy_consultant()
    report_consultant = create_report_consultant()

    # =========================================================
    # TASK 1 — BUSINESS STRATEGY
    # =========================================================

    strategy_task = Task(
        description="""
Analyze the client's business situation.

Business:
{business_name}

Business problem:
{business_problem}

Target customer:
{target_customer}

Target market:
{target_market}

Known competitors:
{competitors}

Additional information:
{research}

Your responsibilities:

1. Define the core business problem.
2. Identify the primary business objective.
3. Identify important constraints.
4. Identify assumptions that require validation.
5. Identify the most important strategic questions.
6. Define the key areas that the consulting team should investigate.

Do not invent facts, statistics, customers, competitors, or market information.

Clearly distinguish:
- Client-provided information
- Reasonable assumptions
- Information requiring validation

Keep the analysis concise and practical.
""",
        expected_output="""
A concise structured business analysis containing:

- Business situation
- Core business problem
- Business objective
- Target customer
- Target market
- Constraints
- Assumptions
- Strategic questions
- Research priorities

Maximum 700 words.
""",
        agent=strategist
    )

    # =========================================================
    # TASK 2 — MARKET RESEARCH
    # =========================================================

    market_task = Task(
        description="""
Analyze the target market using the client's information
and the Business Strategist's analysis.

Business:
{business_name}

Target market:
{target_market}

Target customer:
{target_customer}

Additional information:
{research}

Analyze:

1. Customer segments
2. Customer needs
3. Demand drivers
4. Market trends mentioned in the supplied information
5. Market opportunities
6. Market threats
7. Important unknowns
8. Assumptions requiring validation

Do not claim that internet research was performed.

Do not invent statistics or market facts.

Clearly identify information that requires external validation.

Keep the analysis concise.
""",
        expected_output="""
A structured market analysis containing:

- Customer segments
- Customer needs
- Demand drivers
- Market trends
- Opportunities
- Threats
- Unknowns
- Validation requirements

Maximum 700 words.
""",
        agent=market_researcher,
        context=[strategy_task]
    )

    # =========================================================
    # TASK 3 — COMPETITOR ANALYSIS
    # =========================================================

    competitor_task = Task(
        description="""
Analyze the competitive environment for the business.

Business:
{business_name}

Target market:
{target_market}

Known competitors:
{competitors}

Additional information:
{research}

Analyze:

1. Known competitor offerings
2. Competitor positioning
3. Target customers
4. Competitor strengths
5. Competitor weaknesses
6. Potential differentiation
7. Possible market gaps
8. Competitive risks

If competitor information is insufficient,
explicitly state what cannot be determined.

Do not invent competitor facts.

Keep the analysis concise and evidence-aware.
""",
        expected_output="""
A structured competitive analysis containing:

- Competitor overview
- Positioning
- Customer focus
- Strengths
- Weaknesses
- Differentiation opportunities
- Possible market gaps
- Competitive risks
- Missing information

Maximum 700 words.
""",
        agent=competitor,
        context=[strategy_task]
    )

    # =========================================================
    # TASK 4 — BUSINESS ANALYSIS
    # =========================================================

    business_analysis_task = Task(
        description="""
Perform a structured business analysis using the market
and competitive findings provided by the previous consultants.

Business:
{business_name}

Business problem:
{business_problem}

Target customer:
{target_customer}

Target market:
{target_market}

Additional information:
{research}

Evaluate:

1. Business model
2. Value proposition
3. Customer fit
4. Revenue logic
5. Cost considerations
6. Operational requirements
7. SWOT factors
8. Major risks
9. Dependencies
10. Information gaps

Use the Market Researcher's and Competitor Analyst's findings.

Do not fabricate financial numbers.
Do not fabricate market statistics.
Do not invent missing information.

Keep the analysis practical and concise.
""",
        expected_output="""
A structured business analysis containing:

- Business model
- Value proposition
- Customer fit
- Revenue logic
- Cost considerations
- Operational requirements
- SWOT analysis
- Major risks
- Dependencies
- Information gaps

Maximum 800 words.
""",
        agent=business_analyst,
        context=[
            market_task,
            competitor_task
        ]
    )

    # =========================================================
    # TASK 5 — STRATEGY SYNTHESIS
    # =========================================================

    strategy_synthesis_task = Task(
        description="""
Act as the Senior Strategy Consultant.

Synthesize the Business Analyst's findings into practical
strategic options for the client.

Business:
{business_name}

Business problem:
{business_problem}

Target market:
{target_market}

Target customer:
{target_customer}

Develop:

1. Key strategic insights
2. Strategic options
3. Advantages and disadvantages of each option
4. Major trade-offs
5. Required capabilities
6. Implementation priorities
7. Major risks
8. Risk mitigation approaches
9. Suggested KPIs
10. Questions requiring validation

Do not present assumptions as facts.

Do not create generic motivational advice.

Connect the strategy directly to the client's business situation.

Keep the strategy concise and actionable.
""",
        expected_output="""
A strategic synthesis containing:

- Key strategic insights
- Strategic options
- Advantages and disadvantages
- Trade-offs
- Required capabilities
- Implementation priorities
- Risks
- Risk mitigation
- KPIs
- Validation questions

Maximum 1000 words.
""",
        agent=strategy_consultant,
        context=[
            business_analysis_task
        ]
    )

    # =========================================================
    # TASK 6 — FINAL CONSULTING REPORT
    # =========================================================

    report_task = Task(
        description="""
Create the final Business Consulting Strategy Report.

Business:
{business_name}

Business problem:
{business_problem}

Target market:
{target_market}

Target customer:
{target_customer}

Use the Senior Strategy Consultant's synthesis as the
primary source for the final report.

Create a professional Markdown consulting report with:

# Business Consulting Strategy Report

## 1. Executive Summary

## 2. Business Situation

## 3. Core Business Problem

## 4. Target Customer

## 5. Market Analysis

## 6. Competitive Analysis

## 7. Business Model Analysis

## 8. SWOT Analysis

## 9. Key Strategic Insights

## 10. Strategic Options

## 11. Implementation Roadmap

### 0–30 Days

### 31–60 Days

### 61–90 Days

## 12. KPIs

## 13. Key Risks

## 14. Information Gaps

## 15. Next Steps

Important rules:

- Do not invent statistics.
- Do not invent competitor facts.
- Do not claim internet research was performed.
- Clearly identify assumptions.
- Clearly distinguish supplied information from analysis.
- Avoid generic motivational language.
- Make recommendations specific to the client's business problem.
- If information is unavailable, state that it requires validation.

Keep the final report concise enough to remain useful.
""",
        expected_output="""
A polished Markdown business consulting strategy report
containing all requested sections.

The report should be specific, practical, professional,
and transparent about assumptions and information gaps.

Maximum 1500 words.
""",
        agent=report_consultant,
        context=[
            strategy_synthesis_task
        ]
    )

    # =========================================================
    # CREATE CREW
    # =========================================================

    consulting_crew = Crew(
        agents=[
            strategist,
            market_researcher,
            competitor,
            business_analyst,
            strategy_consultant,
            report_consultant
        ],
        tasks=[
            strategy_task,
            market_task,
            competitor_task,
            business_analysis_task,
            strategy_synthesis_task,
            report_task
        ],
        process=Process.sequential,
        verbose=True,
        share_crew=False
    )

    # =========================================================
    # RUN CREW
    # =========================================================

    result = consulting_crew.kickoff(inputs=inputs)

    return result.raw
