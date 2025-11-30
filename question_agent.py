# agents/question_agent.py
from tools.question_generator import generate_question

class QuestionAgent:
    def __init__(self):
        pass

    def generate_question(self, topic="behavioral", level="medium", resume_summary=None):
        return generate_question(topic=topic, level=level, resume_summary=resume_summary)
