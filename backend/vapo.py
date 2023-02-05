from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
app.debug = True

# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

# Settings for migrations
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    hashed_pwd = db.Column(db.String(100), nullable=False)
    date_joined = db.Column(db.DateTime)
    free_days = db.Column(db.Integer)
    target = db.Column(db.Integer)
    group_id = db.Column(db.Integer)

    posts = db.relationship('Post', backref='users')

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.DateTime, nullable=False)
    num_of_members = db.Column(db.Integer)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime)
    content = db.Column(db.String(100), nullable=False)

    subposts = db.relationship('Subpost', backref='post')

class Subpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))
    date = db.Column(db.DateTime)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

from flask_restful import Resource
from flask import request
from flask_bcrypt import Bcrypt
import json
from datetime import datetime
from sqlalchemy import or_

class CreateUser(Resource):
    def post(self):
        # get imputs 
        data = request.data
        data = json.loads(data)
        username = data["username"]
        password = data["password"]

        # hash password
        bcrypt = Bcrypt()
        hashed_pwd = bcrypt.generate_password_hash(password).decode('utf-8')

        # find a group or generate a group
        group = Group.query.filter(or_(Group.creation_date == datetime.today().date(), Group.num_of_members < 7)).first()
        if(not group):
            group = Group(creation_date=datetime.now(), num_of_members=0)
            db.session.add(group)
        group.num_of_members += 1 
        db.session.commit()

        user = User(username=username, hashed_pwd=hashed_pwd, date_joined=datetime.now(), free_days=0, target=7, group_id=group.id)
        db.session.add(user)
        db.session.commit()
        return 200
api.add_resource(CreateUser, '/create_user')

class Login(Resource):
    def post(self):
        data = request.data
        data = json.loads(data)
        print(data)
        username = data["username"]
        password = data["password"]

        user = db.session.query(User).filter_by(username=username).first()

        if(not user):
            return {"success": False, "user_id": None}

        # hash password
        bcrypt = Bcrypt()
        match = bcrypt.check_password_hash(user.hashed_pwd, password)
        if(match):
            return {"success": True, "user_id": user.id}
        else:
            return {"success": False, "user_id": None}

api.add_resource(Login, '/login')


# class Posts(Resource):
#     def post(self):
#         data = request.data
#         data = json.loads(data)
#         print(data)
#         username = data["username"]
#         password = data["password"]

#         user = db.session.query(User).filter_by(username=username).first()

#         if(not user):
#             return {"success": False, "user_id": None}

#         # hash password
#         bcrypt = Bcrypt()
#         match = bcrypt.check_password_hash(user.hashed_pwd, password)
#         if(match):
#             return {"success": True, "user_id": user.id}
#         else:
#             return {"success": False, "user_id": None}

# api.add_resource(Login, '/login')


if __name__ == '__main__':
    app.run()