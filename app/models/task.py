from app import db

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)
    is_complete = db.Column(db.Boolean, default=False)
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'), nullable=True)
    goal = db.relationship("Goal", back_populates="tasks")

    def to_dict(self):
        task_dict = {
        "id": self.task_id, 
        "title": self.title,
        "description": self.description,
        "is_complete": self.is_complete
        }
        return task_dict

    def to_dict_goal_id(self):
        task_dict_with_goal_id = {
        "id": self.task_id, 
        "title": self.title,
        "description": self.description,
        "is_complete": self.is_complete,
        "goal_id" : self.goal_id
        }
        return task_dict_with_goal_id

    @classmethod
    def from_dict(cls, request):
        task = Task(title=request["title"], description=request["description"])
        return task