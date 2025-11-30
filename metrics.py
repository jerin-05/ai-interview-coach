# observability/metrics.py
from prometheus_client import Counter, Gauge, Histogram

SESSIONS = Counter("ai_sessions_total", "Total sessions started")
QUESTIONS = Counter("ai_questions_total", "Total questions asked")
EVALUATION_TIME = Histogram("ai_evaluation_seconds", "Time taken to evaluate answers")
AVG_SCORE = Gauge("ai_average_score", "Latest overall score")
