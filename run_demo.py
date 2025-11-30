# run_demo.py
"""
Run a simple local demo of the AI Interview Coach pipeline.
Usage: python run_demo.py
"""
from agents.question_agent import QuestionAgent
from agents.evaluation_agent import EvaluationAgent
from agents.feedback_agent import FeedbackAgent
from agents.interview_orchestrator import InterviewOrchestrator
from memory.session_service import InMemorySessionService
import json

def main():
    # create agents
    q_agent = QuestionAgent()
    e_agent = EvaluationAgent()
    f_agent = FeedbackAgent()

    # orchestrator (for demo we still pass agents directly; session service optional)
    orchestrator = InterviewOrchestrator(q_agent, e_agent, f_agent)

    # start a session
    sid = orchestrator.start_session(user_id="sherin")
    qmeta = orchestrator.ask_question(sid, topic="technical")
    print("QUESTION:", qmeta["text"])

    # sample answer; replace with your own when testing
    answer = "I improved query performance by 40% by adding proper indexes and optimizing joins."
    result = orchestrator.submit_answer(sid, answer)

    print("\nEVALUATION:")
    print(json.dumps(result["evaluation"], indent=2))

    print("\nFEEDBACK:")
    print(json.dumps(result["feedback"], indent=2))

    print("\nSession snapshot:")
    print(json.dumps(orchestrator.get_session(sid), indent=2))

    print("\nThumbnail / card image path (for Kaggle):")
    print("/mnt/data/b0425ad7-6f07-431a-8d4d-a0a19c366205.png")

if __name__ == "__main__":
    main()
