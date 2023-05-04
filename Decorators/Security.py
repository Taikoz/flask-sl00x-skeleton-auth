from flask import jsonify, request
from Models.User import UserSession
import os
from datetime import datetime

def is_authenticated(func):
    def wrapper(*args, **kwargs):
        try:
            data = request.headers["Authorization"]
            token = str.replace(str(data), "Bearer ", "")
            if token:
                user_session = UserSession.query.filter_by(token=token).first()
                if user_session.expirate_at <= datetime.now():
                    return jsonify({"message": "Session expired", "status": 400})
                else:
                    return func(*args)
        except Exception as e:
            return jsonify({"message": "You are not authenticated", "status": 400})
    return wrapper