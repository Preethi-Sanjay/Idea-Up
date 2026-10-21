
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


def build_chain():
    llm = ChatOllama(
        model="qwen2.5:3b",
        temperature=0.4,
        num_predict=350
    )

    parser = StrOutputParser()

    # 1. Generate the startup idea
    idea_prompt = ChatPromptTemplate.from_template("""
    Generate one concise startup idea for this problem:
    {problem}

    Include:
    - Startup name and tagline
    - Problem and solution
    - Target users
    - Unique value proposition

    Keep the response under 200 words.
    """)

    # 2. Generate product features
    feature_prompt = ChatPromptTemplate.from_template("""
    Based on this startup idea:
    {idea}

    Suggest exactly 4 essential MVP features and 3 future features.
    Give each MVP feature a one-sentence description.
    Keep the response under 250 words.
    """)

    # 3. Generate a practical MVP plan
    mvp_prompt = ChatPromptTemplate.from_template("""
    Create a realistic one-week MVP plan for this startup.

    Startup idea:
    {idea}

    Features:
    {features}

    Include:
    - A simple, suitable technology stack
    - 5 practical development steps
    - A day-by-day plan for 7 days

    Assume one student developer.
    Do not suggest training an AI model from scratch.
    Prioritize a working prototype.
    Keep the response under 250 words.
    """)

    # Build individual chains
    idea_chain = idea_prompt | llm | parser
    feature_chain = feature_prompt | llm | parser
    mvp_chain = mvp_prompt | llm | parser

    # Execute each stage in sequence
    return (
        RunnablePassthrough.assign(idea=idea_chain)
        | RunnablePassthrough.assign(features=feature_chain)
        | RunnablePassthrough.assign(mvp=mvp_chain)
    )
