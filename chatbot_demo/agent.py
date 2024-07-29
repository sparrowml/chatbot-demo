from typing import Any

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.pydantic_v1 import BaseModel
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

SYSTEM_PROMPT = """
You are a helpful AI agent named Hal. Answer questions and provide information to users in a friendly and informative manner.

Use the tools available to you to find the best answers to the questions asked.

If you don't know the answer, just say "I don't know" and explain why, don't try to make up an answer.
"""


class Input(BaseModel):
    input: str


class Output(BaseModel):
    output: Any


def configure_agent() -> AgentExecutor:
    # Tools
    search = TavilySearchResults()
    tools = [search]

    # Model
    model = ChatOpenAI(model="gpt-4o")

    # Prompt
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            MessagesPlaceholder(variable_name="chat_history", optional=True),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    agent = create_tool_calling_agent(model, tools, prompt)
    return (
        AgentExecutor(agent=agent, tools=tools)
        .with_types(input_type=Input, output_type=Output)
        .with_config({"run_name": "agent"})
    )
