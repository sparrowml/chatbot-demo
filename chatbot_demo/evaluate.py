import pandas as pd
from tqdm import tqdm

from .agent import configure_agent
from .config import Config


def evaluate_model() -> None:
    """
    Evaluate the chatbot model.
    """
    agent = configure_agent()
    questions_df = pd.read_csv(Config.questions_path)
    correct = 0
    total = 0
    for row in tqdm(list(questions_df.itertuples())):
        total += 1
        response = agent.invoke({"input": row.question})
        if row.response_substring in response["output"]:
            correct += 1
    print(f"Accuracy: {correct / total:.2f}")
