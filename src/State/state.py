from typing import TypedDict, List

class State(TypedDict):
    questions: List[str]
    answers: List[str]
    evaluation_reports: List[str]
    question_number: int

    role: str
    difficulty: str
    subject: str

    final_report: str