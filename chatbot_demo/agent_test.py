from .agent import configure_agent


def test_agent_name_is_hal():
    agent = configure_agent()
    result = agent.invoke({"input": "What is your name?"})
    assert "Hal" in result["output"]
