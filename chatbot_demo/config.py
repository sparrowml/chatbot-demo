from pathlib import Path
from dataclasses import dataclass


@dataclass
class Config:
    data_directory = Path("/code/data")
    questions_path = data_directory / "questions.csv"
