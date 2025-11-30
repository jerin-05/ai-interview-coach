# agents/interview_orchestrator.py
import uuid
from datetime import datetime

class InterviewOrchestrator:
    """
    Orchestrates a simple interview: question -> evaluate -> feedback.
    For demo we keep a local sessions dict; later swap to Memory/Session services.
    """

    def __init__(self, question_agent, evaluator_agent, feedback_agent):
        self.question_agent = question_agent
        self.evaluator_agent = evaluator_agent
        self.feedback_agent = feedback_agent
        self.sessions = {}

    def start_session(self, user_id="user-1"):
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = {
            "user_id": user_id,
            "start_time": datetime.utcnow().isoformat(),
            "questions": []
        }
        return session_id

    def ask_question(self, session_id, topic="behavioral", level="medium", resume_summary=None):
        meta = self.question_agent.generate_question(topic=topic, level=level, resume_summary=resume_summary)
        self.sessions[session_id]["questions"].append({
            "q_id": str(uuid.uuid4()),
            "text": meta["text"],
            "topic": meta["topic"],
            "difficulty": meta.get("difficulty", level),
            "time_asked": datetime.utcnow().isoformat(),
            "answer": None,
            "evaluation": None,
            "feedback": None
        })
        return meta

    def submit_answer(self, session_id, answer_text):
        q = self.sessions[session_id]["questions"][-1]
        q_text = q["text"]
        q_meta = {"topic": q.get("topic"), "difficulty": q.get("difficulty")}
        evaluation = self.evaluator_agent.evaluate(answer_text, question_metadata=q_meta)
        feedback = self.feedback_agent.generate_feedback(evaluation, answer_text=answer_text, question_text=q_text)
        q["answer"] = answer_text
        q["evaluation"] = evaluation
        q["feedback"] = feedback
        q["time_answered"] = datetime.utcnow().isoformat()
        return {"evaluation": evaluation, "feedback": feedback}

    def get_session(self, session_id):
        return self.sessions.get(session_id)
