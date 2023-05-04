from Models.User import User
from flask import jsonify, Response
from http import HTTPStatus
from database import db
import hashlib
from Authentication.Authentication import Authenticate
from Decorators.Security import is_authenticated


class UserController:
    def get_all_users():
        db.create_all()
        try:
            users = User.query.all()
            users_list = []
            for user in users:
                users_list.append(user.serialize())
            return users_list, HTTPStatus.OK
        except  Exception as e:
            return jsonify({"message": "BAD_REQUEST"}), HTTPStatus.BAD_REQUEST

    
    @is_authenticated
    def get_user_by_id(id):
        try:
            user = User.query.filter_by(id=id).first()
            if user is None:
                return jsonify({'message': 'USER NOT FOUND'}), HTTPStatus.NOT_FOUND
            return user.serialize(), HTTPStatus.OK
        except Exception as e:
            return jsonify({'message': "BAD_REQUEST", status: 500})


    def create_user(data):
        try:
            user = User(
                username=data['username'],
                email=data['email'],
                password=hashlib.sha256(data['password'].encode()).hexdigest(),
                is_verify=False
            )
            db.session.add(user)
            db.session.commit()
            return user.serialize(), HTTPStatus.CREATED
        except Exception as e:
            return jsonify({"message": "BAD_REQUEST" + str(e)}), HTTPStatus.BAD_REQUEST

    def authenticate(data):
        try:
            auth = Authenticate(username=data['username'], password=data['password'])
            return auth.auhtenticate()
        except Exception as e:
            return jsonify({"message": "BAD_REQUEST"}), HTTPStatus.BAD_REQUEST
        
