from app import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    importance_level = db.Column(db.Integer, default=1)
    
    # RELATIONSHIP AS REQUIRED
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)