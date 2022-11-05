from app import db

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)
    is_complete = db.Column(db.Boolean, default=False)
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'), nullable=True)

    def to_dict(self):
        return {
        "id": self.task_id, 
        "title": self.title,
        "description": self.description,
        "is_complete": self.is_complete
        }
    
    @classmethod
    def from_dict(cls, request):
        task = Task(title=request["title"], description=request["description"])
        return task