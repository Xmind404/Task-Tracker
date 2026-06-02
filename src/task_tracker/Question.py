class Question:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def update(self, changed):
        self.name = changed

    def change_status(self, new_status):
        self.status = new_status