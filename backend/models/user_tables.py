from vapo import db

# testing db schema
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    posts = db.Column(db.String(100), nullable=False)

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable=False)

class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)