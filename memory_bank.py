# memory/memory_bank.py
import json
from collections import defaultdict

class MemoryBank:
    """
    Very small local memory bank to store aggregated user stats.
    For production consider a DB or vector store.
    """
    def __init__(self, path="memory/memory_bank.json"):
        self.path = path
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                self.store = json.load(f)
        except Exception:
            self.store = {}

    def save_profile(self, user_id, profile):
        self.store[user_id] = profile
        self._flush()

    def get_profile(self, user_id):
        return self.store.get(user_id, {})

    def _flush(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.store, f, indent=2)
