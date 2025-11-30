# tools/answer_evaluator.py
import re

def _count_metrics(answer):
    return len(re.findall(r"\d+%?|\d+\.\d+|\d+", answer))

def _star_structure_score(answer):
    s = answer.lower()
    score = 0
    for k in ["situation", "task", "action", "result", "challenge", "goal"]:
        if k in s:
            score += 1
    return min(10, int((score / 6) * 10))

def evaluate_answer(answer_text, question_metadata=None, resume_summary=None):
    words = len(answer_text.split())
    clarity = min(10, max(1, words // 8))
    structure = _star_structure_score(answer_text)
    relevance = 7
    if question_metadata and "expected_keywords" in question_metadata:
        expected = question_metadata["expected_keywords"]
        hits = sum(1 for kw in expected if kw.lower() in answer_text.lower())
        relevance = int(min(10, (hits / max(1,len(expected))) * 10))
    metrics_count = _count_metrics(answer_text)
    specificity = min(10, metrics_count * 3)
    confidence = 7
    if any(p in answer_text.lower() for p in ["maybe", "perhaps", "i think"]):
        confidence = max(1, confidence - 2)
    overall = round((0.3*clarity + 0.3*structure + 0.2*relevance + 0.2*specificity), 1)
    explainers = [f"word_count={words}", f"metrics_count={metrics_count}", f"structure_score={structure}"]
    return {
        "clarity": clarity,
        "structure": structure,
        "relevance": relevance,
        "specificity": specificity,
        "confidence": confidence,
        "overall_score": overall,
        "explainers": explainers
    }
