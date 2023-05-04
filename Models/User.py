from database import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func
from datetime import timedelta, datetime


class User(db.Model):
    id = db.Column(UUID(as_uuid=True), unique=True, primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_verify = db.Column(db.Boolean, nullable=True, default=False)
    sessions = db.relationship('UserSession', backref='user', lazy=True)
    create_at = db.Column(db.DateTime, server_default=func.now())
    update_at = db.Column(db.DateTime, onupdate=func.now())
    

    def __init__(self, username, email, password, is_verify):
        self.username = username
        self.email = email
        self.password = password
        self.is_verify= is_verify
        

    def serialize(self):
        return {
            "uuid": str(self.id),
            "email": self.email,
            "username": self.username,
            "is_verify": self.is_verify
           
        }

    def __repr__(self):
        return '<User %r>' % self.username

class UserSession(db.Model):
    
    id = db.Column(UUID(as_uuid=True), unique=True, primary_key=True, default=uuid.uuid4)
    token = db.Column(db.String(255), nullable=False, unique=True)
    create_at = db.Column(db.DateTime, server_default=func.now())
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey(User.id), nullable=False)
    expirate_at = db.Column(db.DateTime, default=datetime.utcnow() + timedelta(days=14))
    

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def __repr__(self):
            return '<Session %r>' % self.user.username
