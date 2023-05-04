from flask import jsonify, Response
from Models.User import User, UserSession
import re
import hashlib
import jwt
from datetime import datetime, timedelta
from database import db
import os
from http import HTTPStatus


class Authenticate:
    def __init__(self, username=None, password=None):
        if username is None or password is None:
            return jsonify({"message": "You must enter a username and email or password"}), HTTPStatus.NO_CONTENT
            
        else:
            self.secret_word = os.getenv('JWT_SECRET_WORD')
            self.username = username
            self.password = password
    
    def check_user_exist(self, username):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, username):
            return True
        else:
            return False

    def check_authentication(self):
        username_is_mail = self.check_user_exist(self.username)
        user = None
        try:
            if username_is_mail:
                user = User.query.filter_by(email=self.username, password=hashlib.sha256(self.password.encode()).hexdigest()).first()
            else:
                user = User.query.filter_by(username=self.username, password=hashlib.sha256(self.password.encode()).hexdigest()).first()
            if user is None:
                return jsonify({'message': 'User not found check your email or password'}), HTTPStatus.NOT_FOUND
            return user
        except Exception as e:
            return jsonify({'message': 'BAD_REQUEST'}), HTTPStatus.BAD_REQUEST

    def auhtenticate(self):
        try:
            user = self.check_authentication()
            user_id = user.id
            encoded_jwt = jwt.encode({"exp" : datetime.now() + timedelta(days=14)}, self.secret_word, algorithm="HS256")
            exist_session = UserSession.query.filter_by(user_id=user_id).first()
            if exist_session and exist_session.expirate_at >= datetime.now():
                return jsonify({'message': "Already connected"}), HTTPStatus.NOT_MODIFIED
            else:
                create_session = UserSession(
                    token=encoded_jwt,
                    user_id=user.id
                )
            db.session.add(create_session)
            db.session.commit()
            return  jsonify({'token': encoded_jwt}), HTTPStatus.OK
        except Exception as e:
            return jsonify({'message': 'BAD_REQUEST' + str(e)}), HTTPStatus.BAD_REQUEST




            


 
       

        