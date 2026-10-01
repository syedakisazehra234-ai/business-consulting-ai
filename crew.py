from crewai import Crew, Task, Process

from business_strategist import create_business_strategist
from market_researcher import create_market_researcher
from competitor_analyst import create_competitor_analyst
from business_analyst import create_business_analyst
from strategy_consultant import create_strategy_consultant
from report_consultant import create_report_consultant


def run_business_consulting(inputs):

    # ---------------------------------------------------------
    # CREATE AGENTS
    # ---------------------------------------------------------

    strategist = create_business_strategist()

    market_researcher = create_market_researcher()

    competitor = create_competitor_analyst()

    business_analyst = create_business_analyst()

    strategy_consultant = create_strategy_consultant()

    report_consultant = create_report_consultant()


    # ---------------------------------------------------------
    # TASK 1 — BUSINESS STRATEGY
    # ---------------------------------------------------------

    strategy_task = Task(

        description="""
You are the first consultant in the team.

Analyze the following client information:

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

Your job is to:

1. Clearly define the business problem.
2. Identify the primary business objective.
3. Identify important constraints.
4. Identify assumptions that need validation.
5. Identify the most important strategic questions.
6. Define what the other consulting agents should investigate.

Do not invent facts.
Clearly distinguish client-provided information from assumptions.
""",

        expected_output="""
A structured business problem definition containing:

- Business situation
- Core business problem
- Business objective
- Target customer
- Market
- Constraints
- Assumptions
- Key strategic questions
- Research priorities
""",

        agent=strategist
    )


    # ---------------------------------------------------------
    # TASK 2 — MARKET RESEARCH
    # ---------------------------------------------------------

    market_task = Task(

        description="""
Analyze the market using the client information and the
Business Strategist's analysis.

Client information:

Business:
{business_name}

Target market:
{target_market}

Target customer:
{target_customer}

Additional research:
{research}

Previous consultant analysis:

{strategy_task}

Analyze:

1. Target customer segments
2. Customer needs
3. Demand drivers
4. Market trends mentioned in the supplied information
5. Market opportunities
6. Market threats
7. Important unknowns
8. Assumptions requiring external validation

Do not pretend that unsupported information is verified market data.
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


    # ---------------------------------------------------------
    # TASK 3 — COMPETITOR ANALYSIS
    # ---------------------------------------------------------

    competitor_task = Task(

        description="""
Analyze the competitive environment.

Business:
{business_name}

Target market:
{target_market}

Known competitors:
{competitors}

Additional information:
{research}

Use the Business Strategist's analysis below:

{strategy_task}

Analyze:

1. Competitor offerings
2. Competitor positioning
3. Target customers
4. Strengths
5. Weaknesses
6. Differentiation
7. Possible market gaps
8. Competitive risks

If competitor information is missing, explicitly state what
cannot be determined instead of inventing facts.
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


    # ---------------------------------------------------------
    # TASK 4 — BUSINESS ANALYSIS
    # ---------------------------------------------------------

    business_analysis_task = Task(

        description="""
Perform a structured business analysis using the previous
consulting findings.

Business:
{business_name}

Business problem:
{business_problem}

Additional information:
{research}

Business strategy analysis:

{strategy_task}

Market analysis:

{market_task}

Competitive analysis:

{competitor_task}

Evaluate:

1. Business model
2. Value proposition
3. Customer fit
4. Revenue logic
5. Cost considerations
6. Operational requirements
7. SWOT analysis
8. Major risks
9. Dependencies
10. Important information gaps

Do not fabricate financial numbers or market statistics.
""",

        expected_output="""
A structured business analysis containing:

- Business model
- Value proposition
- Customer fit
- Revenue logic
- Cost considerations
- Operational requirements
- SWOT
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


    # ---------------------------------------------------------
    # TASK 5 — STRATEGY SYNTHESIS
    # ---------------------------------------------------------

    strategy_synthesis_task = Task(

        description="""
Act as the senior strategy consultant.

Synthesize all previous findings.

Business:
{business_name}

Business problem:
{business_problem}

Business strategy analysis:

{strategy_task}

Market analysis:

{market_task}

Competitive analysis:

{competitor_task}

Business analysis:

{business_analysis_task}

Develop:

1. Key strategic insights
2. Strategic options
3. Advantages and disadvantages of each option
4. Major trade-offs
5. Required capabilities
6. Implementation priorities
7. Major risks
8. Risk mitigation ideas
9. Suggested KPIs
10. Questions that still require validation

Do not present unsupported assumptions as facts.

The goal is not to produce generic business advice.
The strategy must be directly connected to the supplied
business situation and previous analysis.
""",

        expected_output="""
A strategic synthesis containing:

- Key insights
- Strategic options
- Trade-offs
- Required capabilities
- Implementation priorities
- Risks
- Mitigation approaches
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


    # ---------------------------------------------------------
    # TASK 6 — FINAL REPORT
    # ---------------------------------------------------------

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

Use the complete consulting analysis:

Business Strategy:
{strategy_task}

Market Research:
{market_task}

Competitive Analysis:
{competitor_task}

Business Analysis:
{business_analysis_task}

Strategy Synthesis:
{strategy_synthesis_task}

Create a professional report with the following structure:

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

Create a practical:
- 0–30 day phase
- 31–60 day phase
- 61–90 day phase

## 12. KPIs

## 13. Key Risks

## 14. Information Gaps

## 15. Next Steps

Important rules:

- Do not invent statistics.
- Do not invent competitor facts.
- Do not claim that research was performed on the internet.
- Clearly identify assumptions.
- Clearly distinguish supplied information from analysis.
- Avoid generic motivational language.
- Make the report practical and decision-oriented.
""",

        expected_output="""
A polished Markdown business consulting report containing
all requested sections.

The report must be structured, professional, specific to the
client's business problem and transparent about assumptions
and information gaps.
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


    # ---------------------------------------------------------
    # CREATE CREW
    # ---------------------------------------------------------

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


    # ---------------------------------------------------------
    # RUN CREW
    # ---------------------------------------------------------

    result = consulting_crew.kickoff(
        inputs=inputs
    )

    return result.raw
