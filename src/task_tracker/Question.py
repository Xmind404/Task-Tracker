from datetime import datetime

class Question:
    def __init__(self, description, status, created_at=None, updated_at=None):
        self.description = description
        self.status = status
        self.created_at = created_at if created_at else datetime.now().isoformat()
        self.updated_at = updated_at if updated_at else datetime.now().isoformat()

    def update(self, changed):
        self.description = changed
        self.updated_at = datetime.now().isoformat()

    def change_status(self, new_status):
        self.status = new_status
        self.updated_at = datetime.now().isoformat()