# evaluation/evaluate_harness.py
import json
from tools.answer_evaluator import evaluate_answer
from math import sqrt

def run_evaluation(sample_path="evaluation/sample_qna.json"):
    with open(sample_path, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    results = []
    errors = []
    for row in dataset:
        qmeta = {"topic": "behavioral"}  # basic
        eval_res = evaluate_answer(row["answer"], question_metadata=qmeta)
        results.append({
            "question": row["question"],
            "human": row["human_score"],
            "auto": eval_res["overall_score"]
        })

    # compute simple RMSE
    n = len(results)
    mse = sum((r["human"] - r["auto"])**2 for r in results) / max(1,n)
    rmse = sqrt(mse)
    print("Evaluation results (sample):")
    for r in results:
        print(f'Q: {r["question"]}\n  human={r["human"]} auto={r["auto"]}\n')
    print(f"RMSE: {rmse:.3f}")

if __name__ == "__main__":
    run_evaluation()
