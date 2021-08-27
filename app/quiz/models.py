from dataclasses import dataclass
from typing import Optional


@dataclass
class Theme:
    id: Optional[int]
    title: str


@dataclass
class Answer:
    title: int
    is_correct: bool


@dataclass
class Question:
    title: str
    theme_id: int
    id: Optional[int]
    answers: list[Answer]
