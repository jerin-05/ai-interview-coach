# memory/session_service.py
from datetime import datetime
import uuid

class InMemorySessionService:
    """
    Simple session service for demo & Kaggle requirement.
    Stores sessions in a dict for the current process.
    """
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id="user-1"):
        sid = str(uuid.uuid4())
        self.sessions[sid] = {
            "user_id": user_id,
            "created_at": datetime.utcnow().isoformat(),
            "questions": []
        }
        return sid

    def add_question(self, session_id, question_meta):
        self.sessions[session_id]["questions"].append(question_meta)

    def update_question(self, session_id, q_index, data):
        self.sessions[session_id]["questions"][q_index].update(data)

    def get_session(self, session_id):
        return self.sessions.get(session_id)
