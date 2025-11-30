# tools/improved_answer.py
def generate_improved_answer(answer_text, evaluation, question_text=None):
    improved = []
    improved.append("Start with Situation & Task: briefly explain the context and goal.")
    improved.append("Next, describe the Actions you took in clear steps.")
    improved.append("Finally, state the Results with metrics when possible.")
    improved.append("")
    improved.append("Example improved answer (template):")
    improved.append(f"{answer_text}  (Tip: add quantifiable results and be concise.)")
    return "\n".join(improved)
