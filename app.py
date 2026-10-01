import streamlit as st

from crew import run_business_consulting


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Business Consulting AI",
    page_icon="📊",
    layout="wide"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #8b949e;
        margin-bottom: 30px;
    }

    .agent-card {
        padding: 15px;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.2);
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">📊 Business Consulting AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Multi-Agent Business Research & Strategy System'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.header("🤖 Consulting Team")

    st.write(
        "Six specialized AI consultants work together "
        "to analyze the business problem."
    )

    st.divider()

    st.write("1️⃣ Business Strategist")
    st.write("2️⃣ Market Researcher")
    st.write("3️⃣ Competitor Analyst")
    st.write("4️⃣ Business Analyst")
    st.write("5️⃣ Strategy Consultant")
    st.write("6️⃣ Report Consultant")

    st.divider()

    st.caption(
        "Powered by CrewAI + Groq GPT-OSS 120B"
    )


# ---------------------------------------------------------
# INPUT FORM
# ---------------------------------------------------------

st.subheader("📋 Business Information")

business_name = st.text_input(
    "Business / Company Name",
    placeholder="Example: HealthTech Solutions"
)

business_problem = st.text_area(
    "What business problem are you trying to solve?",
    placeholder=(
        "Example: We want to determine whether our "
        "digital pharmacy service can expand into another market."
    ),
    height=120
)

col1, col2 = st.columns(2)

with col1:

    target_customer = st.text_area(
        "Target Customer",
        placeholder="Who is the customer?",
        height=100
    )

with col2:

    target_market = st.text_input(
        "Target Market / Industry",
        placeholder="Example: Digital healthcare"
    )


competitors = st.text_area(
    "Known Competitors",
    placeholder=(
        "List any competitors you already know. "
        "If none are known, write 'None known'."
    ),
    height=100
)


research = st.text_area(
    "Additional Business Information / Research",
    placeholder=(
        "Paste any information you already have here: "
        "market notes, customer interviews, pricing, "
        "business model, reports, observations, etc."
    ),
    height=180
)


# ---------------------------------------------------------
# GENERATE BUTTON
# ---------------------------------------------------------

st.divider()

generate = st.button(
    "🚀 Generate Business Strategy",
    type="primary",
    use_container_width=True
)


# ---------------------------------------------------------
# RUN CONSULTING CREW
# ---------------------------------------------------------

if generate:

    if not business_problem.strip():

        st.error(
            "Please describe the business problem first."
        )

        st.stop()


    inputs = {

        "business_name": business_name.strip(),

        "business_problem": business_problem.strip(),

        "target_customer": target_customer.strip(),

        "target_market": target_market.strip(),

        "competitors": competitors.strip(),

        "research": research.strip()
    }


    st.divider()

    st.subheader("🤖 Consulting Team Working")

    progress = st.empty()

    progress.info(
        "The consulting team is analyzing your business. "
        "This may take a few minutes because multiple agents "
        "are running sequentially."
    )


    try:

        with st.spinner(
            "Business Consulting Team is working..."
        ):

            final_report = run_business_consulting(
                inputs
            )


        progress.success(
            "✅ All six consulting agents completed."
        )


        st.divider()

        st.subheader("📊 Business Strategy Report")

        st.markdown(final_report)


        st.divider()

        st.download_button(
            label="📥 Download Report",
            data=final_report,
            file_name="business_strategy_report.md",
            mime="text/markdown",
            use_container_width=True
        )


    except Exception as e:

        progress.error(
            "❌ The consulting crew could not complete the analysis."
        )

        st.error(
            "An error occurred while running the AI team."
        )

        with st.expander("Technical error"):

            st.code(
                str(e)
            )
