# agents/feedback_agent.py
from tools.improved_answer import generate_improved_answer

class FeedbackAgent:
    def __init__(self):
        pass

    def generate_feedback(self, evaluation, answer_text=None, question_text=None):
        overall = evaluation.get("overall_score", 0)
        if overall >= 7:
            short = "Good answer — mostly strong. Tighten the structure and add metrics where possible."
        elif overall >= 4:
            short = "Decent, but add clearer structure (STAR) and more specific results."
        else:
            short = "Weak — try to state the situation, actions you took, and measurable results."

        improved = generate_improved_answer(answer_text or "", evaluation, question_text=question_text)
        suggestions = [
            "Practice giving the STAR structure in under 90 seconds.",
            "Include one measurable result in each example.",
            "Use active verbs to describe your actions."
        ]

        return {
            "short_feedback": short,
            "improved_answer": improved,
            "suggestions": suggestions
        }
