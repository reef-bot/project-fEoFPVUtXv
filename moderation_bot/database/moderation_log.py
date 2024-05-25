# moderation_bot/database/moderation_log.py

import pymongo
from datetime import datetime

class ModerationLog:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["moderation_log"]
        self.collection = self.db["logs"]

    def log_action(self, user_id, action, reason):
        log_entry = {
            "user_id": user_id,
            "action": action,
            "reason": reason,
            "timestamp": datetime.now()
        }
        self.collection.insert_one(log_entry)

    def get_logs(self, user_id=None):
        if user_id:
            logs = self.collection.find({"user_id": user_id})
        else:
            logs = self.collection.find()
        return logs

    def clear_logs(self):
        self.collection.delete_many({})

# End of moderation_bot/database/moderation_log.py