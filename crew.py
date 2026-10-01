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

1. Clearly define the business problem.
2. Identify the primary business objective.
3. Identify important constraints.
4. Identify assumptions that need validation.
5. Identify the most important strategic questions.
6. Define what the other consulting agents should investigate.

Do not invent facts.

Clearly distinguish:
- Client-provided information
- Reasonable assumptions
- Information that still needs validation
""",

        expected_output="""
A structured business problem definition containing:

- Business situation
- Core business problem
- Business objective
- Target customer
- Target market
- Constraints
- Assumptions
- Key strategic questions
- Research priorities
""",

        agent=strategist
    )


    # =========================================================
    # TASK 2 — MARKET RESEARCH
    # =========================================================

    market_task = Task(
        description="""
Analyze the target market using the client's information
and the business problem identified by the previous consultant.

Business:
{business_name}

Target market:
{target_market}

Target customer:
{target_customer}

Additional information:
{research}

Your responsibilities:

1. Analyze target customer segments.
2. Identify customer needs.
3. Identify demand drivers.
4. Analyze market trends mentioned in the supplied information.
5. Identify market opportunities.
6. Identify market threats.
7. Identify important unknowns.
8. Identify assumptions requiring validation.

Do not pretend that unsupported information is verified
market data.

Do not invent statistics.

Clearly identify information that requires external validation.
""",

        expected_output="""
A structured market analysis covering:

- Customer segments
- Customer needs
- Demand drivers
- Market trends
- Opportunities
- Threats
- Unknowns
- Assumptions requiring validation
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

Your responsibilities:

1. Analyze known competitor offerings.
2. Analyze competitor positioning.
3. Identify competitor target customers.
4. Identify competitor strengths.
5. Identify competitor weaknesses.
6. Analyze potential differentiation.
7. Identify possible market gaps.
8. Identify competitive risks.

If competitor information is missing,
explicitly state what cannot be determined.

Do not invent competitor facts.
""",

        expected_output="""
A structured competitive analysis containing:

- Competitor overview
- Positioning
- Customer focus
- Strengths
- Weaknesses
- Differentiation
- Possible market gaps
- Competitive risks
- Missing information
""",

        agent=competitor,

        context=[strategy_task]
    )


    # =========================================================
    # TASK 4 — BUSINESS ANALYSIS
    # =========================================================

    business_analysis_task = Task(
        description="""
Perform a structured business analysis using the findings
from the consulting team.

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

Do not fabricate financial numbers.

Do not fabricate market statistics.

Base your analysis on the information provided by the client
and the research findings passed through the previous tasks.
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
- Risks
- Dependencies
- Information gaps
""",

        agent=business_analyst,

        context=[
            strategy_task,
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

Synthesize the complete findings produced by the consulting
team.

Business:
{business_name}

Business problem:
{business_problem}

Target market:
{target_market}

Target customer:
{target_customer}

Develop:

1. Key strategic insights.
2. Strategic options.
3. Advantages and disadvantages of each option.
4. Major trade-offs.
5. Required capabilities.
6. Implementation priorities.
7. Major risks.
8. Risk mitigation approaches.
9. Suggested KPIs.
10. Questions that still require validation.

Do not present unsupported assumptions as facts.

Do not create generic business advice.

The strategy must be directly connected to the client's
business situation and the previous consulting analysis.
""",

        expected_output="""
A strategic synthesis containing:

- Key strategic insights
- Strategic options
- Trade-offs
- Required capabilities
- Implementation priorities
- Risks
- Risk mitigation approaches
- KPIs
- Validation questions
""",

        agent=strategy_consultant,

        context=[
            strategy_task,
            market_task,
            competitor_task,
            business_analysis_task
        ]
    )


    # =========================================================
    # TASK 6 — FINAL REPORT
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

Create a professional consulting report based on the
complete analysis produced by the previous consultants.

The report must contain:

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

Create three phases:

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
- Do not claim that internet research was performed.
- Clearly identify assumptions.
- Clearly distinguish supplied information from analysis.
- Avoid generic motivational language.
- Make the report practical and specific to the client's problem.
""",

        expected_output="""
A polished Markdown business consulting report containing
all requested sections.

The report must be professional, structured, specific
to the client's business problem and transparent about
assumptions and information gaps.
""",

        agent=report_consultant,

        context=[
            strategy_task,
            market_task,
            competitor_task,
            business_analysis_task,
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

    result = consulting_crew.kickoff(
        inputs=inputs
    )

    return result.raw
