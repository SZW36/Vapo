from flask_restful import Resource
from flask import request
from flask_bcrypt import Bcrypt
from vapo import db
from models import User

class CreateUser(Resource):
    def get(self):
        data = request.data
        username = data["username"]
        password = data["password"]
        # hash password
        bcrypt = Bcrypt()
        hashed_pwd = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, hashed_pwd=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        return 200

class Login(Resource):
    def post(self):
        data = request.data
        username = data["username"]
        password = data["password"]

        user = db.session.query(User).filter_by(username=username)

        if(not user):
            return False

        # hash password
        bcrypt = Bcrypt()
        match = bcrypt.check_password_hash(user.hashed_pwd, password)
        return match


