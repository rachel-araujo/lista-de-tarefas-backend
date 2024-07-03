from config import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    completed = db.Column(db.Boolean, default=False)

    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }
