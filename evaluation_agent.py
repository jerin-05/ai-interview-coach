# agents/evaluation_agent.py
from tools.answer_evaluator import evaluate_answer

class EvaluationAgent:
    def __init__(self):
        pass

    def evaluate(self, answer_text, question_metadata=None, resume_summary=None):
        return evaluate_answer(answer_text, question_metadata=question_metadata, resume_summary=resume_summary)
